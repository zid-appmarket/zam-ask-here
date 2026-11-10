"""Load approved Notion pages/databases as knowledge documents.

Only pages explicitly listed in ``NOTION_DATABASE_IDS`` / ``NOTION_PAGE_IDS``
and shared with the integration are read -- the loader never crawls a
workspace. Nothing is sent to Notion other than the read requests themselves.

Property mapping (case-insensitive, falls back to sane defaults):
  Title/Name -> title | Product -> product | Audience -> audience
  Status -> status     | Updated -> updated | Owner -> owner | Tags -> tags
"""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from collections.abc import Iterator
from dataclasses import dataclass, field
from typing import Any

from ...observability.logging import get_logger
from ..documents import Document, build_document
from .base import KnowledgeLoader, LoaderError, LoaderNotConfigured

log = get_logger(__name__)

NOTION_VERSION = "2022-06-28"
API_ROOT = "https://api.notion.com/v1"


@dataclass
class NotionLoader(KnowledgeLoader):
    api_key: str | None
    database_ids: tuple[str, ...] = ()
    page_ids: tuple[str, ...] = ()
    timeout: float = 30.0
    name: str = "notion"
    _opener: Any = field(default=None, repr=False)

    def enabled(self) -> bool:
        return bool(self.api_key) and bool(self.database_ids or self.page_ids)

    def load(self) -> Iterator[Document]:
        if not self.enabled():
            raise LoaderNotConfigured("NOTION_API_KEY plus NOTION_DATABASE_IDS/NOTION_PAGE_IDS required")

        seen: set[str] = set()
        for database_id in self.database_ids:
            for page in self._query_database(database_id):
                page_id = page.get("id", "")
                if page_id and page_id not in seen:
                    seen.add(page_id)
                    doc = self._page_to_document(page)
                    if doc is not None:
                        yield doc
        for page_id in self.page_ids:
            if page_id in seen:
                continue
            seen.add(page_id)
            page = self._request("GET", f"/pages/{page_id}")
            doc = self._page_to_document(page)
            if doc is not None:
                yield doc

    # ------------------------------------------------------------------- HTTP

    def _request(self, method: str, path: str, body: dict[str, Any] | None = None) -> dict[str, Any]:
        url = f"{API_ROOT}{path}"
        if not url.startswith("https://api.notion.com/"):  # defence in depth
            raise LoaderError(f"refusing to fetch a non-Notion URL: {path}")
        data = json.dumps(body).encode("utf-8") if body is not None else None
        request = urllib.request.Request(url, data=data, method=method)  # noqa: S310 - scheme checked above
        request.add_header("Authorization", f"Bearer {self.api_key}")
        request.add_header("Notion-Version", NOTION_VERSION)
        request.add_header("Content-Type", "application/json")
        opener = self._opener or urllib.request.urlopen
        try:
            with opener(request, timeout=self.timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            # Never echo the response body: it can contain page content.
            raise LoaderError(f"Notion API {method} {path} failed with HTTP {exc.code}") from None
        except urllib.error.URLError as exc:
            raise LoaderError(f"Notion API unreachable: {exc.reason}") from None

    def _query_database(self, database_id: str) -> Iterator[dict[str, Any]]:
        cursor: str | None = None
        while True:
            body: dict[str, Any] = {"page_size": 100}
            if cursor:
                body["start_cursor"] = cursor
            payload = self._request("POST", f"/databases/{database_id}/query", body)
            yield from payload.get("results", [])
            if not payload.get("has_more"):
                return
            cursor = payload.get("next_cursor")
            if not cursor:
                return

    def _blocks_markdown(self, block_id: str, depth: int = 0) -> str:
        if depth > 3:
            return ""
        lines: list[str] = []
        cursor: str | None = None
        while True:
            suffix = f"?start_cursor={cursor}&page_size=100" if cursor else "?page_size=100"
            payload = self._request("GET", f"/blocks/{block_id}/children{suffix}")
            for block in payload.get("results", []):
                lines.append(_block_to_markdown(block, depth))
                if block.get("has_children") and block.get("type") not in ("child_page", "child_database"):
                    nested = self._blocks_markdown(block["id"], depth + 1)
                    if nested:
                        lines.append(nested)
            if not payload.get("has_more"):
                break
            cursor = payload.get("next_cursor")
            if not cursor:
                break
        return "\n\n".join(line for line in lines if line.strip())

    # ------------------------------------------------------------- conversion

    def _page_to_document(self, page: dict[str, Any]) -> Document | None:
        page_id = page.get("id", "")
        if not page_id:
            return None
        if page.get("archived") or page.get("in_trash"):
            return None
        props = page.get("properties", {}) or {}
        meta = _properties_to_meta(props)
        body = self._blocks_markdown(page_id)
        if not body.strip():
            log.info("notion page has no readable body", extra={"context": {"page_id": page_id}})
            return None
        meta.setdefault("title", "Untitled Notion page")
        meta.setdefault("id", f"notion-{page_id.replace('-', '')[:12]}")
        meta.setdefault("source_url", page.get("url"))
        meta.setdefault("updated", page.get("last_edited_time"))
        return build_document(raw=body, source=f"notion:{page_id}", defaults=meta)


def _plain_text(rich: list[dict[str, Any]] | None) -> str:
    return "".join(part.get("plain_text", "") for part in (rich or []))


def _block_to_markdown(block: dict[str, Any], depth: int) -> str:
    kind = block.get("type", "")
    data = block.get(kind) or {}
    text = _plain_text(data.get("rich_text"))
    indent = "  " * depth
    match kind:
        case "heading_1":
            return f"# {text}"
        case "heading_2":
            return f"## {text}"
        case "heading_3":
            return f"### {text}"
        case "bulleted_list_item":
            return f"{indent}- {text}"
        case "numbered_list_item":
            return f"{indent}1. {text}"
        case "to_do":
            box = "x" if data.get("checked") else " "
            return f"{indent}- [{box}] {text}"
        case "quote":
            return f"> {text}"
        case "callout":
            return f"> {text}"
        case "toggle":
            return f"**{text}**"
        case "code":
            return f"```{data.get('language', '')}\n{text}\n```"
        case "paragraph":
            return text
        case "divider":
            return "---"
        case "table_row":
            cells = [" ".join(_plain_text(cell) for cell in group) for group in data.get("cells", [])]
            return "| " + " | ".join(cells) + " |" if cells else ""
        case _:
            return text


def _properties_to_meta(props: dict[str, Any]) -> dict[str, Any]:
    meta: dict[str, Any] = {}
    for raw_name, prop in props.items():
        name = raw_name.strip().lower()
        kind = prop.get("type")
        value: Any = None
        if kind == "title":
            value = _plain_text(prop.get("title"))
            name = "title" if name in ("title", "name", "page") else name
        elif kind == "rich_text":
            value = _plain_text(prop.get("rich_text"))
        elif kind == "select":
            value = (prop.get("select") or {}).get("name")
        elif kind == "multi_select":
            value = [item.get("name") for item in prop.get("multi_select") or []]
        elif kind == "status":
            value = (prop.get("status") or {}).get("name")
        elif kind == "date":
            value = (prop.get("date") or {}).get("start")
        elif kind == "last_edited_time":
            value = prop.get("last_edited_time")
        elif kind == "url":
            value = prop.get("url")
        elif kind == "people":
            names = [p.get("name") for p in prop.get("people") or [] if p.get("name")]
            value = ", ".join(names) if names else None
        elif kind == "checkbox":
            value = prop.get("checkbox")
        if value in (None, "", []):
            continue
        if name in ("name", "page"):
            name = "title"
        if name in ("last edited", "last_edited", "last edited time", "updated at"):
            name = "updated"
        if name in ("link", "doc", "document", "source"):
            name = "source_url"
        meta[name] = value
    # A Notion "Status" of anything but Verified must not read as verified.
    status = str(meta.get("status", "")).strip().lower()
    if status:
        meta["status"] = {
            "verified": "verified", "approved": "verified", "published": "verified", "live": "verified",
            "deprecated": "deprecated", "archived": "deprecated", "outdated": "deprecated",
        }.get(status, "draft")
    return meta
