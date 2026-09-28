# -*- coding: utf-8 -*-
"""Fourth sweep: imaging/ECG/pathology descriptive vocabulary (voltage,
cardiac silhouette, tamponade, effusion, exudate/transudate, heart block,
atelectasis, mediastinal shift, calcification, loculation, congestion),
per explicit request to keep ANY term a medical student would know in
English in English, not just disease/symptom names.
"""
import glob
import re

FILES = sorted(glob.glob("data_batch*.py"))

PHRASES = {
    "ظل القلب": "cardiac silhouette",
    "تضخم القلب": "cardiomegaly",
    "تكبير القلب": "cardiomegaly",
}

SINGLE_WORD_TERMS = {
    "فولتية": "voltage",
    "فولتيه": "voltage",
    "الدكاك": "tamponade",
    "دكاك": "tamponade",
    "انصباب": "effusion",
    "نضحي": "exudative",
    "رشحي": "transudative",
    "حصار": "block",
    "انخماص": "atelectasis",
    "انزياح": "shift",
    "تكلس": "calcification",
    "تكيّس": "loculation",
    "تكيس": "loculation",
    "احتقان": "congestion",
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


def make_phrase_pattern(phrase):
    return re.compile(
        r'(?<![؀-ۿ])([وفبكل]{0,2})(ال)?'
        + re.escape(phrase) + r'\b'
    )


def phrase_repl(english):
    def _repl(m):
        prefix = m.group(1) or ""
        article = "الـ" if m.group(2) else ""
        return f'{prefix}{article}<bdi>{english}</bdi>'
    return _repl


total_changes = 0
for path in FILES:
    with open(path, encoding="utf-8") as f:
        content = f.read()
    original = content

    for phrase, english in sorted(PHRASES.items(), key=lambda kv: -len(kv[0])):
        content = make_phrase_pattern(phrase).sub(phrase_repl(english), content)

    for term, english in SINGLE_WORD_TERMS.items():
        content = make_word_pattern(term).sub(word_repl(english), content)

    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"{path}: changed")
        total_changes += 1

print("Files changed:", total_changes)
