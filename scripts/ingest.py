#!/usr/bin/env python3
"""Build, validate and inspect the knowledge index.

    python scripts/ingest.py                      # build + write a snapshot
    python scripts/ingest.py --validate           # fail on any bad document
    python scripts/ingest.py --list               # every indexed document
    python scripts/ingest.py --query "…"          # what would be retrieved
    python scripts/ingest.py --stale              # documents past the age limit

Run ``--validate`` in CI on every change to `knowledge/`.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from dotenv import load_dotenv  # noqa: E402

from zam_agent.config import ConfigError, load_config  # noqa: E402
from zam_agent.knowledge.ingest import KnowledgeBase  # noqa: E402
from zam_agent.observability.logging import configure_logging  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--validate", action="store_true", help="exit non-zero on any invalid document")
    parser.add_argument("--list", action="store_true", help="list indexed documents")
    parser.add_argument("--stale", action="store_true", help="list stale documents")
    parser.add_argument("--query", help="show what this question would retrieve")
    parser.add_argument("--product", choices=["zam", "theme_market", "general"], help="scope --query")
    parser.add_argument("--restricted", action="store_true", help="include restricted documents in --query")
    parser.add_argument("--snapshot", action="store_true", help="write the audit snapshot (default)")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    args = parser.parse_args(argv)

    load_dotenv(override=False)
    configure_logging("WARNING" if args.json else "INFO", "text")

    try:
        config = load_config(require_secrets=False)
    except ConfigError as exc:
        print(f"configuration error: {exc}", file=sys.stderr)
        return 2

    kb = KnowledgeBase(config.knowledge, strict=args.validate)
    try:
        report = kb.reload()
    except Exception as exc:  # noqa: BLE001 - --validate wants the message, not a traceback
        print(f"ingestion failed: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(report.to_dict(), indent=2, ensure_ascii=False))
    else:
        print(f"documents : {report.documents}")
        print(f"chunks    : {report.chunks}")
        print(f"duration  : {report.duration_seconds:.2f}s")
        print(f"by product: {report.by_product or '{}'}")
        print(f"by status : {report.by_status or '{}'}")
        for name, reason in report.skipped_loaders.items():
            print(f"skipped   : {name} ({reason})")
        for failure in report.errors:
            print(f"ERROR     : {failure}", file=sys.stderr)
        if report.duplicate_doc_ids:
            print(f"DUPLICATE ids (first kept): {', '.join(sorted(set(report.duplicate_doc_ids)))}", file=sys.stderr)
        if report.stale_documents:
            print(f"stale     : {len(report.stale_documents)} document(s) past KNOWLEDGE_MAX_AGE_DAYS")

    if args.list:
        print("\n-- indexed documents --")
        for doc in sorted(kb.index.documents, key=lambda d: (d.product, d.doc_id)):
            updated = doc.updated.isoformat() if doc.updated else "no-date"
            print(f"{doc.doc_id:<34} {doc.product:<13} {doc.status:<10} {updated:<11} {doc.title}")

    if args.stale:
        print("\n-- stale documents --")
        stale = set(report.stale_documents)
        for doc in kb.index.documents:
            if doc.doc_id in stale:
                print(f"{doc.doc_id:<34} updated={doc.updated or 'never'} owner={doc.owner or '-'}")
        if not stale:
            print("(none)")

    if args.query:
        result = kb.retrieve(args.query, product=args.product, allow_restricted=args.restricted)
        print(f"\n-- retrieval for {args.query!r} --")
        print(f"coverage      : {result.coverage:.0%}")
        print(f"query terms   : {', '.join(result.query_terms) or '(none)'}")
        print(f"matched terms : {', '.join(result.matched_terms) or '(none)'}")
        if result.conflicts:
            print(f"conflicts     : {'; '.join(result.conflicts)}")
        if result.excluded_restricted:
            print(f"withheld      : {result.excluded_restricted} restricted chunk(s)")
        if not result.evidence:
            print("no matching source — the agent would escalate this question")
        for item in result.evidence:
            snippet = " ".join(item.chunk.text.split())[:160]
            print(f"\n[{item.label}] score={item.score:.3f} status={item.document.status}")
            print(f"  {item.chunk.display_source}")
            print(f"  {snippet}…")

    if args.snapshot or not (args.list or args.query or args.stale or args.validate):
        path = kb.write_snapshot()
        if not args.json:
            print(f"\nsnapshot written to {path}")

    if args.validate and (report.errors or report.duplicate_doc_ids):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
