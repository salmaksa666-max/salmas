# -*- coding: utf-8 -*-
"""Sixth sweep: generic clinical/reasoning vocabulary to English (style B,
the student's explicit pick) — not just named diseases/drugs/signs
anymore, but the common scaffolding nouns and adjectives used to reason
about a case: patient, diagnosis, treatment, symptom, sign, cause,
disease, risk, management, complication, result, case, factor, and the
common severity/normality adjectives.
"""
import glob
import re

FILES = sorted(glob.glob("data_batch*.py"))

SINGLE_WORD_TERMS = {
    # people / core nouns
    "مريضة": "patient",
    "مريض": "patient",
    "تشخيص": "diagnosis",
    "علاج": "treatment",
    "عرض": "symptom",
    "أعراض": "symptoms",
    "علامة": "sign",
    "علامات": "signs",
    "خطوة": "step",
    "سبب": "cause",
    "أسباب": "causes",
    "مرض": "disease",
    "أمراض": "diseases",
    "خطر": "risk",
    "إجراء": "procedure",
    "إجراءات": "procedures",
    "تقييم": "assessment",
    "حالة": "case",
    "عامل": "factor",
    "عوامل": "factors",
    "مضاعفات": "complications",
    "مضاعفة": "complication",
    "نتيجة": "result",
    "نتائج": "results",
    "متابعة": "follow-up",
    "إدارة": "management",

    # common clinical adjectives / descriptors
    "طبيعي": "normal",
    "طبيعية": "normal",
    "حاد": "acute",
    "حادة": "acute",
    "مزمن": "chronic",
    "مزمنة": "chronic",
    "شديد": "severe",
    "شديدة": "severe",
    "خفيف": "mild",
    "خفيفة": "mild",
    "مرتفع": "elevated",
    "مرتفعة": "elevated",
    "منخفض": "low",
    "منخفضة": "low",
    "ثنائي": "bilateral",
    "ثنائية": "bilateral",
}


def make_word_pattern(term):
    return re.compile(
        r'(?<![؀-ۿ])([وفبكل]{0,2})(ال)?'
        + term + r'(?:[ً-ْ]|ا)*\b'
    )


def word_repl(english):
    def _repl(m):
        prefix = m.group(1) or ""
        article = "الـ" if m.group(2) else ""
        return f'{prefix}{article}<bdi>{english}</bdi>'
    return _repl


# longest term first so e.g. "مريضة" (with taa marbuta) is tried before
# a shorter overlapping pattern could misfire
ordered = sorted(SINGLE_WORD_TERMS.items(), key=lambda kv: -len(kv[0]))

total_changes = 0
for path in FILES:
    with open(path, encoding="utf-8") as f:
        content = f.read()
    original = content
    for term, english in ordered:
        content = make_word_pattern(term).sub(word_repl(english), content)
    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"{path}: changed")
        total_changes += 1

print("Files changed:", total_changes)
