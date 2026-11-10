"""Language detection, Arabic normalisation, question and acknowledgement detection."""

from __future__ import annotations

import pytest

from zam_agent.language import (
    detect_language,
    is_acknowledgement_only,
    is_saudi_dialect,
    looks_like_question,
    normalize_arabic,
    normalize_for_search,
    profile,
    reply_language,
    tokenize,
)


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("How long does app review take?", "en"),
        ("كم مدة مراجعة التطبيق؟", "ar"),
        ("وش سياسة الاسترجاع في Theme Market؟", "mixed"),
        ("", "unknown"),
        ("🙂🙂", "unknown"),
    ],
)
def test_detect_language(text: str, expected: str) -> None:
    assert detect_language(text) == expected


def test_reply_language_follows_dominant_script_for_mixed() -> None:
    assert reply_language("وش مدة مراجعة التطبيق في ZAM؟") == "ar"
    assert reply_language("What is the نسبة for ZAM apps and partners?") == "en"


def test_normalize_arabic_folds_orthographic_variants() -> None:
    assert normalize_arabic("أحمد إبراهيم آية") == "احمد ابراهيم ايه"
    # Tashkeel is removed and taa marbuta folds to haa, so written variants match.
    assert normalize_arabic("مُراجَعَة") == "مراجعه"
    assert normalize_arabic("مــراجعة") == "مراجعه"
    assert normalize_arabic("٢٠٢٦") == "2026"


def test_normalize_for_search_strips_arabic_punctuation() -> None:
    assert normalize_for_search("ليش، ما يظهر تطبيقي؟ «مهم»") == "ليش ما يظهر تطبيقي مهم"


def test_tokenize_folds_alef_and_taa_marbuta_so_variants_match() -> None:
    assert tokenize("سياسة الإسترجاع") == tokenize("سياسه الاسترجاع")


@pytest.mark.parametrize(
    "text",
    [
        "How long does ZAM app review take?",
        "كم مدة مراجعة التطبيق؟",
        "وش نسبة زام",
        "ليش ما يظهر تطبيقي",
        "Can someone confirm the refund window",
        "عندي استفسار بخصوص القوالب",
        "Is there a sandbox store for partners",
        "أبغى أعرف باقات القوالب",
    ],
)
def test_looks_like_question_true(text: str) -> None:
    assert looks_like_question(text) is True


@pytest.mark.parametrize(
    "text",
    [
        "thanks!",
        "شكراً",
        "يعطيك العافية",
        "Deploying the new build now",
        "",
    ],
)
def test_looks_like_question_false(text: str) -> None:
    assert looks_like_question(text) is False


@pytest.mark.parametrize("text", ["thanks", "شكرا", "تسلم", "مشكورين", "got it", "+1", "تمام"])
def test_acknowledgement_only(text: str) -> None:
    assert is_acknowledgement_only(text) is True


def test_long_message_is_not_an_acknowledgement() -> None:
    assert is_acknowledgement_only("thanks, but how long does the review actually take?") is False


@pytest.mark.parametrize("text", ["وش الفرق بينهم", "ليش كذا", "أبغى أعرف", "ودي أفهم الموضوع"])
def test_saudi_dialect_detected(text: str) -> None:
    assert is_saudi_dialect(text) is True


def test_msa_is_not_flagged_as_dialect() -> None:
    assert is_saudi_dialect("ما هي مدة مراجعة التطبيق؟") is False


def test_profile_bundles_everything() -> None:
    result = profile("وش مدة مراجعة التطبيق في زام؟")
    assert result.detected == "ar"
    assert result.reply_in == "ar"
    assert result.saudi_dialect is True
    assert result.is_question is True
    assert result.is_acknowledgement is False
