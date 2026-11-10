#!/usr/bin/env python3
"""Report questions the agent could not answer — the knowledge-base backlog.

    python scripts/report_gaps.py                 # most frequent gaps first
    python scripts/report_gaps.py --escalations   # open escalations
    python scripts/report_gaps.py --resolved      # gaps an owner confirmed in Slack
    python scripts/report_gaps.py --draft <key>   # write a reviewable draft document
    python scripts/report_gaps.py --draft-all     # one draft per confirmed gap
    python scripts/report_gaps.py --resolve <key> # mark a gap as covered
    python scripts/report_gaps.py --reopen <key>  # undo a resolution

Each line is a question an employee asked that no approved source answered.
Owners normally close these in Slack by adding the resolve reaction to the
thread; `--draft` then turns the answer they wrote into a document in
`knowledge/_inbox/` for review.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from dotenv import load_dotenv  # noqa: E402

from zam_agent.config import ConfigError, load_config  # noqa: E402
from zam_agent.knowledge.drafts import write_draft  # noqa: E402
from zam_agent.observability.logging import configure_logging  # noqa: E402
from zam_agent.store.sqlite_store import SQLiteStore  # noqa: E402


def _when(ts: float) -> str:
    return _dt.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--limit", type=int, default=30)
    parser.add_argument("--escalations", action="store_true", help="show open escalations instead")
    parser.add_argument("--interactions", action="store_true", help="show the recent decision log")
    parser.add_argument("--include-resolved", action="store_true")
    parser.add_argument("--resolved", action="store_true", help="show gaps an owner confirmed in Slack")
    parser.add_argument("--resolve", metavar="QUESTION_KEY", help="mark a gap as covered")
    parser.add_argument("--reopen", metavar="QUESTION_KEY", help="undo a resolution")
    parser.add_argument(
        "--draft", metavar="QUESTION_KEY", help="write a reviewable draft document for one gap"
    )
    parser.add_argument(
        "--draft-all", action="store_true", help="write a draft for every confirmed gap with an answer"
    )
    parser.add_argument("--prune", type=int, metavar="DAYS", help="delete telemetry older than DAYS")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    load_dotenv(override=False)
    configure_logging("WARNING", "text")
    try:
        config = load_config(require_secrets=False)
    except ConfigError as exc:
        print(f"configuration error: {exc}", file=sys.stderr)
        return 2

    store = SQLiteStore(config.database_url)

    if args.resolve:
        store.resolve_knowledge_gap(args.resolve)
        print(f"marked {args.resolve} as covered")
        return 0

    if args.reopen:
        store.reopen_knowledge_gap(args.reopen)
        print(f"reopened {args.reopen}")
        return 0

    if args.draft or args.draft_all:
        gaps = []
        if args.draft:
            gap = store.knowledge_gap(args.draft)
            if gap is None:
                print(f"no gap recorded with key {args.draft}", file=sys.stderr)
                return 1
            gaps = [gap]
        else:
            gaps = [g for g in store.resolved_knowledge_gaps(limit=args.limit) if g.resolution_note]
            if not gaps:
                print("no confirmed gaps with a captured answer yet")
                return 0
        written = [write_draft(gap, config.knowledge.draft_directory) for gap in gaps]
        for path in written:
            print(f"wrote {path}")
        print(
            f"\n{len(written)} draft(s) in {config.knowledge.draft_directory} — review them, set\n"
            "`status: verified`, then move each into knowledge/<product>/ and run:\n"
            "  python scripts/ingest.py --validate"
        )
        return 0

    if args.resolved:
        rows = store.resolved_knowledge_gaps(limit=args.limit)
        if args.json:
            print(json.dumps([row.__dict__ for row in rows], indent=2, ensure_ascii=False))
            return 0
        if not rows:
            print("no gaps have been confirmed yet")
            return 0
        for row in rows:
            when = _when(row.resolved_at) if row.resolved_at else "unknown"
            print(f"\n{row.question_key}  confirmed {when} by {row.resolved_by or 'unknown'}")
            print(f"  Q: {' '.join(row.question.split())[:100]}")
            if row.resolution_note:
                for line in row.resolution_note.splitlines():
                    if line.strip():
                        print(f"  A: {line.strip()[:100]}")
            else:
                print("  A: (no answer was captured from the thread)")
        print("\nTurn these into documents: python scripts/report_gaps.py --draft-all")
        return 0

    if args.prune:
        removed = store.prune(older_than_days=args.prune)
        print(f"pruned {removed} processed-event row(s) older than {args.prune} days")
        return 0

    if args.escalations:
        rows = store.open_escalations(limit=args.limit)
        if args.json:
            print(json.dumps([row.__dict__ for row in rows], indent=2, ensure_ascii=False))
            return 0
        if not rows:
            print("no open escalations")
            return 0
        print(f"{'opened':<17} {'product':<13} {'owner':<13} question")
        for row in rows:
            print(f"{_when(row.created_at):<17} {(row.product or '-'):<13} {row.owner_user_id:<13} "
                  f"{' '.join(row.question.split())[:70]}")
        return 0

    if args.interactions:
        rows = store.recent_interactions(limit=args.limit)
        if args.json:
            print(json.dumps(rows, indent=2, ensure_ascii=False))
            return 0
        print(f"{'when':<17} {'action':<10} {'conf':<6} {'category':<28} topic")
        for row in rows:
            print(f"{_when(row['created_at']):<17} {row['action']:<10} "
                  f"{row['confidence_score']:<6.2f} {row['category'][:27]:<28} {row['topic'][:40]}")
        return 0

    gaps = store.knowledge_gaps(limit=args.limit, include_resolved=args.include_resolved)
    if args.json:
        print(json.dumps([gap.__dict__ for gap in gaps], indent=2, ensure_ascii=False))
        return 0
    if not gaps:
        print("no knowledge gaps recorded — every question so far was answerable")
        return 0

    print(f"{'asked':<6} {'last seen':<17} {'product':<13} {'key':<34} question")
    for gap in gaps:
        print(f"{gap.occurrences:<6} {_when(gap.last_seen):<17} {(gap.product or '-'):<13} "
              f"{gap.question_key:<34} {' '.join(gap.question.split())[:60]}")
    print(
        "\nAn owner can close any of these in Slack by adding "
        f":{config.slack.resolve_reaction}: to the thread. Then:\n"
        "  python scripts/report_gaps.py --draft-all      # capture their answers as drafts\n"
        "  python scripts/ingest.py --validate --query '<the question>'"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
