# -*- coding: utf-8 -*-
import json

_parsed = {q["qno"]: q for q in json.load(open("abosarah2026/data/parsed_questions.json", encoding="utf-8"))}
_exp = json.load(open("abosarah2026/data/explanations.json", encoding="utf-8"))


def b(t):
    return f"<bdi>{t}</bdi>"


def build(R):
    E, W, H = {}, {}, {}
    for qno, r in R.items():
        old = _exp[qno]
        assert r["ans"] == old["correct_letter"], f"{qno}: answer changed"
        E[qno] = {
            "correct_letter": r["ans"],
            "self_judged": old["self_judged"],
            "idea": r["idea"],
            "clues": r["clues"],
            "why_correct": r["why"],
            "when_changes": [r["when"]],
            "rule": r["rule"],
            "comparison": None,
            "labs": old.get("labs"),
            "guideline_note": old.get("guideline_note"),
        }
        W[qno] = r["wrong"]
        H[qno] = [t for t, _ in r["clues"]]
    return E, W, H
