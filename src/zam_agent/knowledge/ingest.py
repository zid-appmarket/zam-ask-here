"""Knowledge ingestion pipeline: loaders -> documents -> chunks -> index.

``KnowledgeBase`` is the only thing the rest of the app touches. It owns the
index, can rebuild it on demand (``scripts/ingest.py``, a cron job, or the
``/health`` reload hook) and swaps the live index atomically so in-flight
requests never see a half-built index.
"""

from __future__ import annotations

import datetime as _dt
import json
import os
import tempfile
import threading
import time
from collections.abc import Sequence
from dataclasses import dataclass, field
from pathlib import Path

from ..config import KnowledgeConfig
from ..observability.logging import get_logger
from .documents import Chunk, Document, DocumentError, chunk_document
from .index import Evidence, KnowledgeIndex, RetrievalResult
from .loaders.base import KnowledgeLoader, LoaderError, LoaderNotConfigured
from .loaders.gdrive_loader import GoogleDriveLoader
from .loaders.markdown_loader import MarkdownLoader
from .loaders.notion_loader import NotionLoader

log = get_logger(__name__)


@dataclass
class IngestReport:
    documents: int = 0
    chunks: int = 0
    duration_seconds: float = 0.0
    per_loader: dict[str, int] = field(default_factory=dict)
    skipped_loaders: dict[str, str] = field(default_factory=dict)
    duplicate_doc_ids: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    by_product: dict[str, int] = field(default_factory=dict)
    by_status: dict[str, int] = field(default_factory=dict)
    stale_documents: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, object]:
        return {
            "documents": self.documents,
            "chunks": self.chunks,
            "duration_seconds": round(self.duration_seconds, 3),
            "per_loader": self.per_loader,
            "skipped_loaders": self.skipped_loaders,
            "duplicate_doc_ids": self.duplicate_doc_ids,
            "errors": self.errors,
            "by_product": self.by_product,
            "by_status": self.by_status,
            "stale_documents": self.stale_documents,
        }


def default_loaders(config: KnowledgeConfig, *, strict: bool = False) -> list[KnowledgeLoader]:
    return [
        MarkdownLoader(directory=config.directory, strict=strict),
        NotionLoader(
            api_key=config.notion_api_key,
            database_ids=config.notion_database_ids,
            page_ids=config.notion_page_ids,
        ),
        GoogleDriveLoader(
            credentials_file=config.gdrive_credentials_file,
            folder_ids=config.gdrive_folder_ids,
            file_ids=config.gdrive_file_ids,
        ),
    ]


