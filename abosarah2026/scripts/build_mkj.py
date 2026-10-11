import sys, os, re, json, sqlite3, io, html, collections
sys.path.insert(0, "abosarah2026/scripts")
import genanki
import build_apkg as B

SRC = sys.argv[1]
OUT = sys.argv[2]
SOURCE_NAME = "SMLE MKJ September Without Repetition"

import zstandard, zipfile, tempfile
tmp = tempfile.mkdtemp()
zipfile.ZipFile(SRC).extractall(tmp)
raw = open(os.path.join(tmp, "collection.anki21b"), "rb").read()
dbp = os.path.join(tmp, "col.db")
open(dbp, "wb").write(zstandard.ZstdDecompressor().stream_reader(io.BytesIO(raw)).read())
c = sqlite3.connect(dbp)
names = [r[0] for r in c.execute("select name from fields where ntid=(select id from notetypes limit 1) order by ord")]
decks = {r[0]: r[1].replace("\x1f", "::") for r in c.execute("select id,name from decks")}
did_of = {r[0]: r[1] for r in c.execute("select nid,did from cards")}
rows = []
for nid, flds, tags in c.execute("select id,flds,tags from notes order by id"):
    d = dict(zip(names, flds.split("\x1f")))
    d["_deck"] = decks[did_of[nid]]
    rows.append(d)

LABELS = {
    "Why the answer is right": "ليش الجواب صح",
    "Why the endorsed answer is right": "ليش الجواب المعتمد صح",
    "Why the others are wrong": None,
    "Key concept": "KC",
    "Exam pearl": "EP",
    "Explanation source": None,
    "Author's notes (Alhomrani) and card notes": "ملاحظات الدكتور",
    "⚠ Check this answer": "⚠ تأكدي من هالجواب",
    "What this tests (no firm answer was marked by the source)": "وش يختبر السؤال",
    "How to decide between the options": "كيف تفرقين بين الخيارات",
}
BADGES = {"Repeated ×2": "🔁 تكرر ٢ مرات", "Repeated ×3": "🔁 تكرر ٣ مرات", "Repeated ×4": "🔁 تكرر ٤ مرات",
          "Updated answer": "✏ الجواب تحدّث", "Duplicate": "نسخة مكررة", "🆕 New recall": "🆕 سؤال جديد"}
TAGS = {"Repeated ×2": "تكرر_2", "Repeated ×3": "تكرر_3", "Repeated ×4": "تكرر_4", "Updated answer": "جواب_تحدث", "Duplicate": "مكرر", "🆕 New recall": "جديد"}

def kw(h):
    return re.sub(r'<span class="kw">(.*?)</span>', r'<mark class="l1">\1</mark>', h, flags=re.S)

def opt_text(h):
    return re.sub(r"^[A-E]\.\s*", "", re.sub(r"<[^>]+>", "", h)).strip()

model = B.MODEL
by_deck = {}
notes = 0
stats = collections.Counter()
for r in rows:
    qno = r["QNo"]
    qh = r["OriginalQuestionHTML"]
    m = re.search(r'<div class="question-stem-text">(.*?)</div>\s*(<div class="question-options">|$)', qh, re.S)
    stem = kw(m.group(1)) if m else kw(re.sub(r'<div class="question-options">.*', "", qh, flags=re.S))
    opts = dict((l, opt_text(t)) for l, t in re.findall(r'<div class="source-option" data-letter="([A-Z])">(.*?)</div>', qh, re.S))
    extra = ""
    if len(opts) > 4 or len(opts) < 2:
        extra = "".join(f"<br>{l}. {html.escape(t)}" for l, t in opts.items())
        stats["options_in_stem"] += 1
        opts = {}
    stem += extra

    sa = r["SourceAnswer"].strip()
    mm = re.match(r"^([A-E])\.\s*(.*)", sa, re.S)
    letter = mm.group(1) if mm else ""
    if letter and opts and letter not in opts:
        letter = ""
    answer_line = ""
    if mm and not opts:
        answer_line = f'<p><b>الجواب:</b> <bdi dir="ltr">{html.escape(mm.group(1) + ". " + mm.group(2))}</bdi></p>'

    items = re.findall(r'<div class="study-item"><span class="study-label">(.*?)</span><div class="study-value">(.*?)</div></div>', r["StudyNote"], re.S)
    why = {}
    parts, kc, ep = [], "", ""
    for lab, val in items:
        t = LABELS.get(lab, lab)
        if lab == "Why the others are wrong":
            for seg in re.split(r"<br\s*/?>", val):
                sm = re.match(r"\s*<b>([A-E])\.</b>\s*(.*)", seg, re.S)
                if sm:
                    why[sm.group(1)] = sm.group(2).strip()
            continue
        if t is None:
            continue
        if t == "KC":
            kc = val; continue
        if t == "EP":
            ep = val; continue
        parts.append(f"<p><b>{t}:</b></p><div dir=\"ltr\" style=\"text-align:left\">{val}</div>")
    topic = ""
    if kc or ep:
        body = (f'<div class="kc">{kc}</div>' if kc else "") + (f'<p class="pearl"><b>Exam pearl:</b> {ep}</p>' if ep else "")
        topic = f'<details class="topic"><summary>ملخص الموضوع ▾</summary><div class="topic-body" dir="ltr">{body}</div></details>'

    badges = []
    st = r["AnswerState"]
    if not letter:
        badges.append("⭐ المصدر ما حط جواب لهذا السؤال")
        stats["no_answer"] += 1
    elif st in ("uncertain", "provisional"):
        badges.append("⚠ المصدر مو متأكد 100% من هذا الجواب")
    for k in (r["RepeatLabel"], r["StatusLabel"]):
        if k in BADGES:
            badges.append(BADGES[k])
    badge_html = "".join(f'<div class="star-badge">{b_}</div>' for b_ in badges)

    explain = badge_html + answer_line + "".join(parts) + topic
    explain += f'<p class="src">المصدر: {SOURCE_NAME}، السؤال رقم {qno}</p>'

    deck_name = r["_deck"]
    if not letter:
        deck_name = deck_name.rsplit("::", 1)[0] + "::⚠ المشكوك فيهم"
    if deck_name not in by_deck:
        by_deck[deck_name] = genanki.Deck(B.deck_id_for("mkj::" + deck_name), deck_name)
    tags = [TAGS[k] for k in (r["RepeatLabel"], r["StatusLabel"]) if k in TAGS]
    fields = [stem] + [opts.get(L, "") for L in "ABCD"] + [("" if (L == letter or L not in why) else f'<span dir="ltr" style="display:block;text-align:left">{why[L]}</span>') for L in "ABCD"] + [letter, explain, qno]
    by_deck[deck_name].add_note(genanki.Note(model=model, fields=fields, guid=genanki.guid_for(SOURCE_NAME, qno), tags=tags))
    notes += 1

pkg = genanki.Package(list(by_deck.values()))
pkg.write_to_file(OUT)
print("notes", notes, dict(stats))
for k, v in sorted(by_deck.items()):
    print(len(v.notes), k)
