# -*- coding: utf-8 -*-
"""Dump an MKJ 'Clinical Recall' apkg to items JSON for build_tables.py, plus an EXPL json
(rule = Exam pearl, author = Alhomrani / card notes without the recall boilerplate).
usage: dump_mkj.py SRC.apkg ITEMS.json EXPL.json [DECK_SUBSTRING]  (only cards whose deck name contains it)"""
import html
import json
import os
import re
import sqlite3
import sys
import tempfile
import zipfile

SRC, ITEMS, EXPL = sys.argv[1:4]
DECK = sys.argv[4] if len(sys.argv) > 4 else ""


def plain(h):
    t = html.unescape(html.unescape(re.sub(r"<[^>]+>", "", h or "")))
    return re.sub(r"\s+", " ", t.replace("\xa0", " ")).strip()


BOIL = re.compile(r"^(Partial recall|↻ Reappeared|Same question as|Option letters re-assigned|Recaller: (Recaller )?(could not|did not|forgot|does not)|"
                  r"Recaller: Options? [A-E].{0,20}not (re)?(re)?membered|Recaller: Only one option|Stem was recalled in Arabic)", re.I)

d = tempfile.mkdtemp()
zipfile.ZipFile(SRC).extract("collection.anki21", d)
c = sqlite3.connect(os.path.join(d, "collection.anki21"))
names = [f["name"] for f in list(json.loads(c.execute("select models from col").fetchone()[0]).values())[0]["flds"]]
items, expl = [], {}
decks = json.loads(c.execute("select decks from col").fetchone()[0])
ok_nids = {nid for nid, did in c.execute("select nid, did from cards") if DECK in decks.get(str(did), {}).get("name", "")}
for nid, flds in c.execute("select id, flds from notes order by id"):
    if nid not in ok_nids:
        continue
    r = dict(zip(names, flds.split("\x1f")))
    if r.get("StatusLabel") == "Duplicate":
        continue
    qh = r["OriginalQuestionHTML"]
    m = re.search(r'<div class="question-stem-text">(.*?)</div>', qh, re.S)
    stem = re.sub(r"^\s*\d+\.\s*", "", plain(m.group(1) if m else qh.split('<div class="question-options">')[0]))
    opts = [(k, re.sub(r"^[A-E][.\-)]\s*", "", plain(t))) for k, t in
            re.findall(r'<div class="source-option" data-letter="([A-Z])">(.*?)</div>', qh, re.S)]
    sa = plain(r["SourceAnswer"])
    if "no_source_answer" in sa:
        sa = ""
    flag = " ⚠" if r["AnswerState"] not in ("confirmed", "sourced") or not sa else ""
    sn = r.get("StudyNote", "")
    pearl = re.search(r'<span class="study-label">Exam pearl</span><div class="study-value">(.*?)</div></div>', sn, re.S)
    pearl = plain(pearl.group(1)) if pearl else ""
    kc = re.search(r'<span class="study-label">Key concept</span><div class="study-value">(.*?)</div></div>', sn, re.S)
    key = ""
    if kc:
        head, _, rest = kc.group(1).partition("<ul>")
        key = plain(head)
        if key.endswith(":") or len(key) < 25:
            lis = [plain(x) for x in re.findall(r"<li>(.*?)</li>", rest, re.S)][:3]
            key = (key + " " + "; ".join(lis)).strip()
    dec = []
    dm = re.search(r'How to decide between the options</span><div class="study-value">(.*?)</div></div>', sn, re.S)
    if dm:
        for opt, txt in re.findall(r"<b>(.*?)</b>\s*:?\s*(.*?)(?=<br>|$)", dm.group(1), re.S):
            opt = re.sub(r"^([A-E]\.\s*)+", "", plain(opt)).strip(" :")
            cond = re.split(r"(?<=[.;])\s", plain(txt).lstrip(": "), 1)[0].rstrip(".;")
            if opt and cond:
                dec.append([opt, cond if len(cond) <= 190 else cond[:190].rsplit(" ", 1)[0] + "…"])
    i = sn.find("Author's notes")
    if i < 0:
        i = sn.find("Author&#x27;s notes")
    author = []
    if i >= 0:
        part = re.sub(r"<(br|/div|/li|/p|/span)[^>]*>", "\n", sn[i:])
        for ln in html.unescape(re.sub(r"<[^>]+>", "", part)).split("\n")[1:]:
            ln = re.sub(r"\s+", " ", ln).strip()
            if ln and not BOIL.match(ln):
                author.append(ln)
    q = r["QNo"]
    items.append(dict(qid=q, stem=stem, opts=opts, ans=sa or "— no firm answer in the source", flag=flag,
                      rep=r.get("RepeatLabel", "").replace("Repeated", "").strip()))
    expl[q] = dict(rule=pearl, author=" ".join(author), key=key, decide=dec)
json.dump(items, open(ITEMS, "w", encoding="utf-8"), ensure_ascii=False)
json.dump(expl, open(EXPL, "w", encoding="utf-8"), ensure_ascii=False)
print(len(items), "items;", sum(1 for v in expl.values() if v["author"]), "with author notes")
