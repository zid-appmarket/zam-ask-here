"""Sync public documentation sites into ``knowledge/`` as reviewable Markdown.

**Why files in git rather than a runtime crawl.** The agent could fetch these
sites at boot, but then nobody reviews what it is allowed to say, a site outage
becomes an agent outage, and a silent upstream edit silently changes answers.
Writing documents into the repository keeps the usual gate: a sync produces a
diff, somebody reads it, CI validates it. Re-running the sync later shows
exactly what upstream changed.

Nothing here runs inside the agent. It is a tool for maintainers:
``scripts/sync_docs.py``.

The extractor is deliberately dependency-free and generic -- it prefers
``<article>``/``<main>``, then a content-looking container, then the densest
block -- rather than per-site CSS selectors, which break on the next redeploy.
Fetched HTML is untrusted input: it is converted to text, never executed, and
the resulting documents are reviewed before they can be cited.
"""

from __future__ import annotations

import datetime as _dt
import gzip
import hashlib
import html as _html
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from ..language import detect_language
from ..observability.logging import get_logger
from .documents import normalize_product

log = get_logger(__name__)

USER_AGENT = "zam-ask-here-docs-sync (+internal support agent knowledge sync)"
REQUEST_TIMEOUT = 30.0

# ------------------------------------------------------------------ HTML -> text

_DROP_ELEMENTS = (
    "script", "style", "noscript", "svg", "iframe", "template", "nav", "header",
    "footer", "aside", "form", "button", "select", "option", "label", "picture",
    "video", "audio", "canvas", "dialog",
)
_CONTENT_HINT = re.compile(r"markdown|article|content|prose|docs?-body|post-body|entry", re.I)

_BOILERPLATE = (
    "skip to main content",
    "did this answer your question",
    "copy page",
    "all collections",
    "search for articles",
    "table of contents",
    "on this page",
    "was this helpful",
    "powered by intercom",
    "ask ai",
    "جديد مركز المساعدة",
    "هل أجاب هذا على سؤالك",
    "الانتقال إلى لوحة التحكم",
    "تواصل معنا",
)


def _strip_elements(markup: str) -> str:
    for tag in _DROP_ELEMENTS:
        markup = re.sub(rf"(?is)<{tag}\b[^>]*>.*?</{tag}\s*>", " ", markup)
        markup = re.sub(rf"(?is)<{tag}\b[^>]*/?>", " ", markup)
    return re.sub(r"(?s)<!--.*?-->", " ", markup)


