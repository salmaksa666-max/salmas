# -*- coding: utf-8 -*-
"""Anki deck for the Yasir 1–7 November recalls, using the same 'Clinical Recall v1' note type (and look) as the MKJ decks.
Decks: ROOT::NN Specialty::NN System, cards in the PDF order (due = position).
usage: build_yasir_apkg.py TEMPLATE.apkg ITEMS_PRE.json EXPL.json OUT.apkg"""
import hashlib
import html
import json
import os
import random
import sqlite3
import string
import sys
import tempfile
import time
import zipfile

TPL, ITEMS, EXPL, OUT = sys.argv[1:5]
ROOT = "SMLE · 1–7 November (Yasir)"
SPEC_ORDER = ["Medicine", "Surgery", "Pediatrics", "OB/GYN", "Ethics & public health", "Psychiatry, ENT, eye & skin"]
items = json.load(open(ITEMS, encoding="utf-8"))
ex = json.load(open(EXPL, encoding="utf-8"))
e = lambda t: html.escape(t or "", quote=False)

work = tempfile.mkdtemp()
with zipfile.ZipFile(TPL) as z:
    z.extract("collection.anki21", work)
db = os.path.join(work, "collection.anki21")
c = sqlite3.connect(db)
for t in ("notes", "cards", "revlog", "graves"):
    c.execute(f"delete from {t}")
model = list(json.loads(c.execute("select models from col").fetchone()[0]).values())[0]
names = [f["name"] for f in model["flds"]]
decks = json.loads(c.execute("select decks from col").fetchone()[0])
tmpl = next(d for d in decks.values() if d["name"] != "Default" and not d.get("dyn"))
new_decks = {k: v for k, v in decks.items() if v["name"] == "Default"}
now, base = int(time.time()), int(time.time() * 1000)
ids = {}


def deck(name):
    parts = name.split("::")
    for i in range(1, len(parts) + 1):
        nm = "::".join(parts[:i])
        if nm not in ids:
            d = json.loads(json.dumps(tmpl))
            d["id"] = base + len(ids)
            d["name"], d["mod"], d["usn"] = nm, now, -1
            new_decks[str(d["id"])] = d
            ids[nm] = d["id"]
    return ids[name]


def clean(t):
    return t.replace("/", "-").replace(":", "-")


sys_num = {}
rnd = random.Random(1107)
chars = string.ascii_letters + string.digits + "!#$%&()*+,-./:;<=>?@[]^_`{|}~"
for pos, it in enumerate(items):
    q = it["qid"]
    x = ex[q]
    si = SPEC_ORDER.index(it["spec"]) + 1
    tl = sys_num.setdefault(it["spec"], [])
    if it["topic"] not in tl:
        tl.append(it["topic"])
    sec = f"{si:02d} {clean(it['spec'])}"
    dname = f"{ROOT}::{sec}" + ("" if it["topic"] == it["spec"] else f"::{tl.index(it['topic']) + 1:02d} {clean(it['topic'])}")
    qh = (f'<div class="question-stem-text">{it["num"]}. {e(it["stem"])}</div><div class="question-options">'
          + "".join(f'<div class="source-option" data-letter="{k}">{k}. {e(t)}</div>' for k, t in it["opts"]) + "</div>")
    study = '<style>.back-grid{grid-template-columns:minmax(0,1fr)!important}.back-card{width:min(96vw,1180px)}</style><div class="study-note-v8">'
    for lab, val in (("Why the answer is right", x.get("expl_full") or x["rule"]), ("Why not the others", x.get("whynot", "")),
                     ("Look-alike set " + (str(it["set"]["n"]) + " · " + it["set"]["title"] if it["set"] else ""), it["set"]["how"] if it["set"] else ""),
                     ("Claude's note", x.get("cnote", ""))):
        if val:
            study += f'<div class="study-item"><span class="study-label">{e(lab)}</span><div class="study-value">{e(val)}</div></div>'
    study += "</div>"
    f = dict.fromkeys(names, "")
    f.update(QNo=q, Section=sec, SourceSet="1–7 November · Yasir", OriginalQuestionHTML=qh,
             OriginalQuestionText=f'{it["num"]}. {e(it["stem"])}', AnswersExplanationsHTML=f'<div class="source-note-block">{e(it["ans"])}</div>',
             AnswersExplanationsText=it["ans"], SourceAnswer=it["ans"], StudyNote=study, SourcePage=e(it.get("exam", "")),
             MatchClass="direct" if not it["claude"] else "", MatchLabel=("Answered by Claude (no Telegram answer)" if it["claude"] else e(it["src"])),
             RepeatLabel=("Look-alike from before Nov" if it.get("exam", "").startswith("before") else ""), AnswerState=("provisional" if it["claude"] else "sourced"),
             StatusLabel=("Claude answer ⚠" if it["claude"] else ""))
    flds = "\x1f".join(f[n] for n in names)
    sort_field = f[names[model.get("sortf", 0)]]
    csum = int(hashlib.sha1(f[names[0]].encode()).hexdigest()[:8], 16)
    nid, cid = base + 100000 + pos, base + 200000 + pos
    tags = " ".join(["Source::Nov_1_7_Yasir", "Specialty::" + clean(it["spec"]).replace(" ", "_"), "System::" + clean(it["topic"]).replace(" ", "_"),
                     "AnswerState::" + ("provisional" if it["claude"] else "sourced")] + ([f"LookAlike::Set_{it['set']['n']:03d}"] if it["set"] else []))
    c.execute("insert into notes values (?,?,?,?,?,?,?,?,?,?,?)",
              (nid, "".join(rnd.choice(chars) for _ in range(10)), model["id"], now, -1, f" {tags} ", flds, sort_field, csum, 0, ""))
    c.execute("insert into cards values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
              (cid, nid, deck(dname), 0, now, -1, 0, 0, pos, 0, 0, 0, 0, 0, 0, 0, 0, ""))
c.execute("update col set decks=?, mod=?", (json.dumps(new_decks), now * 1000))
c.commit()
print(c.execute("pragma integrity_check").fetchone(), c.execute("select count(*) from notes").fetchone()[0], "notes")
c.execute("vacuum")
c.close()
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    z.write(db, "collection.anki21")
    z.writestr("media", "{}")
print("->", OUT, round(os.path.getsize(OUT) / 1e6, 2), "MB;", len(ids), "decks")
