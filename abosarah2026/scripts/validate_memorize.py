import importlib
import json
import sys

sys.path.insert(0, "abosarah2026/scripts/batches")

batch_module = sys.argv[1]
mod = importlib.import_module(batch_module)

with open("abosarah2026/data/parsed_questions.json", encoding="utf-8") as f:
    questions = {q["qno"]: q for q in json.load(f)}

errors = []
checked = 0

for qno, m in mod.MEMORIZE.items():
    checked += 1
    q = questions.get(qno)
    if q is None:
        errors.append(f"{qno}: not found in parsed_questions.json")
        continue
    stem = q["stem"] or ""

    level2 = m.get("level2", [])
    level1 = m.get("level1", [])
    line = m.get("line", "")

    if not (1 <= len(level2) <= 2):
        errors.append(f"{qno}: level2 must have 1-2 entries, has {len(level2)}")

    total = len(level2) + len(level1)
    if not (3 <= total <= 7):
        errors.append(f"{qno}: total highlighted segments must be 3-7, has {total}")

    for term in level2 + level1:
        if not term or term not in stem:
            errors.append(f"{qno}: term not found verbatim in stem: {term!r}")
        if len(term.split()) > 6:
            errors.append(f"{qno}: segment too long (not short phrase): {term!r}")

    if not line:
        errors.append(f"{qno}: missing memorize line")
    else:
        if len(line) > 140:
            errors.append(f"{qno}: memorize line too long ({len(line)} chars)")
        if not line.startswith("احفظي:"):
            errors.append(f"{qno}: memorize line must start with 'احفظي:'")
        if "→" not in line and "->" not in line:
            errors.append(f"{qno}: memorize line missing '→' separator between clues and answer")

print(f"Checked {checked} questions from {batch_module}")
if errors:
    print(f"{len(errors)} errors")
    for e in errors:
        print("ERROR:", e)
    sys.exit(1)
else:
    print("0 errors")
