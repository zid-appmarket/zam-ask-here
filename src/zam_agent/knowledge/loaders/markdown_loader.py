"""Load knowledge from a directory of Markdown/text files.

This is the default and recommended source: the files live in git, so every
change to what the bot is allowed to say is reviewed like code.

Layout convention (the directory name sets the default ``product``):

    knowledge/
      zam/…            -> product: zam
      theme-market/…   -> product: theme_market
      general/…        -> product: general

Front matter on the file always wins over the directory default. Files and
directories whose name starts with ``_`` or ``.`` are ignored, so templates and
notes can live alongside real content.
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path

from ...observability.logging import get_logger
from ..documents import Document, DocumentError, build_document, normalize_product
from .base import KnowledgeLoader, LoaderNotConfigured

log = get_logger(__name__)

TEXT_SUFFIXES = {".md", ".markdown", ".mdx", ".txt"}
# Repository housekeeping files are documentation about the knowledge base,
# not knowledge. Ingesting them would let the bot "cite" its own README.
EXCLUDED_NAMES = {"readme", "contributing", "license", "licence", "changelog", "index"}


@dataclass
class MarkdownLoader(KnowledgeLoader):
    directory: str
    strict: bool = False
    name: str = "markdown"

    def enabled(self) -> bool:
        return Path(self.directory).is_dir()

    def load(self) -> Iterator[Document]:
        root = Path(self.directory)
        if not root.is_dir():
            raise LoaderNotConfigured(f"knowledge directory not found: {root}")

        for path in sorted(root.rglob("*")):
            if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            rel = path.relative_to(root)
            if any(part.startswith(("_", ".")) for part in rel.parts):
                continue
            if path.stem.lower() in EXCLUDED_NAMES:
                continue
            try:
                raw = path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError) as exc:
                log.warning(
                    "skipping unreadable knowledge file",
                    extra={"context": {"path": str(rel), "error": str(exc)}},
                )
                continue

            defaults = {"product": _product_from_path(rel)}
            try:
                yield build_document(
                    raw=raw,
                    source=f"markdown:{rel.as_posix()}",
                    defaults=defaults,
                    strict=self.strict,
                )
            except DocumentError as exc:
                if self.strict:
                    raise
                log.warning(
                    "skipping invalid knowledge document",
                    extra={"context": {"path": str(rel), "error": str(exc)}},
                )


def _product_from_path(rel: Path) -> str:
    for part in rel.parts[:-1]:
        product = normalize_product(part.replace("-", " ").replace("_", " "))
        if product != "general":
            return product
    return "general"
