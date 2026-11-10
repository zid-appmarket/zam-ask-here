"""Load approved Google Drive documents as knowledge documents.

Requires the optional extra::

    pip install '.[gdrive]'      # google-api-python-client + google-auth

Authentication is a **service account** with read-only Drive scope; share the
approved folder (or document) with the service account's e-mail. Only the IDs
listed in ``GOOGLE_DRIVE_FOLDER_IDS`` and ``GOOGLE_DRIVE_FILE_IDS`` are read,
so the agent cannot reach documents nobody approved. Use ``_FILE_IDS`` when the
canonical source is one Doc rather than a folder. Google Docs are exported as plain text; metadata comes from
Drive ``appProperties`` (preferred) or the file's own description, using the
same keys as Markdown front matter.
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from typing import Any

import yaml

from ...observability.logging import get_logger
from ..documents import Document, build_document
from .base import KnowledgeLoader, LoaderError, LoaderNotConfigured

log = get_logger(__name__)

SCOPES = ("https://www.googleapis.com/auth/drive.readonly",)
EXPORTABLE = {
    "application/vnd.google-apps.document": "text/plain",
}
DOWNLOADABLE = {"text/plain", "text/markdown", "text/x-markdown"}


@dataclass
class GoogleDriveLoader(KnowledgeLoader):
    credentials_file: str | None
    folder_ids: tuple[str, ...] = ()
    file_ids: tuple[str, ...] = ()
    name: str = "gdrive"

    def enabled(self) -> bool:
        return bool(self.credentials_file) and bool(self.folder_ids or self.file_ids)

    def load(self) -> Iterator[Document]:
        if not self.enabled():
            raise LoaderNotConfigured(
                "GOOGLE_DRIVE_CREDENTIALS_FILE plus GOOGLE_DRIVE_FOLDER_IDS "
                "and/or GOOGLE_DRIVE_FILE_IDS required"
            )
        service = self._build_service()
        seen: set[str] = set()

        for folder_id in self.folder_ids:
            for meta in self._list_folder(service, folder_id):
                if meta["id"] in seen:
                    continue
                seen.add(meta["id"])
                document = self._safe_convert(service, meta)
                if document is not None:
                    yield document

        # Individually approved documents, for when the canonical source is a
        # single Doc rather than a folder.
        for file_id in self.file_ids:
            if file_id in seen:
                continue
            seen.add(file_id)
            single = self._file_metadata(service, file_id)
            if single is None:
                continue
            document = self._safe_convert(service, single)
            if document is not None:
                yield document

    def _safe_convert(self, service: Any, meta: dict[str, Any]) -> Document | None:
        try:
            return self._file_to_document(service, meta)
        except LoaderError as exc:
            log.warning(
                "skipping Drive file",
                extra={"context": {"file_id": meta.get("id"), "error": str(exc)}},
            )
            return None

    def _file_metadata(self, service: Any, file_id: str) -> dict[str, Any] | None:
        fields = "id, name, mimeType, modifiedTime, description, webViewLink, appProperties"
        try:
            return dict(
                service.files().get(fileId=file_id, fields=fields, supportsAllDrives=True).execute()
            )
        except Exception as exc:  # noqa: BLE001 - the client raises its own error types
            log.warning(
                "could not read Drive file metadata",
                extra={"context": {"file_id": file_id, "error": type(exc).__name__}},
            )
            return None

    def _build_service(self) -> Any:
        try:
            from google.oauth2 import service_account
            from googleapiclient.discovery import build
        except ImportError as exc:  # pragma: no cover - optional extra
            raise LoaderNotConfigured(
                "Google Drive support needs the optional extra: pip install '.[gdrive]'"
            ) from exc
        credentials = service_account.Credentials.from_service_account_file(
            self.credentials_file, scopes=list(SCOPES)
        )
        return build("drive", "v3", credentials=credentials, cache_discovery=False)

    def _list_folder(self, service: Any, folder_id: str) -> Iterator[dict[str, Any]]:
        page_token: str | None = None
        fields = "nextPageToken, files(id, name, mimeType, modifiedTime, description, webViewLink, appProperties)"
        while True:
            response = (
                service.files()
                .list(
                    q=f"'{folder_id}' in parents and trashed = false",
                    fields=fields,
                    pageToken=page_token,
                    pageSize=100,
                    supportsAllDrives=True,
                    includeItemsFromAllDrives=True,
                )
                .execute()
            )
            for item in response.get("files", []):
                if item.get("mimeType") == "application/vnd.google-apps.folder":
                    yield from self._list_folder(service, item["id"])
                else:
                    yield item
            page_token = response.get("nextPageToken")
            if not page_token:
                return

    def _file_to_document(self, service: Any, meta: dict[str, Any]) -> Document | None:
        mime = meta.get("mimeType", "")
        file_id = meta["id"]
        if mime in EXPORTABLE:
            body = (
                service.files()
                .export(fileId=file_id, mimeType=EXPORTABLE[mime])
                .execute()
            )
        elif mime in DOWNLOADABLE:
            body = service.files().get_media(fileId=file_id).execute()
        else:
            log.info("skipping unsupported Drive mime type", extra={"context": {"mime": mime}})
            return None
        text = body.decode("utf-8", "replace") if isinstance(body, bytes) else str(body)
        if not text.strip():
            return None

        defaults: dict[str, Any] = {
            "title": meta.get("name") or "Untitled Drive document",
            "id": f"gdrive-{file_id[:12]}",
            "updated": meta.get("modifiedTime"),
            "source_url": meta.get("webViewLink"),
        }
        defaults.update(_metadata_from_drive(meta))
        return build_document(raw=text, source=f"gdrive:{file_id}", defaults=defaults)


def _metadata_from_drive(meta: dict[str, Any]) -> dict[str, Any]:
    """Read front-matter-style keys from appProperties, else the description."""

    props = {str(k).lower(): v for k, v in (meta.get("appProperties") or {}).items()}
    if props:
        return props
    description = (meta.get("description") or "").strip()
    if not description:
        return {}
    try:
        parsed = yaml.safe_load(description)
    except yaml.YAMLError:
        return {}
    return {str(k).lower(): v for k, v in parsed.items()} if isinstance(parsed, dict) else {}
