# -*- coding: utf-8 -*-
"""Second, broader sweep: more Arabic clinical exam-sign/symptom terms
that should stay in English, using a prefix/suffix-aware regex so we
don't corrupt words like "مخدر" (drug) when fixing "خدر" (numbness).
Run once, then re-merge and rebuild.
"""
import glob
import re

FILES = sorted(glob.glob("data_batch*.py"))

# term (Arabic root) -> English replacement
SINGLE_WORD_TERMS = {
    "صفير": "wheeze",
    "أزيز": "wheeze",
    "خشخشة": "crackles",
    "زرقة": "cyanosis",
    "زراق": "cyanosis",
    "شحوب": "pallor",
    "يرقان": "jaundice",
    "ترنح": "ataxia",
    "رعشة": "tremor",
    "ارتعاش": "tremor",
    "خفقان": "palpitations",
    "تنميل": "paresthesia",
    "طنين": "tinnitus",
}

# multi-word literal phrases (no prefix/suffix gymnastics needed)
PHRASE_TERMS = {
    "تدلي الجفن": "ptosis",
}


def make_word_pattern(term):
    return re.compile(
        r'(?<![؀-ۿ])([وفبكل]{0,2})(ال)?'
        + term + r'(?:[ً-ْ]|ا)*\b'
    )


def word_repl(english):
    def _repl(m):
        prefix = m.group(1) or ""
        article = "الـ" if m.group(2) else ""  # "الـ"
        return f'{prefix}{article}<bdi>{english}</bdi>'
    return _repl


total_changes = 0
for path in FILES:
    with open(path, encoding="utf-8") as f:
        content = f.read()
    original = content

    for phrase, english in PHRASE_TERMS.items():
        content = content.replace(phrase, f'<bdi>{english}</bdi>')

    for term, english in SINGLE_WORD_TERMS.items():
        pattern = make_word_pattern(term)
        content = pattern.sub(word_repl(english), content)

    if content != original:
        n = sum(1 for a, b in zip(original.splitlines(), content.splitlines()) if a != b)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"{path}: changed")
        total_changes += 1

print("Files changed:", total_changes)
