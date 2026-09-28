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
highlight_terms = load("data/highlight_terms.json", {})
progress = load("data/progress.json", [])

topic_map = getattr(mod, "TOPICS", None)
default_topic = getattr(mod, "TOPIC", None)

for num in mod.EXPLANATIONS:
    if topic_map is not None:
        topics[str(num)] = topic_map[num]
    else:
        topics[str(num)] = default_topic
    explanations[str(num)] = mod.EXPLANATIONS[num]
    why_wrong[str(num)] = mod.WHY_WRONG.get(num, {})
    highlight_terms[str(num)] = mod.HIGHLIGHT_TERMS.get(num, [])
    if num not in progress:
        progress.append(num)

progress.sort()

with open("data/topics.json", "w", encoding="utf-8") as f:
    json.dump(topics, f, ensure_ascii=False, indent=2)
with open("data/explanations.json", "w", encoding="utf-8") as f:
    json.dump(explanations, f, ensure_ascii=False, indent=2)
with open("data/why_wrong.json", "w", encoding="utf-8") as f:
    json.dump(why_wrong, f, ensure_ascii=False, indent=2)
with open("data/highlight_terms.json", "w", encoding="utf-8") as f:
    json.dump(highlight_terms, f, ensure_ascii=False, indent=2)
with open("data/progress.json", "w", encoding="utf-8") as f:
    json.dump(progress, f, ensure_ascii=False, indent=2)

print("merged", len(mod.EXPLANATIONS), "questions from", batch_module)
print("total progress so far:", len(progress))
