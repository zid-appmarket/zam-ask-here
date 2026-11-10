"""HTML extraction and documentation sync.

These never touch the network: the fetcher's opener is injected.
"""

from __future__ import annotations

import datetime as _dt
import gzip
import io
from typing import Any

import pytest

from zam_agent.knowledge.documents import build_document
from zam_agent.knowledge.websync import (
    FetchError,
    WebSource,
    _link_density,
    _strip_elements,
    extract_description,
    extract_title,
    extract_updated,
    fetch,
    html_to_markdown,
    load_sources,
    pick_main_region,
    render_document,
    sitemap_urls,
    slug_for,
    sync_source,
)

# A page shaped like a real documentation site: heavy nav, then the article.
PAGE = """<!doctype html>
<html><head>
  <title>Publish your app | Zid Partners | Help Center</title>
  <meta name="description" content="How to publish an app to Zid App Market.">
  <meta property="article:modified_time" content="2026-09-15T10:00:00Z">
  <script>var tracking = 1;</script><style>.x{color:red}</style>
</head><body>
  <nav><a href="/a">Overview</a><a href="/b">Start Here</a><a href="/c">Responses</a></nav>
  <div class="sidebar"><a href="/d">Rate Limiting</a><a href="/e">Embedded Apps</a></div>
  <div class="markdown-container">
    <p>Skip to main content</p>
    <h1>Publish your app</h1>
    <p>Review takes <strong>4 business days</strong> from submission.</p>
    <h2>Requirements</h2>
    <ul><li>A development store</li><li>A support channel</li></ul>
    <pre>curl https://api.example.invalid/apps</pre>
    <p>See <a href="https://docs.example.invalid/review">the review guide</a> for detail.</p>
    <p>Did this answer your question?</p>
  </div>
  <footer><a href="/privacy">Privacy</a></footer>
</body></html>"""

SITEMAP = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://help.example.invalid/en/articles/11501759-publish-your-app</loc></url>
  <url><loc>https://help.example.invalid/en/articles/11471817-theme-review</loc></url>
  <url><loc>https://help.example.invalid/en/collections/7129696-index</loc></url>
  <url><loc>https://help.example.invalid/en/articles/11999999-tiny</loc></url>
