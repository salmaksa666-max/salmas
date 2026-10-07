import importlib
import json
import re
import sys

sys.path.insert(0, "abosarah2026/scripts/batches")

batch_module = sys.argv[1]
mod = importlib.import_module(batch_module)

with open("abosarah2026/data/parsed_questions.json", encoding="utf-8") as f:
    questions = {q["qno"]: q for q in json.load(f)}

ARROW_CHARS = "→➔➡"
ALLOWED_TAGS = {"bdi", "b", "br", "ul", "li", "p", "table", "tr", "td", "th", "mark", "div"}
BAD_LT_RE = re.compile(r'<(?!/?(?:' + "|".join(ALLOWED_TAGS) + r')\b)')

errors = []
warnings = []

for qno, e in mod.EXPLANATIONS.items():
    q = questions.get(qno)
    if q is None:
        errors.append(f"{qno}: not found in parsed_questions.json")
        continue

    correct = e.get("correct_letter")
    if not correct or correct not in "ABCD":
        errors.append(f"{qno}: missing/invalid correct_letter")
    elif not q.get(f"Opt{correct}"):
        errors.append(f"{qno}: correct_letter {correct} has no option text")

    source_ans = q.get("answer_letter")
    if source_ans:
        if e.get("self_judged"):
            errors.append(f"{qno}: source HAS an answer ({source_ans}) but self_judged=True — never override a source answer")
        if correct != source_ans:
            errors.append(f"{qno}: source answer is {source_ans} but correct_letter is {correct} — must match source exactly")
    else:
        if not e.get("self_judged"):
            errors.append(f"{qno}: source has NO answer but self_judged is not True — must flag self-judged questions")

    ww = mod.WHY_WRONG.get(qno, {})
    for L in "ABCD":
        opt = q.get(f"Opt{L}")
        if opt is None:
            continue
        if correct and L == correct:
            if ww.get(L):
                warnings.append(f"{qno}: WHY_WRONG has an entry for the correct letter {L} (will be ignored)")
        else:
            if not ww.get(L, "").strip():
                errors.append(f"{qno}: missing WHY_WRONG[{L}] for a wrong option")

    full_text = " ".join([
        e.get("idea", ""),
        " ".join(e.get("why_correct", [])) if isinstance(e.get("why_correct"), list) else str(e.get("why_correct", "")),
        " ".join(e.get("when_changes", [])) if isinstance(e.get("when_changes"), list) else str(e.get("when_changes", "")),
        e.get("rule", ""),
    ])

    for ch in ARROW_CHARS:
        if ch in full_text:
            errors.append(f"{qno}: contains forbidden arrow character")
            break

    all_strings = [e.get("idea", ""), e.get("rule", "")]
    all_strings += e.get("why_correct", []) if isinstance(e.get("why_correct"), list) else [e.get("why_correct", "")]
    all_strings += e.get("when_changes", []) if isinstance(e.get("when_changes"), list) else [e.get("when_changes", "")]
    for term, meaning in e.get("clues", []):
        all_strings += [term, meaning]
    if e.get("comparison"):
        for row in e["comparison"].get("rows", []):
            all_strings += row
        all_strings += e["comparison"].get("headers", [])
    if e.get("labs"):
        for name, value, normal in e["labs"]:
            all_strings += [name, value, normal]
    if e.get("guideline_note"):
        all_strings.append(e["guideline_note"])
    for s in all_strings:
        if BAD_LT_RE.search(s):
            errors.append(f"{qno}: raw '<' not part of an allowed tag (escape as &lt;) in: {s[:60]!r}")

    hl_terms = mod.HIGHLIGHT_TERMS.get(qno, [])
    if not hl_terms:
        errors.append(f"{qno}: missing HIGHLIGHT_TERMS")
    stem = q["stem"]
    for term in hl_terms:
        if term.lower() not in stem.lower():
            errors.append(f"{qno}: highlight term '{term}' not found verbatim in question stem")

    if not e.get("clues"):
        errors.append(f"{qno}: missing clues table entries")
    if not e.get("rule", "").strip():
        errors.append(f"{qno}: missing rule")
    if not e.get("idea", "").strip():
        errors.append(f"{qno}: missing idea")
    if not e.get("why_correct"):
        errors.append(f"{qno}: missing why_correct")
    if not e.get("when_changes"):
        errors.append(f"{qno}: missing when_changes")

print(f"Checked {len(mod.EXPLANATIONS)} questions from {batch_module}")
print(f"{len(errors)} errors, {len(warnings)} warnings")
for e in errors:
    print("ERROR:", e)
for w in warnings:
    print("WARN:", w)

if errors:
    sys.exit(1)
