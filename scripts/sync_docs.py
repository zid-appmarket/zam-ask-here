#!/usr/bin/env python3
"""Sync Zid's public documentation into `knowledge/` as reviewable Markdown.

    python scripts/sync_docs.py --list                  # what is configured
    python scripts/sync_docs.py --dry-run               # what would change
    python scripts/sync_docs.py --source partner-help   # one source
    python scripts/sync_docs.py --url <page>            # one page, to eyeball
    python scripts/sync_docs.py                         # write everything

Synced files are overwritten on every run, so never hand-edit one: fix the
upstream page and re-sync. Review the diff before committing, then run
`python scripts/ingest.py --validate`.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from dotenv import load_dotenv  # noqa: E402

from zam_agent.config import ConfigError, load_config  # noqa: E402
from zam_agent.knowledge.websync import (  # noqa: E402
    FetchError,
    SyncReport,
    WebSource,
    _strip_elements,
    extract_title,
    extract_updated,
    fetch,
    html_to_markdown,
    load_sources,
    pick_main_region,
    sitemap_urls,
    sync_source,
)
from zam_agent.observability.logging import configure_logging  # noqa: E402

DEFAULT_SOURCES = "knowledge/sources.yaml"


def _print_report(report: SyncReport, *, verbose: bool) -> None:
    print(
        f"\n[{report.source}] discovered={report.discovered} selected={report.selected} "
        f"written={report.written} unchanged={report.unchanged} "
        f"skipped={report.skipped} failed={report.failed}"
    )
    for page in report.pages:
        if page.status == "written" and verbose:
            print(f"  + {page.path}  ({page.chars} chars)")
        elif page.status == "skipped":
            print(f"  ~ skipped {page.url}  ({page.reason})")
        elif page.status == "failed":
            print(f"  ! failed  {page.url}  ({page.reason})", file=sys.stderr)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--sources", default=DEFAULT_SOURCES, help=f"config file (default {DEFAULT_SOURCES})")
    parser.add_argument("--source", action="append", help="sync only this source (repeatable)")
    parser.add_argument("--url", action="append", help="sync only these URLs, against their source")
    parser.add_argument("--list", action="store_true", help="show configured sources and page counts")
    parser.add_argument("--dry-run", action="store_true", help="fetch and report, write nothing")
    parser.add_argument("--limit", type=int, help="cap pages per source (overrides the config)")
    parser.add_argument("--delay", type=float, default=0.25, help="seconds between requests (default 0.25)")
    parser.add_argument("--preview", action="store_true", help="with --url, print the extracted body")
    parser.add_argument("--quiet", action="store_true", help="only print the per-source summary")
    args = parser.parse_args(argv)

    load_dotenv(override=False)
    configure_logging("WARNING", "text")
    try:
        config = load_config(require_secrets=False)
    except ConfigError as exc:
        print(f"configuration error: {exc}", file=sys.stderr)
        return 2

    sources_path = Path(args.sources)
    if not sources_path.exists():
        print(f"no source config at {sources_path}", file=sys.stderr)
        return 2
    sources: list[WebSource] = load_sources(sources_path)
    if args.source:
        wanted = set(args.source)
        sources = [s for s in sources if s.name in wanted]
        if not sources:
            print(f"no source named {', '.join(sorted(wanted))}", file=sys.stderr)
            return 2
    if args.limit:
        for source in sources:
            source.limit = args.limit

    knowledge_dir = config.knowledge.directory

    # --preview: extract one page and print it, so a selector problem is
    # obvious before writing hundreds of files.
    if args.url and args.preview:
        for url in args.url:
            try:
                markup = fetch(url)
            except FetchError as exc:
                print(f"! {url}: {exc}", file=sys.stderr)
                continue
            body = html_to_markdown(pick_main_region(_strip_elements(markup)))
            print("=" * 78)
            print(f"{url}\ntitle   : {extract_title(markup, '?')}")
            print(f"updated : {extract_updated(markup) or '(not stated)'}\nchars   : {len(body)}")
            print("-" * 78)
            print(body)
        return 0

    if args.list:
        for source in sources:
            try:
                urls = sitemap_urls(source.sitemap)
            except FetchError as exc:
                print(f"{source.name:<16} sitemap unreachable: {exc}", file=sys.stderr)
                continue
            wanted_urls = [u for u in urls if source.wants(u)]
            print(
                f"{source.name:<16} {len(wanted_urls):>4} of {len(urls):>4} pages  "
                f"-> {knowledge_dir}/{source.directory}/  "
                f"product={source.default_product} status={source.status} lang={source.language}"
            )
        return 0

    today = _dt.date.today()
    totals = {"written": 0, "unchanged": 0, "skipped": 0, "failed": 0}
    for source in sources:
        try:
            report = sync_source(
                source,
                knowledge_dir=knowledge_dir,
                today=today,
                dry_run=args.dry_run,
                delay=args.delay,
                only=args.url,
            )
        except FetchError as exc:
            print(f"[{source.name}] sitemap unreachable: {exc}", file=sys.stderr)
            totals["failed"] += 1
            continue
        _print_report(report, verbose=not args.quiet)
        for key in totals:
            totals[key] += getattr(report, key)

    verb = "would write" if args.dry_run else "wrote"
    print(
        f"\n{verb} {totals['written']} document(s); {totals['unchanged']} unchanged, "
        f"{totals['skipped']} skipped, {totals['failed']} failed"
    )
    if totals["written"] and not args.dry_run:
        print("\nNext: review the diff, then\n  python scripts/ingest.py --validate")
    return 1 if totals["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
