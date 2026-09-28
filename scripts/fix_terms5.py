# -*- coding: utf-8 -*-
"""Fifth sweep: a systematic frequency-based audit of the whole corpus
(not just reactive fixes) turned up two more categories still in
Arabic: (1) drug/hormone/organism names written as Arabic transliteration
instead of English (e.g. "وارفارين" instead of "warfarin"), and (2) a
handful of missed disease/condition names (dementia, psychosis, clot/
embolism, cirrhosis, asthma in its bare form, Parkinson's, Graves').
"""
import glob
import re

FILES = sorted(glob.glob("data_batch*.py"))

PHRASES = {
    "تشمع الكبد": "liver cirrhosis",
    "الانصمام الرئوي": "pulmonary embolism",
    "ذهاني": "psychotic",
    "ذهانية": "psychotic",
    "باركنسونية": "parkinsonism",
}

SINGLE_WORD_TERMS = {
    # missed disease/condition terms
    "ربو": "asthma",
    "خرف": "dementia",
    "ذهان": "psychosis",
    "جلطة": "thrombus",
    "خثرة": "thrombus",
    "انصمام": "embolism",
    "تشمع": "cirrhosis",
    "إيكو": "echo",
    "باركنسون": "Parkinson's disease",
    "جريفز": "Graves' disease",

    # drug / hormone / organism names written as Arabic transliteration
    "وارفارين": "warfarin",
    "أسبرين": "aspirin",
    "بروبرانولول": "propranolol",
    "أتينولول": "atenolol",
    "أملوديبين": "amlodipine",
    "أنسولين": "insulin",
    "انسولين": "insulin",
    "فروسمايد": "furosemide",
    "فوروسمايد": "furosemide",
    "سبيرونولاكتون": "spironolactone",
    "دوبامين": "dopamine",
    "هيبارين": "heparin",
    "مورفين": "morphine",
    "بريدنيزولون": "prednisolone",
    "ديجوكسين": "digoxin",
    "أميودارون": "amiodarone",
    "ستاتين": "statin",
    "ميتفورمين": "metformin",
    "كلوروكوين": "chloroquine",
    "ألدوستيرون": "aldosterone",
    "سيروتونين": "serotonin",
    "برولاكتين": "prolactin",
    "بروسيلا": "Brucella",
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


total_changes = 0
for path in FILES:
    with open(path, encoding="utf-8") as f:
        content = f.read()
    original = content

    for phrase, english in sorted(PHRASES.items(), key=lambda kv: -len(kv[0])):
        content = make_phrase_pattern(phrase).sub(word_repl(english), content)

    for term, english in SINGLE_WORD_TERMS.items():
        content = make_word_pattern(term).sub(word_repl(english), content)

    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"{path}: changed")
        total_changes += 1

print("Files changed:", total_changes)
