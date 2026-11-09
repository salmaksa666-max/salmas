# -*- coding: utf-8 -*-
"""Put filled answers (twin / Claude) and Alhomrani edit notes into the merged Sept+Oct apkg.
Cards still without an answer or without options are suspended.
usage: apply_fills_apkg.py IN.apkg FILL_DIR OUT.apkg"""
import html, json, os, re, sqlite3, sys, tempfile, zipfile
IN, FD, OUT = sys.argv[1:4]
fill = {}
for f in ["sepm", "oct", "pedsS", "pedsO", "obS", "obO", "surS", "surO"]:
    for x in json.load(open(os.path.join(FD, f + "_items.json"), encoding="utf-8")):
        if x.get("filled") or x.get("xnote") or x.get("corrected"):
            fill[x["qid"]] = x
work = tempfile.mkdtemp()
zipfile.ZipFile(IN).extractall(work)
c = sqlite3.connect(os.path.join(work, "collection.anki21"))
names = [f["name"] for f in list(json.loads(c.execute("select models from col").fetchone()[0]).values())[0]["flds"]]
ix = {n: i for i, n in enumerate(names)}
nf = ne = 0
for nid, flds in c.execute("select id, flds from notes").fetchall():
    f = flds.split("\x1f")
    x = fill.get(f[ix["QNo"]])
    if not x:
        continue
    if x.get("filled"):
        src = "من سؤال مشابه له جواب" if x["filled"] == "twin" else "جواب Claude (ما كان له جواب بالمصدر) ⚠"
        f[ix["SourceAnswer"]] = html.escape(x["ans"])
        f[ix["AnswersExplanationsHTML"]] = f'<div class="source-note-block">{html.escape(x["ans"])}<br><i>{src}</i></div>'
        f[ix["AnswersExplanationsText"]] = x["ans"]
        f[ix["AnswerState"]] = "provisional"
        f[ix["StatusLabel"]] = "Similar Q answer" if x["filled"] == "twin" else "Claude answer ⚠"
        f[ix["MatchLabel"]] = "Answer from a similar question" if x["filled"] == "twin" else "Not from the source"
        f[ix["MatchClass"]] = ""
        nf += 1
    if x.get("corrected"):
        f[ix["SourceAnswer"]] = html.escape(x["ans"])
        f[ix["AnswersExplanationsHTML"]] = f'<div class="source-note-block">{html.escape(x["ans"])}<br><i>عدّله الحمراني (منشور #{x["corrected"]})</i></div>'
        f[ix["AnswersExplanationsText"]] = x["ans"]
        f[ix["StatusLabel"]] = "Alhomrani corrected ✏"
        nf += 1
    if x.get("xnote"):
        notes = re.findall(r'<div class="nt ed">✏ (.*?)</div>', x["xnote"])
        if notes:
            item = ('<div class="study-item"><span class="study-label">✏ تعديلات الحمراني</span><div class="study-value" dir="auto">'
                    + "<br>".join(notes) + "</div></div>")
            sn = f[ix["StudyNote"]]
            f[ix["StudyNote"]] = sn.replace('<div class="study-note-v8">', '<div class="study-note-v8">' + item, 1) if 'study-note-v8' in sn else item + sn
            ne += 1
    c.execute("update notes set flds=?, mod=strftime('%s','now'), usn=-1 where id=?", ("\x1f".join(f), nid))
# suspend what is still empty
si, oi = ix["SourceAnswer"], ix["OriginalQuestionHTML"]
empty = [nid for nid, flds in c.execute("select id, flds from notes").fetchall()
         if (lambda f: "no_source_answer" in f[si] or not f[si].strip() or "source-option" not in f[oi])(flds.split("\x1f"))]
c.execute("update cards set queue=0 where queue=-1")
c.executemany("update cards set queue=-1 where nid=?", [(n,) for n in empty])
c.commit()
print(nf, "answers filled;", ne, "notes with Alhomrani edits;", len(empty), "suspended (still empty)")
c.execute("vacuum"); c.close()
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for fn in os.listdir(work):
        z.write(os.path.join(work, fn), fn)
print("->", OUT)
