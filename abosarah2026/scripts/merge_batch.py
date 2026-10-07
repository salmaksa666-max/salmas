import json
import importlib
import sys

sys.path.insert(0, "abosarah2026/scripts/batches")

batch_module = sys.argv[1]
mod = importlib.import_module(batch_module)


def load(path, default):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return default


explanations = load("abosarah2026/data/explanations.json", {})
why_wrong = load("abosarah2026/data/why_wrong.json", {})
highlight_terms = load("abosarah2026/data/highlight_terms.json", {})
progress = load("abosarah2026/data/progress.json", [])

for qno in mod.EXPLANATIONS:
    explanations[qno] = mod.EXPLANATIONS[qno]
    why_wrong[qno] = mod.WHY_WRONG.get(qno, {})
    highlight_terms[qno] = mod.HIGHLIGHT_TERMS.get(qno, [])
    if qno not in progress:
        progress.append(qno)

progress.sort()

with open("abosarah2026/data/explanations.json", "w", encoding="utf-8") as f:
    json.dump(explanations, f, ensure_ascii=False, indent=2)
with open("abosarah2026/data/why_wrong.json", "w", encoding="utf-8") as f:
    json.dump(why_wrong, f, ensure_ascii=False, indent=2)
with open("abosarah2026/data/highlight_terms.json", "w", encoding="utf-8") as f:
    json.dump(highlight_terms, f, ensure_ascii=False, indent=2)
with open("abosarah2026/data/progress.json", "w", encoding="utf-8") as f:
    json.dump(progress, f, ensure_ascii=False, indent=2)

print("merged", len(mod.EXPLANATIONS), "questions from", batch_module)
print("total progress so far:", len(progress))
