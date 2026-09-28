"""Build the Alhomrani deck with rich Arabic explanations (alh_out/*.json)."""
import sys, os, glob, json, importlib.util, genanki
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/home/claude"); sys.path.insert(0, HERE)
import render
# card template/CSS/field helpers from build_all.py (skip its Hamoud-specific module-level code)
src = open(os.path.join(HERE, "build_all.py")).read()
B = {}
exec(src[src.index("CSS = "):src.index("def build_anki")], B)
RICH = {}
for f in sorted(glob.glob(os.path.join(HERE, "alh_out", "*.json"))): RICH.update(json.load(open(f)))
mcq = genanki.Model(1726400901, "SMLE MCQ Alhomrani", fields=[{"name": n} for n in ["Section","Question","Options","Correct","Explanation","Note","Source"]],
  templates=[{"name": "MCQ", "qfmt": B["QFMT"], "afmt": B["AFMT"]}], css=B["CSS"])
info = genanki.Model(1726400902, "SMLE Info Alhomrani", fields=[{"name": "Front"}, {"name": "Back"}], templates=[{"name": "Info", "qfmt": "{{Front}}", "afmt": "{{Front}}<hr>{{Back}}"}], css=B["CSS"])
decks = []; start = genanki.Deck(1726411000, "SMLE Surgery::Alhomrani::00 Start Here (indexes + differences)"); decks.append(start)
tot = 0; missing = []
for f in sorted(glob.glob("/home/claude/alh/[ab][0-9][0-9]_*.py")):
    spec = importlib.util.spec_from_file_location("s", f); s = importlib.util.module_from_spec(spec); spec.loader.exec_module(s)
    start.add_note(genanki.Note(model=info, guid=genanki.guid_for("alh-v3", "alh1-index", s.KEY), fields=[f"<div class=tag>ALHOMRANI · KEYWORD INDEX {s.ORDER:02d}</div><b>{s.TITLE}: clue → answer</b>", "<table class=ix>" + "".join(f"<tr><td>{c}</td><td><b>{a}</b></td></tr>" for c, a, _ in s.INDEX) + "</table>"]))
    TAG = {"NEW": "🟢 NEW", "CLEAR": "🔵 CLARIFIES", "CONFLICT": "🔴 CONFLICT"}
    start.add_note(genanki.Note(model=info, guid=genanki.guid_for("alh-v3", "alh1-diff", s.KEY), fields=[f"<div class=tag>ALHOMRANI · DIFFERENCES FROM HAMOUD {s.ORDER:02d}</div><b>{s.TITLE}</b>", "".join(f"<p><b>{TAG[t]}</b> {x} <span class=src>(A {p})</span></p>" for t, x, p in s.DIFFS)]))
    d = genanki.Deck(1726411000 + s.ORDER, f"SMLE Surgery::Alhomrani::{s.ORDER:02d} {s.TITLE}"); decks.append(d)
    for q in s.Q:
        e = RICH.get(str(q["n"]))
        if e: q["expl"] = render.render(e, q, q.get("expl", ""))
        else: missing.append(q["n"])
        fl = B["anki_fields"](s, q); FILE = getattr(s, "FILE", 1)
        fl[0] = fl[0].replace("· QA", "· A").replace("· QB", "· B"); fl[6] = f"Alhomrani {FILE}, page {q['p']}"
        d.add_note(genanki.Note(model=mcq, guid=genanki.guid_for("alh-v3", s.KEY, q["n"]), fields=fl, tags=["Surgery", "Alhomrani1", s.KEY])); tot += 1
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "SMLE_Surgery_Alhomrani_Arabic.apkg")
genanki.Package(decks).write_to_file(out)
print("topics", len(decks) - 1, "questions", tot, "rich", tot - len(missing), "missing rich", len(missing), "start cards", len(start.notes))