class KnowledgeBase:
    """Thread-safe holder of the live knowledge index."""

    def __init__(
        self,
        config: KnowledgeConfig,
        *,
        loaders: Sequence[KnowledgeLoader] | None = None,
        strict: bool = False,
    ) -> None:
        self.config = config
        self.strict = strict
        self._loaders = list(loaders) if loaders is not None else default_loaders(config, strict=strict)
        self._lock = threading.RLock()
        self._index = KnowledgeIndex()
        self._report = IngestReport()
        self._loaded_at: float | None = None

    # ------------------------------------------------------------------ state

    @property
    def index(self) -> KnowledgeIndex:
        with self._lock:
            return self._index

    @property
    def report(self) -> IngestReport:
        with self._lock:
            return self._report

    @property
    def loaded_at(self) -> float | None:
        return self._loaded_at

    @property
    def is_empty(self) -> bool:
        return len(self.index) == 0

    def status(self) -> dict[str, object]:
        report = self.report
        return {
            "documents": report.documents,
            "chunks": report.chunks,
            "loaded_at": self._loaded_at,
            "by_product": report.by_product,
            "by_status": report.by_status,
            "stale_documents": len(report.stale_documents),
            "errors": report.errors,
            "skipped_loaders": report.skipped_loaders,
        }

    # ---------------------------------------------------------------- loading

    def reload(self, *, today: _dt.date | None = None) -> IngestReport:
        started = time.perf_counter()
        report = IngestReport()
        today = today or _dt.date.today()

        documents: dict[str, Document] = {}
        for loader in self._loaders:
            name = getattr(loader, "name", loader.__class__.__name__)
            try:
                if not loader.enabled():
                    report.skipped_loaders[name] = "not configured"
                    continue
                count = 0
                for document in loader.load():
                    if document.doc_id in documents:
                        report.duplicate_doc_ids.append(document.doc_id)
                        log.warning(
                            "duplicate knowledge document id -- keeping the first",
                            extra={
                                "context": {
                                    "doc_id": document.doc_id,
                                    "kept": documents[document.doc_id].source,
                                    "dropped": document.source,
                                }
                            },
                        )
                        continue
                    documents[document.doc_id] = document
                    count += 1
                report.per_loader[name] = count
            except LoaderNotConfigured as exc:
                report.skipped_loaders[name] = str(exc)
            except (LoaderError, DocumentError) as exc:
                report.errors.append(f"{name}: {exc}")
                log.error("knowledge loader failed", extra={"context": {"loader": name, "error": str(exc)}})
                if self.strict:
                    raise
            except Exception as exc:  # pragma: no cover - defensive
                report.errors.append(f"{name}: unexpected {type(exc).__name__}")
                log.exception("knowledge loader crashed", extra={"context": {"loader": name}})
                if self.strict:
                    raise

        chunks: list[Chunk] = []
        for document in documents.values():
            chunks.extend(
                chunk_document(
                    document,
                    target_chars=self.config.chunk_target_chars,
                    overlap_chars=self.config.chunk_overlap_chars,
                )
            )
            report.by_product[document.product] = report.by_product.get(document.product, 0) + 1
            report.by_status[document.status] = report.by_status.get(document.status, 0) + 1
            if document.is_stale(self.config.max_age_days, today):
                report.stale_documents.append(document.doc_id)

        report.documents = len(documents)
        report.chunks = len(chunks)
        report.duration_seconds = time.perf_counter() - started

        index = KnowledgeIndex(chunks)
        with self._lock:
            self._index = index
            self._report = report
            self._loaded_at = time.time()

        log.info("knowledge index rebuilt", extra={"context": report.to_dict()})
        return report

    # -------------------------------------------------------------- retrieval

    def retrieve(
        self,
        query: str,
        *,
        product: str | None = None,
        allow_internal: bool = True,
        allow_restricted: bool = False,
        top_k: int | None = None,
        today: _dt.date | None = None,
    ) -> RetrievalResult:
        audiences: list[str] = ["all"]
        if allow_internal:
            audiences.append("internal")
        if allow_restricted:
            audiences.append("restricted")
        return self.index.search(
            query,
            top_k=top_k if top_k is not None else self.config.top_k,
            min_score=self.config.min_score,
            product=product,
            allowed_audiences=tuple(audiences),
            max_age_days=self.config.max_age_days,
            today=today,
        )

    # -------------------------------------------------------------- snapshots

    def write_snapshot(self, path: str | None = None) -> str:
        """Persist a human-readable audit snapshot of what the bot can cite."""

        target = Path(path or self.config.snapshot_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "generated_at": _dt.datetime.now(_dt.UTC).isoformat(),
            "report": self.report.to_dict(),
            "documents": [
                {
                    "doc_id": doc.doc_id,
                    "title": doc.title,
                    "product": doc.product,
                    "audience": doc.audience,
                    "status": doc.status,
                    "updated": doc.updated.isoformat() if doc.updated else None,
                    "owner": doc.owner,
                    "tags": list(doc.tags),
                    "source": doc.source,
                    "source_url": doc.source_url,
                    "chars": len(doc.body),
                }
                for doc in sorted(self.index.documents, key=lambda d: d.doc_id)
            ],
        }
        fd, tmp = tempfile.mkstemp(dir=str(target.parent), suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as handle:
                json.dump(payload, handle, ensure_ascii=False, indent=2)
            os.replace(tmp, target)
        finally:
            if os.path.exists(tmp):
                os.unlink(tmp)
        return str(target)


def format_evidence_block(evidence: Sequence[Evidence], *, max_chars: int = 1400) -> str:
    """Render retrieved evidence for the model, with stable citation labels."""

    parts: list[str] = []
    for item in evidence:
        doc = item.document
        text = item.chunk.text.strip()
        if len(text) > max_chars:
            text = text[:max_chars].rstrip() + " …"
        header = (
            f"[{item.label}] title={doc.title!r} product={doc.product} status={doc.status} "
            f"updated={doc.updated.isoformat() if doc.updated else 'unknown'}"
        )
        if doc.source_url:
            header += f" url={doc.source_url}"
        parts.append(f"{header}\n{text}")
    return "\n\n".join(parts)
