#!/usr/bin/env python3
"""Run a message through the full pipeline without Slack.

    python scripts/simulate.py "وش مدة مراجعة التطبيق؟"
    python scripts/simulate.py --file questions.txt
    python scripts/simulate.py "…" --thread "[employee:U1] earlier question"

Needs ANTHROPIC_API_KEY (it really calls Claude) but no Slack credentials, and
posts nothing anywhere. This is the quickest way to see whether a knowledge
change moves the agent from "escalate" to "answer".
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
from zam_agent.llm.anthropic_client import AnthropicLLM  # noqa: E402
from zam_agent.observability.logging import configure_logging  # noqa: E402
from zam_agent.pipeline import IncomingMessage, SupportPipeline  # noqa: E402
from zam_agent.store.sqlite_store import SQLiteStore  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("question", nargs="?", help="the message to simulate")
    parser.add_argument("--file", help="a file with one message per line")
    parser.add_argument("--thread", default="", help="rendered prior thread messages")
    parser.add_argument("--channel", default="C00000000000", help="channel id to simulate")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    questions: list[str] = []
    if args.question:
        questions.append(args.question)
    if args.file:
        questions.extend(
            line.strip() for line in Path(args.file).read_text(encoding="utf-8").splitlines() if line.strip()
        )
    if not questions:
        parser.error("give a question or --file")

    load_dotenv(override=False)
    configure_logging("WARNING" if args.json else "INFO", "text")
    try:
        config = load_config(require_secrets=False)
    except ConfigError as exc:
        print(f"configuration error: {exc}", file=sys.stderr)
        return 2
    if not config.llm.api_key:
        print("ANTHROPIC_API_KEY is required to simulate (the pipeline calls Claude)", file=sys.stderr)
        return 2

    knowledge = KnowledgeBase(config.knowledge)
    report = knowledge.reload()
    if not args.json:
        print(f"knowledge: {report.documents} document(s), {report.chunks} chunk(s)\n")

    # Simulation must never touch the production de-duplication table.
    store = SQLiteStore("sqlite://:memory:")
    pipeline = SupportPipeline(
        config=config, knowledge=knowledge, llm=AnthropicLLM(config.llm), store=store
    )

    results = []
    for idx, question in enumerate(questions):
        decision = pipeline.handle(
            IncomingMessage(
                channel_id=args.channel,
                user_id="U00000000000",
                text=question,
                message_ts=f"{1000 + idx}.000000",
                event_key=f"sim-{idx}",
                thread_ts=None,
                is_thread_reply=bool(args.thread),
                thread_context=args.thread,
            )
        )
        payload = {
            "question": question,
            "action": decision.action.value,
            "category": decision.category,
            "product": decision.product,
            "language": decision.language,
            "confidence_level": decision.confidence_level,
            "confidence_score": decision.confidence_score,
            "skip_reason": decision.skip_reason,
            "tagged_owner": decision.tagged_owner,
            "owner_user_id": decision.owner_user_id,
            "sources": [ref.label for ref in decision.sources],
            "reply": decision.text,
            "reasons": list(decision.verdict.reasons) if decision.verdict else [],
            "components": dict(decision.verdict.components) if decision.verdict else {},
            "diagnostics": dict(decision.diagnostics),
        }
        results.append(payload)
        if args.json:
            continue
        print("=" * 78)
        print(f"Q: {question}")
        print(f"→ action={payload['action']} category={payload['category']} "
              f"confidence={payload['confidence_level']} ({payload['confidence_score']:.2f})")
        if payload["skip_reason"]:
            print(f"   skipped: {payload['skip_reason']}")
        if payload["components"]:
            print("   components: " + ", ".join(f"{k}={v}" for k, v in payload["components"].items()))
        if payload["reasons"]:
            for reason in payload["reasons"][:5]:
                print(f"   · {reason}")
        if payload["reply"]:
            print("\n" + payload["reply"] + "\n")

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