</urlset>"""

TINY = "<html><head><title>Tiny</title></head><body><main><h1>Tiny</h1><p>x</p></main></body></html>"


class FakeResponse(io.BytesIO):
    def __init__(self, body: str, *, headers: dict[str, str] | None = None, gzipped: bool = False):
        payload = body.encode("utf-8")
        if gzipped:
            payload = gzip.compress(payload)
        super().__init__(payload)
        self._headers = headers or {}

    @property
    def headers(self) -> Any:
        class _H(dict):
            def get_content_charset(self) -> str | None:
                return "utf-8"

        return _H(self._headers)

    def __enter__(self) -> FakeResponse:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()


def make_opener(pages: dict[str, str], *, gzipped: bool = False):
    def opener(request: Any, timeout: float = 0) -> FakeResponse:  # noqa: ARG001
        url = request.full_url if hasattr(request, "full_url") else str(request)
        if url not in pages:
            raise FetchError(f"unexpected URL in test: {url}")
        headers = {"Content-Encoding": "gzip"} if gzipped else {}
        return FakeResponse(pages[url], headers=headers, gzipped=gzipped)

    return opener


# ------------------------------------------------------------------ extraction


def test_navigation_is_not_mistaken_for_content() -> None:
    body = html_to_markdown(pick_main_region(_strip_elements(PAGE)))

    assert "4 business days" in body
    assert "Rate Limiting" not in body, "sidebar leaked into the document"
    assert "Start Here" not in body
    assert "Privacy" not in body


def test_link_density_separates_nav_from_prose() -> None:
    nav = '<div><a href="/a">One</a><a href="/b">Two</a></div>'
    prose = "<div><p>" + ("word " * 60) + '<a href="/a">one link</a></p></div>'
    assert _link_density(nav) > 0.8
    assert _link_density(prose) < 0.2


def test_markdown_conversion_keeps_the_useful_structure() -> None:
    body = html_to_markdown(pick_main_region(_strip_elements(PAGE)))

    assert "# Publish your app" in body
    assert "## Requirements" in body
    assert "- A development store" in body
    assert "**4 business days**" in body
    assert "```" in body and "curl https://api.example.invalid/apps" in body
    # A link's destination is often the real answer, so keep it.
    assert "the review guide (https://docs.example.invalid/review)" in body


def test_boilerplate_lines_are_dropped() -> None:
    body = html_to_markdown(pick_main_region(_strip_elements(PAGE)))
    assert "Skip to main content" not in body
    assert "Did this answer your question" not in body


def test_scripts_and_styles_never_survive() -> None:
    stripped = _strip_elements(PAGE)
    assert "var tracking" not in stripped
    assert "color:red" not in stripped


def test_title_strips_the_site_suffix() -> None:
    assert extract_title(PAGE, "fallback") == "Publish your app"
    no_h1 = "<html><head><title>Payouts | Zid Partners | Help Center</title></head><body><p>x</p></body></html>"
    assert extract_title(no_h1, "fallback") == "Payouts"
    assert extract_title("<html></html>", "fallback") == "fallback"


def test_description_and_date_come_from_metadata() -> None:
    assert extract_description(PAGE) == "How to publish an app to Zid App Market."
    assert extract_updated(PAGE) == _dt.date(2026, 9, 15)
    assert extract_updated("<html><body>no date</body></html>") is None


@pytest.mark.parametrize(
    ("url", "expected"),
    [
        ("https://help.example.invalid/en/articles/11501759-app-payouts", "app-payouts"),
        ("https://docs.example.invalid/rate-limiting-644369m0", "rate-limiting"),
        ("https://docs.example.invalid/submit-app-for-review", "submit-app-for-review"),
        ("https://help.example.invalid/ar/online-store/theme-market", "theme-market"),
    ],
)
def test_slugs_drop_generated_ids(url: str, expected: str) -> None:
    assert slug_for(url) == expected


def test_slugs_keep_path_context() -> None:
    """A help centre repeats the same leaf under several sections."""

    from zam_agent.knowledge.websync import slug_for as s

    assert s("https://help.example.invalid/ar/products") == "products"
    assert s("https://help.example.invalid/ar/analytics/products") == "analytics-products"
    assert s("https://help.example.invalid/ar/marketplaces/products") == "marketplaces-products"


def test_colliding_slugs_are_all_disambiguated() -> None:
    """Two different pages must never resolve to one file."""

    from zam_agent.knowledge.websync import assign_slugs

    urls = [
        "https://docs.example.invalid/events-878234m0",
        "https://docs.example.invalid/events-1954903m0",
        "https://docs.example.invalid/submit-app-for-review",
    ]
    assigned = assign_slugs(urls)

    assert len(set(assigned.values())) == 3
    # The unambiguous one keeps its readable name.
    assert assigned[urls[2]] == "submit-app-for-review"
    # Both sides of a collision are suffixed, so neither silently wins.
    assert assigned[urls[0]] != "events"
    assert assigned[urls[1]] != "events"
    assert assigned[urls[0]].startswith("events-")
    assert assigned[urls[1]].startswith("events-")
    # Stable across runs.
    assert assign_slugs(urls) == assigned


def test_the_shipped_sources_produce_no_colliding_slugs() -> None:
    """Guard the real URL sets, which is where collisions actually appeared."""

    from zam_agent.knowledge.websync import assign_slugs

    # Representative URLs that previously collapsed onto one filename.
    for urls in (
        [
            "https://help.zid.sa/ar/orders",
            "https://help.zid.sa/ar/marketplaces/orders",
            "https://help.zid.sa/ar/customers/wallet",
            "https://help.zid.sa/ar/finance/wallet",
            "https://help.zid.sa/ar/products",
            "https://help.zid.sa/ar/analytics/products",
            "https://help.zid.sa/ar/marketplaces/products",
        ],
        [
            "https://docs.zid.sa/overview-1379323m0",
            "https://docs.zid.sa/overview-1702203m0",
            "https://docs.zid.sa/overview-1340225m0",
        ],
        [
            "https://help-partner.zid.sa/en/articles/8717911-troubleshooting-the-user-credentials-were-incorrect",
            "https://help-partner.zid.sa/en/articles/8717946-troubleshooting-the-user-credentials-were-incorrect",
        ],
    ):
        assigned = assign_slugs(urls)
        assert len(set(assigned.values())) == len(urls), f"collision in {urls}"


def test_a_slug_is_never_empty() -> None:
    assert slug_for("https://example.invalid/") != ""


# -------------------------------------------------------------------- fetching


def test_fetch_decodes_and_gunzips() -> None:
    url = "https://help.example.invalid/x"
    assert "Publish your app" in fetch(url, opener=make_opener({url: PAGE}))
    assert "Publish your app" in fetch(url, opener=make_opener({url: PAGE}, gzipped=True))


def test_a_url_with_arabic_in_the_path_is_encoded_not_crashed() -> None:
    """Sitemaps carry raw UTF-8; the request line has to be ASCII."""

    from zam_agent.knowledge.websync import encode_url

    encoded = encode_url("https://help.example.invalid/en/articles/8718012-لا-يمكن-تغيير")
    assert encoded.isascii()
    assert encoded.startswith("https://help.example.invalid/en/articles/8718012-")
    # Already-encoded URLs must not be encoded a second time.
    assert encode_url(encoded) == encoded
    # Fragments are never sent.
    assert encode_url("https://x.invalid/a#b") == "https://x.invalid/a"


def test_one_unprocessable_page_does_not_end_the_run(tmp_path) -> None:
    def exploding_opener(request: Any, timeout: float = 0) -> FakeResponse:  # noqa: ARG001
        url = request.full_url
        if url.endswith("11471817-theme-review"):
            raise UnicodeEncodeError("ascii", "x", 0, 1, "boom")
        return make_opener(pages())(request, timeout)

    report = sync_source(
        source_for(tmp_path), knowledge_dir=tmp_path, delay=0, opener=exploding_opener
    )

    assert report.written == 1, "the healthy page still got written"
    assert report.failed == 1


def test_fetch_refuses_a_non_http_url() -> None:
    with pytest.raises(FetchError, match="non-HTTP"):
        fetch("file:///etc/passwd")


def test_sitemap_urls_are_deduplicated_and_ordered() -> None:
    url = "https://help.example.invalid/sitemap.xml"
    urls = sitemap_urls(url, opener=make_opener({url: SITEMAP}))
    assert urls[0].endswith("11501759-publish-your-app")
    assert len(urls) == 4


# ------------------------------------------------------------------- the sync


def source_for(tmp_path) -> WebSource:
    return WebSource(
        name="test-help",
        sitemap="https://help.example.invalid/sitemap.xml",
        directory="test-help",
        default_product="zam",
        language="auto",
        include=(__import__("re").compile("/en/articles/"),),
        exclude=(__import__("re").compile("/collections/"),),
        product_rules=(),
        tags=("test-source",),
        id_prefix="ts",
    )


def pages() -> dict[str, str]:
    return {
        "https://help.example.invalid/sitemap.xml": SITEMAP,
        "https://help.example.invalid/en/articles/11501759-publish-your-app": PAGE,
        "https://help.example.invalid/en/articles/11471817-theme-review": PAGE.replace(
            "Publish your app", "Theme review"
        ),
        "https://help.example.invalid/en/articles/11999999-tiny": TINY,
    }


def test_sync_writes_documents_the_loader_can_read(tmp_path) -> None:
    report = sync_source(
        source_for(tmp_path), knowledge_dir=tmp_path, delay=0, opener=make_opener(pages())
    )

    assert report.discovered == 4
    assert report.selected == 3, "the collection index must be excluded"
    assert report.written == 2
    assert report.skipped == 1, "the near-empty page is not worth a document"

    written = sorted((tmp_path / "test-help").glob("*.md"))
    assert [p.name for p in written] == ["publish-your-app.md", "theme-review.md"]

    document = build_document(
        raw=written[0].read_text(encoding="utf-8"), source="markdown:test-help/publish-your-app.md"
    )
    assert document.doc_id == "ts-publish-your-app"
    assert document.title == "Publish your app"
    assert document.product == "zam"
    assert document.status == "verified"
    assert document.updated == _dt.date(2026, 9, 15)
    assert document.source_url.endswith("11501759-publish-your-app")
    assert "partner-help-center" not in document.tags
    assert "test-source" in document.tags
    assert document.language == "en", "language is detected, not declared"
    assert "4 business days" in document.body


def test_re_syncing_an_unchanged_page_rewrites_nothing(tmp_path) -> None:
    opener = make_opener(pages())
    first = sync_source(source_for(tmp_path), knowledge_dir=tmp_path, delay=0, opener=opener)
    second = sync_source(source_for(tmp_path), knowledge_dir=tmp_path, delay=0, opener=opener)

    assert first.written == 2
    assert second.written == 0
    assert second.unchanged == 2


def test_an_upstream_change_is_rewritten(tmp_path) -> None:
    sync_source(source_for(tmp_path), knowledge_dir=tmp_path, delay=0, opener=make_opener(pages()))

    changed = pages()
    changed["https://help.example.invalid/en/articles/11501759-publish-your-app"] = PAGE.replace(
        "4 business days", "6 business days"
    )
    report = sync_source(
        source_for(tmp_path), knowledge_dir=tmp_path, delay=0, opener=make_opener(changed)
    )

    assert report.written == 1
    assert "6 business days" in (tmp_path / "test-help" / "publish-your-app.md").read_text(encoding="utf-8")


def test_dry_run_writes_nothing(tmp_path) -> None:
    report = sync_source(
        source_for(tmp_path), knowledge_dir=tmp_path, delay=0, dry_run=True, opener=make_opener(pages())
    )

    assert report.written == 2
    assert not (tmp_path / "test-help").exists()


def test_a_failed_fetch_is_reported_not_fatal(tmp_path) -> None:
    broken = pages()
    del broken["https://help.example.invalid/en/articles/11471817-theme-review"]

    report = sync_source(
        source_for(tmp_path), knowledge_dir=tmp_path, delay=0, opener=make_opener(broken)
    )

    assert report.written == 1
    assert report.failed == 1


def test_a_synced_document_warns_against_hand_editing(tmp_path) -> None:
    sync_source(source_for(tmp_path), knowledge_dir=tmp_path, delay=0, opener=make_opener(pages()))
    text = (tmp_path / "test-help" / "publish-your-app.md").read_text(encoding="utf-8")
    assert "Do not hand-edit" in text
    assert "Synced from https://help.example.invalid" in text


def test_product_rules_route_by_url() -> None:
    import re as _re

    source = WebSource(
        name="s",
        sitemap="https://x.invalid/sitemap.xml",
        directory="d",
        default_product="zam",
        product_rules=(
            __import__("zam_agent.knowledge.websync", fromlist=["ProductRule"]).ProductRule(
                pattern=_re.compile("theme|vitrin"), product="theme_market"
            ),
        ),
    )
    assert source.product_for("https://x.invalid/publish-your-theme") == "theme_market"
    assert source.product_for("https://x.invalid/app-payouts") == "zam"


def test_a_quote_in_a_title_cannot_break_the_front_matter(tmp_path) -> None:
    source = source_for(tmp_path)
    rendered = render_document(
        source=source,
        url="https://x.invalid/a",
        title='The "best" theme',
        body="# body\n\ntext",
        description="",
        updated=_dt.date(2026, 1, 1),
        language="en",
    )
    document = build_document(raw=rendered, source="markdown:x.md")
    assert document.title == "The 'best' theme"


def test_the_shipped_source_config_is_valid() -> None:
    sources = {s.name: s for s in load_sources("knowledge/sources.yaml")}

    assert {"partner-help", "partner-docs", "merchant-help"} <= set(sources)
    # Every source must produce reviewable, attributable documents.
    for source in sources.values():
        assert source.sitemap.startswith("https://")
        assert source.audience == "all", "public documentation is not restricted"
        assert source.language == "auto"

    # The endpoint reference must stay out: ~400 near-identical stubs would
    # dilute retrieval without answering what this channel asks.
    docs = sources["partner-docs"]
    assert not docs.wants("https://docs.zid.sa/delete-a-product-image-35821474e0")
    assert not docs.wants("https://docs.zid.sa/orders-1934403f0")
    assert docs.wants("https://docs.zid.sa/submit-app-for-review")
    assert docs.wants("https://docs.zid.sa/rate-limiting-644369m0")

    # Collection indexes are link lists, not answers.
    partner = sources["partner-help"]
    assert not partner.wants("https://help-partner.zid.sa/en/collections/7129696-getting-started")
    assert partner.wants("https://help-partner.zid.sa/en/articles/11501759-app-payouts")
    assert partner.product_for("https://help-partner.zid.sa/en/articles/11471817-publish-your-theme") == (
        "theme_market"
    )

    # The merchant help centre has an English mirror of every page; including
    # it would double the corpus for a channel that asks in Arabic.
    merchant = sources["merchant-help"]
    assert merchant.wants("https://help.zid.sa/ar/online-store/theme-market")
    assert not merchant.wants("https://help.zid.sa/en/online-store/theme-market")
    assert not merchant.wants("https://help.zid.sa/ar/topics/orders")
    assert merchant.product_for("https://help.zid.sa/ar/apps/installed-apps") == "zam"
