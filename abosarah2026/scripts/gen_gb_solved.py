# -*- coding: utf-8 -*-
"""Game Boy solved sheets: items JSON (build_mkj_dense.py DUMP=) + list files -> build_review.py source.
Per question: key clues -> answer, and what flips it.  Per block: the topic lists ("@@ key | regex") that fit, each printed once.
usage: gen_gb_solved.py ITEMS.json PARTS(comma) OUT.txt LISTS.txt [LISTS2.txt ...]"""
import json
import re
import sys

items = json.load(open(sys.argv[1], encoding="utf-8"))
parts = sys.argv[2].split(",")
OUT = sys.argv[3]
LISTS = []
for f in sys.argv[4:]:
    for blk in re.split(r"(?m)^@@ ", open(f, encoding="utf-8").read())[1:]:
        head, *body = blk.rstrip("\n").split("\n")
        key, _, rx = head.partition("|")
        LISTS.append((key.strip(), re.compile(rx.strip(), re.I), body))
CH, CAP = 8, 2
items = [it for it in items if it["part"] in parts]
items.sort(key=lambda it: parts.index(it["part"]))
used, out, sec = set(), [], None
groups = []

for it in items:
    k = (it["part"], it["sec"], it["dn"])
    if groups and groups[-1][0] == k:
        groups[-1][1].append(it)
    else:
        groups.append((k, [it]))
blocks = []
for (part, s, dn), its in groups:
    chunks = [its[i:i + CH] for i in range(0, len(its), CH)]
    for n, ch in enumerate(chunks, 1):
        blocks.append((s, dn + (f"  ({n}/{len(chunks)})" if len(chunks) > 1 else ""), ch))
place = {}
for k, rx, body in LISTS:
    best = max(range(len(blocks)), key=lambda b: (len(rx.findall(" ".join(it["stem"] + " " + it["ans"] + " " + it["dn"] for it in blocks[b][2]))), -b))
    place.setdefault(best, []).append(body)
    used.add(k)
for b, (s, title, ch) in enumerate(blocks):
    if s != sec:
        sec = s
        out.append(f"# {s}")
    out.append(f"== {title}")
    for it in ch:
        stem = " ".join(it["stem"].replace("|", "/").split())
        out.append(f"q: {stem} | {it['ans'].replace('|', '/')}{it['flag']} @{it['qid']}")
    out.append("idea:")
    for i, it in enumerate(ch):
        clues = (it["l2"] + it["l1"])[:3]
        ans = re.sub(r"^[A-E]\.\s*", "", it["ans"]).strip(" .")
        if clues:
            out.append(f"- [[{i}]] 🔑 {' + '.join(clues)} → {ans}")
        if it["flip"]:
            out.append(f"- {'' if clues else f'[[{i}]] '}🔁 {it['flip']}")
    for body in place.get(b, []):
        out += body
open(OUT, "w", encoding="utf-8").write("\n".join(out) + "\n")
print(len(items), "questions;", len(used), "of", len(LISTS), "lists placed; missing:", [k for k, _, _ in LISTS if k not in used])
