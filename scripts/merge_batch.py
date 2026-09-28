import json
import importlib
import sys

batch_module = sys.argv[1] if len(sys.argv) > 1 else "data_batch1"
mod = importlib.import_module(batch_module)

def load(path, default):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return default

topics = load("data/topics.json", {})
explanations = load("data/explanations.json", {})
why_wrong = load("data/why_wrong.json", {})
progress = load("data/progress.json", [])

for num in mod.EXPLANATIONS:
    topics[str(num)] = mod.TOPIC
    explanations[str(num)] = mod.EXPLANATIONS[num]
    why_wrong[str(num)] = mod.WHY_WRONG.get(num, {})
    if num not in progress:
        progress.append(num)

progress.sort()

with open("data/topics.json", "w", encoding="utf-8") as f:
    json.dump(topics, f, ensure_ascii=False, indent=2)
with open("data/explanations.json", "w", encoding="utf-8") as f:
    json.dump(explanations, f, ensure_ascii=False, indent=2)
with open("data/why_wrong.json", "w", encoding="utf-8") as f:
    json.dump(why_wrong, f, ensure_ascii=False, indent=2)
with open("data/progress.json", "w", encoding="utf-8") as f:
    json.dump(progress, f, ensure_ascii=False, indent=2)

print("merged", len(mod.EXPLANATIONS), "questions from", batch_module)
print("total progress so far:", len(progress))
