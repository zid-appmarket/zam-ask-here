"""Loader contract shared by every knowledge source."""

from __future__ import annotations

from collections.abc import Iterable
from typing import Protocol

from ..documents import Document


class LoaderError(RuntimeError):
    """A loader was configured but failed to fetch."""


class LoaderNotConfigured(LoaderError):
    """A loader has no credentials/targets, so it is skipped (not an error)."""


class KnowledgeLoader(Protocol):
    name: str

    def enabled(self) -> bool: ...

    def load(self) -> Iterable[Document]: ...
