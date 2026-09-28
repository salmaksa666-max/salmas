import importlib
import json
import re
import sys

batch_module = sys.argv[1]
mod = importlib.import_module(batch_module)

with open("data/parsed_questions.json", encoding="utf-8") as f:
    questions = {q["num"]: q for q in json.load(f)}

ARROW_CHARS = "→➔➡"
ARABIC_RE = re.compile(r'[؀-ۿ]')
ALLOWED_TAGS = {"bdi", "b", "br", "ul", "li", "p", "table", "tr", "td", "th", "mark", "div"}
BAD_LT_RE = re.compile(r'<(?!/?(?:' + "|".join(ALLOWED_TAGS) + r')\b)')


def word_count_arabic_ish(text):
    plain = re.sub(r'<[^>]+>', ' ', text)
    return len(plain.split())


errors = []
warnings = []

topics = getattr(mod, "TOPICS", None) or {}
for num, e in mod.EXPLANATIONS.items():
    q = questions.get(num)
    if q is None:
        errors.append(f"Q{num}: not found in parsed_questions.json")
        continue

    if num not in topics and not getattr(mod, "TOPIC", None):
        errors.append(f"Q{num}: no topic assigned")

    ans = q["answer_letter"]
    opts = {L: q.get(f"Opt{L}") for L in "ABCD"}
    if not opts.get(ans):
        errors.append(f"Q{num}: answer letter {ans} has empty option text")

    ww = mod.WHY_WRONG.get(num, {})
    for L in "ABCD":
        if opts.get(L) is None:
            continue
        if L == ans:
            if ww.get(L):
                warnings.append(f"Q{num}: WHY_WRONG has an entry for the correct letter {L} (will be ignored)")
        else:
            if not ww.get(L, "").strip():
                errors.append(f"Q{num}: missing WHY_WRONG[{L}] for a wrong option")

    full_text = " ".join([
        e.get("idea", ""),
        " ".join(e.get("why_correct", [])) if isinstance(e.get("why_correct"), list) else str(e.get("why_correct", "")),
        " ".join(e.get("when_changes", [])) if isinstance(e.get("when_changes"), list) else str(e.get("when_changes", "")),
        e.get("rule", ""),
    ])

    for ch in ARROW_CHARS:
        if ch in full_text:
            errors.append(f"Q{num}: contains forbidden arrow character")
            break

    # check every string field (incl. comparison table cells) for a stray
    # literal "<" that isn't one of our allowed tags (e.g. "<50" needs &lt;50)
    all_strings = [e.get("idea", ""), e.get("rule", "")]
    all_strings += e.get("why_correct", []) if isinstance(e.get("why_correct"), list) else [e.get("why_correct", "")]
    all_strings += e.get("when_changes", []) if isinstance(e.get("when_changes"), list) else [e.get("when_changes", "")]
    for term, meaning in e.get("clues", []):
        all_strings += [term, meaning]
    if e.get("comparison"):
        for row in e["comparison"].get("rows", []):
            all_strings += row
        all_strings += e["comparison"].get("headers", [])
    if e.get("guideline_note"):
        all_strings.append(e["guideline_note"])
    for s in all_strings:
        if BAD_LT_RE.search(s):
            errors.append(f"Q{num}: raw '<' not part of an allowed tag (escape as &lt;) in: {s[:60]!r}")

    wc = word_count_arabic_ish(full_text)
    if wc < 60:
        warnings.append(f"Q{num}: explanation seems short ({wc} words, excluding clues/comparison/fromfile)")
    if wc > 400:
        warnings.append(f"Q{num}: explanation seems long ({wc} words)")

    if not e.get("clues"):
        errors.append(f"Q{num}: missing clues table entries")

    hl_terms = mod.HIGHLIGHT_TERMS.get(num, [])
    if not hl_terms:
        errors.append(f"Q{num}: missing HIGHLIGHT_TERMS")
    stem = q["stem"]
    for term in hl_terms:
        if term.lower() not in stem.lower():
            errors.append(f"Q{num}: highlight term '{term}' not found verbatim in question stem")
        elif "<br>" in stem[max(0, stem.lower().find(term.lower())-40):stem.lower().find(term.lower())+len(term)+40].lower() and re.search(re.escape(term), stem, re.IGNORECASE):
            # crude check: make sure the matched span itself doesn't contain a <br>
            m = re.search(re.escape(term), stem, re.IGNORECASE)
            if m and "<br>" in stem[m.start():m.end()]:
                errors.append(f"Q{num}: highlight term '{term}' spans a <br> line break")

    if not e.get("rule", "").strip():
        errors.append(f"Q{num}: missing rule")
    if not e.get("idea", "").strip():
        errors.append(f"Q{num}: missing idea")
    if not e.get("why_correct"):
        errors.append(f"Q{num}: missing why_correct")
    if not e.get("when_changes"):
        errors.append(f"Q{num}: missing when_changes")

print(f"Checked {len(mod.EXPLANATIONS)} questions from {batch_module}")
print(f"{len(errors)} errors, {len(warnings)} warnings")
for e in errors:
    print("ERROR:", e)
for w in warnings:
    print("WARN:", w)

if errors:
    sys.exit(1)
