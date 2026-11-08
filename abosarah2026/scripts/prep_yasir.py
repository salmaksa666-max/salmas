# -*- coding: utf-8 -*-
"""Give each parsed Yasir item a system (sys = specialty, topic = system) using the same keyword classifiers as the
merged files, keep each look-alike set together, and write them in final order for build_dense_merged.py (PRESET=1).
usage: prep_yasir.py ITEMS.json OUT_ITEMS.json"""
import json
import os
import re
import sys

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import peds_systems  # noqa: E402
import surgery_obgyn_systems as so  # noqa: E402

src = open(os.path.join(here, "build_dense_merged.py"), encoding="utf-8").read()
ns = {}
exec(src[src.index("SYS = ["):src.index("_by = {")].split("GUIDE_FILE =")[0], ns)  # Medicine SYS / SYSORDER
MED, MED_ORDER = ns["SYS"], ns["SYSORDER"]
PSY = [("Psychiatry", r"depress|anxiety|psychos|schizo|bipolar|mania|suicid|panic|ocd|obsess|personality|antidepress|ssri|lithium|haloperidol|memory|dementia|alcohol|substance|adhd|autism|eating|anorexia|bulimia|sleep|insomnia|grief", [("Psychiatry", r".")]),
       ("ENT", r"\bears?\b|hearing|tinnitus|otitis|tonsil|nasal|nose|sinus|epistaxis|larynx|hoarse|vertigo|throat", [("ENT", r".")]),
       ("Eye", r"\beyes?\b|vision|visual|red reflex|squint|strabismus|conjunctiv|glaucoma|cataract|retina|cornea|ocular|pupil", [("Eye", r".")]),
       ("Skin", r"skin|rash|eczema|dermat|psoriasis|acne|urticaria|lesion|mole|melanoma|itch|pruritus|wart|scabies|tinea|vitiligo|alopecia", [("Skin", r".")])]
SPEC = {"Medicine": (MED, MED_ORDER + ["Other"]), "Pediatrics": (peds_systems.SYS, peds_systems.SYSORDER + ["Other"]),
        "Surgery": (so.SURGERY, so.SURGERY_ORDER + ["Other"]), "OB/GYN": (so.OBGYN, so.OBGYN_ORDER + ["Other"]),
        "Psychiatry, ENT, eye & skin": (PSY, ["Psychiatry", "ENT", "Eye", "Skin", "Other"])}
SPEC_ORDER = ["Medicine", "Surgery", "Pediatrics", "OB/GYN", "Ethics & public health", "Psychiatry, ENT, eye & skin"]


def classify(rules, it):
    stem = it["stem"].lower()
    sents = re.split(r"(?<=[.?!])\s+", stem)
    parts = ((it["ans"].lower(), 3.0), (sents[-1] if sents else "", 2.0), (" ".join(o for _, o in it["opts"]).lower(), 1.2), (stem, 1.0))
    best = None
    for s, rx, _ in rules:
        sc = sum(w * len(re.findall(rx, t)) for t, w in parts)
        if sc and (best is None or sc > best[0]):
            best = (sc, s)
    return best[1] if best else "Other"


items = json.load(open(sys.argv[1], encoding="utf-8"))
for it in items:
    rules = SPEC.get(it["spec"])
    it["sys_guess"] = classify(rules[0], it) if rules else it["spec"]
# a look-alike set stays together: it takes the most common system of its members
from collections import Counter  # noqa: E402
by_set = {}
for it in items:
    if it["set"]:
        by_set.setdefault(it["set"]["n"], []).append(it)
for members in by_set.values():
    top = Counter(m["sys_guess"] for m in members).most_common(1)[0][0]
    for m in members:
        m["sys_guess"] = top
out = []
for it in items:
    order = SPEC.get(it["spec"], (None, [it["spec"]]))[1]
    key = (SPEC_ORDER.index(it["spec"]), order.index(it["sys_guess"]) if it["sys_guess"] in order else 99, it["num"])
    out.append((key, dict(it, sys=it["spec"], topic=it["sys_guess"], tag=it["exam"] or "Nov", rep="")))
out = [x for _, x in sorted(out, key=lambda t: t[0])]
# set_first must point at the first member in the new order
seen = set()
for it in out:
    it["set_first"] = bool(it["set"]) and it["set"]["n"] not in seen
    if it["set"]:
        seen.add(it["set"]["n"])
json.dump(out, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False)
c = Counter((x["sys"], x["topic"]) for x in out)
for k in sorted(c, key=lambda k: (SPEC_ORDER.index(k[0]), k[1])):
    print(f"{c[k]:4d}  {k[0]} › {k[1]}")