def _text_length(markup: str) -> int:
    return len(re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", markup)).strip())


def _balanced_blocks(markup: str, tag: str) -> list[str]:
    """Every ``<tag>…</tag>`` region, nesting handled by depth counting."""

    out: list[str] = []
    token = re.compile(rf"(?is)<({tag})\b[^>]*>|</({tag})\s*>")
    depth = 0
    start = 0
    for match in token.finditer(markup):
        if match.group(1):
            if depth == 0:
                start = match.start()
            depth += 1
        elif depth:
            depth -= 1
            if depth == 0:
                out.append(markup[start : match.end()])
    return out


def _link_density(markup: str) -> float:
    """Share of the text that sits inside links. Navigation approaches 1.0."""

    total = _text_length(markup)
    if not total:
        return 1.0
    linked = sum(_text_length(block) for block in _balanced_blocks(markup, "a"))
    return min(linked / total, 1.0)


def _content_score(markup: str) -> float:
    """Prose beats navigation.

    Text length alone picks the outermost wrapper, which on a documentation
    site means the whole sidebar. Discounting by link density picks the region
    a human would call the article.
    """

    return _text_length(markup) * (1.0 - min(_link_density(markup), 0.95))


def _trim_to_heading(markup: str) -> str:
    """Drop anything before the page's ``<h1>``, which is where chrome lives."""

    match = re.search(r"(?is)<h1\b", markup)
    if not match:
        return markup
    trimmed = markup[match.start() :]
    # Only if the heading is not the last thing on the page.
    return trimmed if _text_length(trimmed) >= 150 else markup


def pick_main_region(markup: str) -> str:
    """The part of the page that is actually the document."""

    for tag in ("article", "main"):
        blocks = _balanced_blocks(markup, tag)
        if blocks:
            best = max(blocks, key=_content_score)
            if _text_length(best) >= 200:
                return _trim_to_heading(best)

    # A container whose class or id looks like content.
    candidates: list[str] = []
    for block in _balanced_blocks(markup, "div") + _balanced_blocks(markup, "section"):
        opening = re.match(r"(?is)<\w+\b[^>]*>", block)
        if opening and _CONTENT_HINT.search(opening.group(0)):
            candidates.append(block)
    if candidates:
        best = max(candidates, key=_content_score)
        if _text_length(best) >= 200:
            return _trim_to_heading(best)

    body = _balanced_blocks(markup, "body")
    return _trim_to_heading(body[0] if body else markup)


_BLOCK_BREAK = re.compile(
    r"(?is)</(p|div|section|li|tr|h[1-6]|pre|blockquote|table|ul|ol|dl|dd|dt)\s*>|<br\s*/?>"
)


def html_to_markdown(markup: str) -> str:
    """A small, predictable HTML-to-Markdown conversion.

    Not a full converter: it keeps headings, paragraphs, lists, code and link
    targets, which is everything the retrieval and grounding layers use.
    """

    text = markup
    text = re.sub(
        r"(?is)<h([1-6])\b[^>]*>(.*?)</h\1\s*>",
        lambda m: f"\n\n{'#' * int(m.group(1))} {m.group(2)}\n\n",
        text,
    )
    text = re.sub(r"(?is)<li\b[^>]*>", "\n- ", text)
    text = re.sub(r"(?is)<(strong|b)\b[^>]*>(.*?)</\1\s*>", r"**\2**", text)
    text = re.sub(r"(?is)<(code|kbd|samp)\b[^>]*>(.*?)</\1\s*>", r"`\2`", text)
    text = re.sub(r"(?is)<pre\b[^>]*>(.*?)</pre\s*>", lambda m: f"\n\n```\n{m.group(1)}\n```\n\n", text)
    # Keep the destination of an external link; it is often the real answer.
    text = re.sub(
        r"(?is)<a\b[^>]*href=\"(https?://[^\"]+)\"[^>]*>(.*?)</a\s*>",
        lambda m: f"{m.group(2)} ({m.group(1)})" if m.group(2).strip() else m.group(1),
        text,
    )
    text = _BLOCK_BREAK.sub("\n\n", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    text = _html.unescape(text)

    lines: list[str] = []
    for raw_line in text.splitlines():
        line = re.sub(r"[ \t ]+", " ", raw_line).strip()
        if not line:
            lines.append("")
            continue
        lowered = line.lower()
        if any(marker in lowered for marker in _BOILERPLATE):
            continue
        if line in {"-", "- ", "#", "|"}:
            continue
        lines.append(line)

    out = "\n".join(lines)
    out = re.sub(r"\n{3,}", "\n\n", out)
    out = re.sub(r"(?m)^-\s*$", "", out)
    return out.strip()


def extract_title(markup: str, fallback: str) -> str:
    heading = re.search(r"(?is)<h1\b[^>]*>(.*?)</h1\s*>", markup)
    if heading:
        title = _html.unescape(re.sub(r"(?s)<[^>]+>", " ", heading.group(1)))
        title = re.sub(r"\s+", " ", title).strip()
        if title:
            return title
    tag = re.search(r"(?is)<title\b[^>]*>(.*?)</title\s*>", markup)
    if tag:
        title = _html.unescape(re.sub(r"\s+", " ", tag.group(1))).strip()
        # Help centres append " | Site name" to every title.
        title = re.split(r"\s+[|–-]\s+", title)[0].strip()
        if title:
            return title
    return fallback


def extract_description(markup: str) -> str:
    for pattern in (
        r"(?is)<meta\b[^>]*name=\"description\"[^>]*content=\"([^\"]{10,400})\"",
        r"(?is)<meta\b[^>]*property=\"og:description\"[^>]*content=\"([^\"]{10,400})\"",
    ):
        match = re.search(pattern, markup)
        if match:
            return re.sub(r"\s+", " ", _html.unescape(match.group(1))).strip()
    return ""


def extract_updated(markup: str) -> _dt.date | None:
    """A published/updated date, if the page states one in metadata."""

    for pattern in (
        r"(?is)<meta\b[^>]*property=\"article:modified_time\"[^>]*content=\"([^\"]+)\"",
        r"(?is)<meta\b[^>]*property=\"article:published_time\"[^>]*content=\"([^\"]+)\"",
        r"(?is)<time\b[^>]*datetime=\"([^\"]+)\"",
        r"\"dateModified\"\s*:\s*\"([^\"]+)\"",
        r"\"datePublished\"\s*:\s*\"([^\"]+)\"",
    ):
        match = re.search(pattern, markup)
        if not match:
            continue
        value = match.group(1).strip()
        try:
            return _dt.datetime.fromisoformat(value.replace("Z", "+00:00")).date()
        except ValueError:
            try:
                return _dt.datetime.strptime(value[:10], "%Y-%m-%d").date()
            except ValueError:
                continue
    return None


# ----------------------------------------------------------------- fetching

class FetchError(RuntimeError):
    pass


def encode_url(url: str) -> str:
    """Make a URL safe to put on the wire.

    Sitemaps carry raw UTF-8 in paths (Arabic article slugs, for instance) and
    ``http.client`` encodes the request line as ASCII, so an unencoded URL
    raises ``UnicodeEncodeError`` instead of fetching. ``%`` is kept safe so an
    already-encoded URL is not encoded twice.
    """

    parsed = urllib.parse.urlsplit(url)
    netloc = parsed.netloc
    if not netloc.isascii():
        netloc = netloc.encode("idna").decode("ascii")
    return urllib.parse.urlunsplit(
        (
            parsed.scheme,
            netloc,
            urllib.parse.quote(parsed.path, safe="/%:@&=+$,~!*'()"),
            urllib.parse.quote(parsed.query, safe="/%:@&=+$,~!*'()?"),
            "",  # a fragment is never sent
        )
    )


def fetch(url: str, *, timeout: float = REQUEST_TIMEOUT, opener: Any = None) -> str:
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme not in ("http", "https"):
        raise FetchError(f"refusing a non-HTTP URL: {url}")
    request = urllib.request.Request(encode_url(url), method="GET")
    request.add_header("User-Agent", USER_AGENT)
    request.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
    request.add_header("Accept-Encoding", "gzip")
    try:
        # Scheme is validated above; nothing else is accepted.
        with (opener or urllib.request.urlopen)(request, timeout=timeout) as response:  # noqa: S310
            payload = response.read()
            if response.headers.get("Content-Encoding") == "gzip":
                payload = gzip.decompress(payload)
            charset = response.headers.get_content_charset() or "utf-8"
    except urllib.error.HTTPError as exc:
        raise FetchError(f"HTTP {exc.code}") from None
    except urllib.error.URLError as exc:
        raise FetchError(f"unreachable: {exc.reason}") from None
    except OSError as exc:  # pragma: no cover - transport level
        raise FetchError(f"transport error: {type(exc).__name__}") from None
    except UnicodeError as exc:
        raise FetchError(f"could not encode the URL: {exc}") from None
    return payload.decode(charset, "replace")


def sitemap_urls(sitemap_url: str, *, opener: Any = None) -> list[str]:
    """URLs from a sitemap, following one level of sitemap index."""

    body = fetch(sitemap_url, opener=opener)
    locs = [_html.unescape(m.group(1)).strip() for m in re.finditer(r"(?is)<loc>(.*?)</loc>", body)]
    if "<sitemapindex" in body.lower():
        nested: list[str] = []
        for child in locs[:20]:
            try:
                nested.extend(sitemap_urls(child, opener=opener))
            except FetchError as exc:
                log.warning("nested sitemap failed", extra={"context": {"url": child, "error": str(exc)}})
        return list(dict.fromkeys(nested))
    return list(dict.fromkeys(locs))


# ------------------------------------------------------------------- config

@dataclass
class ProductRule:
    pattern: re.Pattern[str]
    product: str

    @classmethod
    def parse(cls, raw: dict[str, Any]) -> ProductRule:
        return cls(pattern=re.compile(raw["match"], re.I), product=normalize_product(raw["product"]))


@dataclass
class WebSource:
    name: str
    sitemap: str
    directory: str
    default_product: str = "general"
    audience: str = "all"
    status: str = "verified"
    language: str = "unknown"
    include: tuple[re.Pattern[str], ...] = ()
    exclude: tuple[re.Pattern[str], ...] = ()
    product_rules: tuple[ProductRule, ...] = ()
    tags: tuple[str, ...] = ()
    id_prefix: str = "doc"
    limit: int | None = None
    min_chars: int = 200

    @classmethod
    def parse(cls, raw: dict[str, Any]) -> WebSource:
        return cls(
            name=str(raw["name"]),
            sitemap=str(raw["sitemap"]),
            directory=str(raw["directory"]),
            default_product=normalize_product(raw.get("product")),
            audience=str(raw.get("audience", "all")),
            status=str(raw.get("status", "verified")),
            language=str(raw.get("language", "unknown")),
            include=tuple(re.compile(p, re.I) for p in raw.get("include", []) or []),
            exclude=tuple(re.compile(p, re.I) for p in raw.get("exclude", []) or []),
            product_rules=tuple(ProductRule.parse(r) for r in raw.get("product_rules", []) or []),
            tags=tuple(str(t) for t in raw.get("tags", []) or []),
            id_prefix=str(raw.get("id_prefix", "doc")),
            limit=int(raw["limit"]) if raw.get("limit") else None,
            min_chars=int(raw.get("min_chars", 200)),
        )

    def wants(self, url: str) -> bool:
        if self.exclude and any(p.search(url) for p in self.exclude):
            return False
        if self.include:
            return any(p.search(url) for p in self.include)
        return True

    def product_for(self, url: str) -> str:
        for rule in self.product_rules:
            if rule.pattern.search(url):
                return rule.product
        return self.default_product


def load_sources(path: str | Path) -> list[WebSource]:
    raw = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    return [WebSource.parse(entry) for entry in raw.get("sources", [])]


# -------------------------------------------------------------------- sync

_SLUG = re.compile(r"[^a-z0-9]+")
# Path segments that say nothing about which page this is.
_NOISE_SEGMENTS = frozenset(
    {"en", "ar", "en-us", "ar-sa", "articles", "article", "collections", "collection", "docs", "help", "kb"}
)


def slug_for(url: str) -> str:
    """A readable file stem.

    Built from the whole path, not just its last segment: a help centre has
    ``/ar/products``, ``/ar/analytics/products`` and ``/ar/marketplaces/products``,
    and using the tail alone would collapse all three into one file.
    """

    path = urllib.parse.unquote(urllib.parse.urlsplit(url).path).strip("/")
    segments = [seg for seg in path.split("/") if seg and seg.lower() not in _NOISE_SEGMENTS]
    if not segments:
        segments = ["index"]
    # Intercom-style slugs carry a numeric id prefix, docs-site slugs a
    # trailing one; neither helps a human find the file.
    segments[-1] = re.sub(r"^\d{5,}-", "", segments[-1])
    segments[-1] = re.sub(r"-\d{5,}[a-z]?\d*$", "", segments[-1])
    slug = _SLUG.sub("-", "-".join(segments).lower()).strip("-")[:70].strip("-")
    return slug or hashlib.sha256(url.encode()).hexdigest()[:10]


def assign_slugs(urls: Sequence[str]) -> dict[str, str]:
    """Map each URL to a unique stem.

    Stripping generated ids makes readable names but can make two pages agree
    (``events-878234m0`` and ``events-1954903m0`` are different pages). Where
    that happens, every member of the colliding group gets a short stable
    suffix, so one page can never silently overwrite another.
    """

    groups: dict[str, list[str]] = {}
    for url in urls:
        groups.setdefault(slug_for(url), []).append(url)

    assigned: dict[str, str] = {}
    for slug, group in groups.items():
        if len(group) == 1:
            assigned[group[0]] = slug
            continue
        for url in sorted(group):
            assigned[url] = f"{slug}-{hashlib.sha256(url.encode()).hexdigest()[:6]}"
    return assigned


@dataclass
class PageResult:
    url: str
    status: str  # written | unchanged | skipped | failed
    path: Path | None = None
    reason: str = ""
    chars: int = 0


@dataclass
class SyncReport:
    source: str = ""
    discovered: int = 0
    selected: int = 0
    written: int = 0
    unchanged: int = 0
    skipped: int = 0
    failed: int = 0
    pages: list[PageResult] = field(default_factory=list)

    def add(self, result: PageResult) -> None:
        self.pages.append(result)
        setattr(self, result.status, getattr(self, result.status) + 1)


def render_document(
    *,
    source: WebSource,
    url: str,
    slug: str | None = None,
    title: str,
    body: str,
    description: str,
    updated: _dt.date,
    language: str,
) -> str:
    tags = ", ".join(sorted({*source.tags, "from-docs-site"}))
    safe_title = title.replace('"', "'")
    header = [
        "---",
        f"# Synced from {url}",
        "# Do not hand-edit: scripts/sync_docs.py overwrites this file.",
        "# Correct the upstream page instead, then re-run the sync.",
        f"id: {source.id_prefix}-{slug or slug_for(url)}",
        f'title: "{safe_title}"',
        f"product: {source.product_for(url)}",
        f"audience: {source.audience}",
        f"status: {source.status}",
        f"updated: {updated.isoformat()}",
        f"source_url: {url}",
        f"tags: [{tags}]",
        f"language: {language}",
        "---",
        "",
    ]
    if description:
        header.extend([f"> {description}", ""])
    return "\n".join(header) + body.rstrip() + "\n"


def sync_source(
    source: WebSource,
    *,
    knowledge_dir: str | Path,
    today: _dt.date | None = None,
    dry_run: bool = False,
    delay: float = 0.3,
    opener: Any = None,
    only: Sequence[str] | None = None,
) -> SyncReport:
    report = SyncReport(source=source.name)
    today = today or _dt.date.today()
    target_dir = Path(knowledge_dir) / source.directory

    urls: list[str] = list(only) if only else sitemap_urls(source.sitemap, opener=opener)
    urls = list(dict.fromkeys(urls))
    report.discovered = len(urls)

    wanted = [url for url in urls if source.wants(url)]
    if source.limit:
        wanted = wanted[: source.limit]
    report.selected = len(wanted)
    slugs = assign_slugs(wanted)

    if not dry_run:
        target_dir.mkdir(parents=True, exist_ok=True)

    for index, url in enumerate(wanted):
        if index and delay:
            time.sleep(delay)
        try:
            markup = fetch(url, opener=opener)
            region = pick_main_region(_strip_elements(markup))
            body = html_to_markdown(region)
        except FetchError as exc:
            report.add(PageResult(url=url, status="failed", reason=str(exc)))
            log.warning("fetch failed", extra={"context": {"url": url, "error": str(exc)}})
            continue
        except Exception as exc:  # noqa: BLE001 - one bad page must not end the run
            report.add(PageResult(url=url, status="failed", reason=f"{type(exc).__name__}: {exc}"))
            log.warning(
                "page could not be processed",
                extra={"context": {"url": url, "error": type(exc).__name__}},
            )
            continue
        if len(body) < source.min_chars:
            report.add(PageResult(url=url, status="skipped", reason=f"only {len(body)} chars of text"))
            continue

        slug = slugs[url]
        title = extract_title(markup, slug.replace("-", " ").title())
        language = source.language
        if language in ("", "unknown", "auto"):
            detected = detect_language(body)
            language = detected if detected != "unknown" else "unknown"

        document = render_document(
            source=source,
            url=url,
            slug=slug,
            title=title,
            body=body,
            description=extract_description(markup),
            updated=extract_updated(markup) or today,
            language=language,
        )
        path = target_dir / f"{slug}.md"

        if path.exists() and _same_content(path, document):
            report.add(PageResult(url=url, status="unchanged", path=path, chars=len(body)))
            continue
        if not dry_run:
            path.write_text(document, encoding="utf-8")
        report.add(PageResult(url=url, status="written", path=path, chars=len(body)))

    return report


def _same_content(path: Path, document: str) -> bool:
    """Ignore the ``updated:`` line so an unchanged page is not re-dated."""

    try:
        existing = path.read_text(encoding="utf-8")
    except OSError:
        return False
    strip = re.compile(r"(?m)^updated:.*$")
    return strip.sub("", existing).strip() == strip.sub("", document).strip()
