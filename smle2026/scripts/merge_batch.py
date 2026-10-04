import json
import importlib
import sys

sys.path.insert(0, "smle2026/scripts/batches")

batch_module = sys.argv[1]
mod = importlib.import_module(batch_module)


def load(path, default):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return default


topics = load("smle2026/data/topics.json", {})
explanations = load("smle2026/data/explanations.json", {})
why_wrong = load("smle2026/data/why_wrong.json", {})
highlight_terms = load("smle2026/data/highlight_terms.json", {})
progress = load("smle2026/data/progress.json", [])

for num in mod.EXPLANATIONS:
    topics[str(num)] = mod.TOPICS[num]
    explanations[str(num)] = mod.EXPLANATIONS[num]
    why_wrong[str(num)] = mod.WHY_WRONG.get(num, {})
    highlight_terms[str(num)] = mod.HIGHLIGHT_TERMS.get(num, [])
    if num not in progress:
        progress.append(num)

progress.sort()

with open("smle2026/data/topics.json", "w", encoding="utf-8") as f:
    json.dump(topics, f, ensure_ascii=False, indent=2)
with open("smle2026/data/explanations.json", "w", encoding="utf-8") as f:
    json.dump(explanations, f, ensure_ascii=False, indent=2)
with open("smle2026/data/why_wrong.json", "w", encoding="utf-8") as f:
    json.dump(why_wrong, f, ensure_ascii=False, indent=2)
with open("smle2026/data/highlight_terms.json", "w", encoding="utf-8") as f:
    json.dump(highlight_terms, f, ensure_ascii=False, indent=2)
with open("smle2026/data/progress.json", "w", encoding="utf-8") as f:
    json.dump(progress, f, ensure_ascii=False, indent=2)

print("merged", len(mod.EXPLANATIONS), "questions from", batch_module)
print("total progress so far:", len(progress))
