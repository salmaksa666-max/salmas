# -*- coding: utf-8 -*-
# Hand-reasoned answers for the 115 questions the source left without an answer.
import json
from fix115_data import FIX

_memo = json.load(open("abosarah2026/data/memorize.json", encoding="utf-8"))
_hl = json.load(open("abosarah2026/data/parsed_questions.json", encoding="utf-8"))
_stems = {q["qno"]: q for q in _hl}

NOTE = "ما فيه جواب من المصدر لهذا السؤال؛ الجواب هنا اجتهاد طبي مبني على ملخص الموضوع بالمصدر نفسه."

EXPLANATIONS = {}
WHY_WRONG = {}
HIGHLIGHT_TERMS = {}

for qno, (letter, idea, why, when, rule, wrong) in FIX.items():
    m = _memo.get(qno, {})
    terms = (m.get("level2", []) + m.get("level1", []))[:3]
    stem = _stems[qno]["stem"] or ""
    terms = [t for t in terms if t and t in stem] or [stem.split()[0]]
    EXPLANATIONS[qno] = {
        "correct_letter": letter,
        "self_judged": True,
        "idea": idea,
        "clues": [(t, "دليل مهم بالسؤال") for t in terms],
        "why_correct": [why],
        "when_changes": [when],
        "rule": rule,
        "comparison": None,
        "labs": None,
        "guideline_note": NOTE,
    }
    WHY_WRONG[qno] = wrong
    HIGHLIGHT_TERMS[qno] = terms
