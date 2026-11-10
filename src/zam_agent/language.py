"""Language detection, Arabic normalization and question detection.

Supports Modern Standard Arabic, Saudi/Gulf dialect and English. Dialect
detection is only used to hint tone to the model -- the reply language is
decided by script, which is reliable.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from typing import Literal

Language = Literal["ar", "en", "mixed", "unknown"]

_ARABIC_RANGE = re.compile(r"[؀-ۿݐ-ݿࢠ-ࣿﭐ-﷿ﹰ-﻿]")
_LATIN_RANGE = re.compile(r"[A-Za-z]")

# Combining marks: tashkeel, tatweel, Quranic annotation signs.
_TASHKEEL = re.compile(r"[ؐ-ًؚ-ٰٟۖ-ۭـ]")
_NON_WORD = re.compile(r"[^\w؀-ۿ]+", re.UNICODE)
# Arabic punctuation sits inside the Arabic block, so strip it explicitly.
_AR_PUNCT = re.compile('[،؛؞؟٪٫٬٭۔\u06dd«»‐‑‒–—―]')

_ALEF_VARIANTS = str.maketrans({"أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ٲ": "ا", "ٳ": "ا"})
_OTHER_FOLDS = str.maketrans({"ى": "ي", "ئ": "ي", "ة": "ه", "ؤ": "و", "ۀ": "ه", "ک": "ك", "گ": "ك", "ی": "ي"})

# Arabic-Indic and extended Arabic-Indic digits -> ASCII.
_DIGITS = str.maketrans("٠١٢٣٤٥٦٧٨٩۰۱۲۳۴۵۶۷۸۹", "01234567890123456789")

_AR_QUESTION_WORDS = {
    "كيف", "ليش", "لماذا", "وش", "ايش", "إيش", "شنو", "متى", "وين", "اين", "أين",
    "من", "مين", "هل", "كم", "ممكن", "ابغى", "أبغى", "ابغا", "عندي", "استفسار",
    "سؤال", "تقدر", "اقدر", "أقدر", "فيه", "في", "ايه", "وشو", "كيفية", "امتى",
    "يمكن", "محتاج", "احتاج", "أحتاج", "وضحوا", "توضيح", "افهم", "ودي",
}

_EN_QUESTION_WORDS = {
    "how", "why", "what", "when", "where", "who", "which", "whom", "whose",
    "is", "are", "do", "does", "did", "can", "could", "should", "would", "will",
    "any", "anyone", "anybody", "has", "have", "was", "were", "am",
}

_EN_QUESTION_PHRASES = (
    "do we", "can we", "is there", "are there", "how do", "how can", "what is",
    "what's", "anyone know", "does anyone", "need help", "not sure", "any idea",
    "could someone", "can someone", "help me understand", "clarify", "confirm",
)

_AR_QUESTION_PHRASES = (
    "ممكن تفيدوني", "ممكن افهم", "عندي سؤال", "عندي استفسار", "ابغى اعرف",
    "ودي اعرف", "احتاج اعرف", "محتاج اعرف", "ايش الفرق", "وش الفرق", "وش يعني",
    "ليش ما", "كيف اقدر", "كيف يمكن", "متى يتم", "مين يتابع", "وش الحل",
)

# Gulf / Saudi dialect markers -- used only to set tone, never to gate answers.
_SAUDI_MARKERS = {
    "وش", "ايش", "إيش", "ليش", "كذا", "كذه", "ابغى", "أبغى", "ابغا", "تبغى",
    "يبغى", "ودي", "خلاص", "طيب", "يعطيك", "يعطيكم", "مشكور", "مشكورين",
    "الله", "تكفى", "عطني", "اعطني", "شكله", "جالس", "قاعد", "ماعندي",
    "ماعرف", "مره", "مرره", "زين", "مو", "ماكو", "فيه", "باقي", "تمام",
    "يالطيب", "حياك", "بالعافيه", "اشوى", "عاد", "لسا", "لسه",
}

_THANKS_ONLY = {
    "thanks", "thank you", "thx", "ty", "cheers", "noted", "ok", "okay", "k",
    "great", "perfect", "nice", "got it", "understood", "+1", "done",
    "شكرا", "شكراً", "مشكور", "مشكورين", "تسلم", "تسلمون", "يعطيك العافيه",
    "يعطيك العافية", "تمام", "طيب", "اوك", "أوك", "خلاص", "ماشي", "جزاك الله خير",
}


def normalize_arabic(text: str) -> str:
    """Fold Arabic orthographic variation so retrieval matches reliably."""

    text = unicodedata.normalize("NFKC", text)
    text = _TASHKEEL.sub("", text)
    return text.translate(_ALEF_VARIANTS).translate(_OTHER_FOLDS).translate(_DIGITS)


def normalize_for_search(text: str) -> str:
    text = normalize_arabic(text).lower()
    text = _AR_PUNCT.sub(" ", text)
    text = _NON_WORD.sub(" ", text)
    return re.sub(r"\s+", " ", text).strip()


def tokenize(text: str) -> list[str]:
    """Tokens for lexical retrieval; drops 1-char noise but keeps digits."""

    tokens = [tok for tok in normalize_for_search(text).split(" ") if tok]
    return [tok for tok in tokens if len(tok) > 1 or tok.isdigit()]


def detect_language(text: str) -> Language:
    arabic = len(_ARABIC_RANGE.findall(text))
    latin = len(_LATIN_RANGE.findall(text))
    total = arabic + latin
    if total == 0:
        return "unknown"
    ar_ratio = arabic / total
    if ar_ratio >= 0.75:
        return "ar"
    if ar_ratio <= 0.25:
        return "en"
    return "mixed"


def reply_language(text: str) -> Literal["ar", "en"]:
    """The language to answer in. ``mixed`` follows the dominant script."""

    detected = detect_language(text)
    if detected == "ar":
        return "ar"
    if detected == "en":
        return "en"
    arabic = len(_ARABIC_RANGE.findall(text))
    latin = len(_LATIN_RANGE.findall(text))
    return "ar" if arabic >= latin else "en"


def is_saudi_dialect(text: str) -> bool:
    tokens = set(tokenize(text))
    normalized = normalize_for_search(text)
    if tokens & {normalize_for_search(m) for m in _SAUDI_MARKERS}:
        return True
    return any(marker in normalized for marker in ("وش ", "ليش ", "ابغى", "ودي "))


def looks_like_question(text: str) -> bool:
    """True when the message reads as a question or request for information.

    Deliberately generous: a missed question costs a silent bot, while a false
    positive is caught later by the classifier and the relevance gate.
    """

    stripped = text.strip()
    if not stripped:
        return False
    if "؟" in stripped or "?" in stripped:
        return True

    normalized = normalize_for_search(stripped)
    if not normalized:
        return False
    if normalized in {normalize_for_search(t) for t in _THANKS_ONLY}:
        return False

    for phrase in _EN_QUESTION_PHRASES + _AR_QUESTION_PHRASES:
        if normalize_for_search(phrase) in normalized:
            return True

    tokens = normalized.split(" ")
    if not tokens:
        return False
    head = set(tokens[:3])
    if head & {normalize_for_search(w) for w in _AR_QUESTION_WORDS}:
        return True
    return bool(head & _EN_QUESTION_WORDS)


def is_acknowledgement_only(text: str) -> bool:
    """Short pleasantries that must never trigger a reply."""

    normalized = normalize_for_search(text)
    if not normalized:
        return True
    if len(normalized) > 40:
        return False
    folded = {normalize_for_search(t) for t in _THANKS_ONLY}
    words = normalized.split(" ")
    return normalized in folded or (len(words) <= 4 and all(w in folded or len(w) <= 2 for w in words))


@dataclass(frozen=True)
class LanguageProfile:
    detected: Language
    reply_in: Literal["ar", "en"]
    saudi_dialect: bool
    is_question: bool
    is_acknowledgement: bool


def profile(text: str) -> LanguageProfile:
    return LanguageProfile(
        detected=detect_language(text),
        reply_in=reply_language(text),
        saudi_dialect=is_saudi_dialect(text),
        is_question=looks_like_question(text),
        is_acknowledgement=is_acknowledgement_only(text),
    )
