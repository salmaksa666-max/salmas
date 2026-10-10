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


memorize = load("abosarah2026/data/memorize.json", {})

for qno in mod.MEMORIZE:
    memorize[qno] = mod.MEMORIZE[qno]

with open("abosarah2026/data/memorize.json", "w", encoding="utf-8") as f:
    json.dump(memorize, f, ensure_ascii=False, indent=2)

print(f"merged {len(mod.MEMORIZE)} questions from {batch_module}")
print("total memorize entries so far:", len(memorize))
