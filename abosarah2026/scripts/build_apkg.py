import json
import hashlib
import re
import sys
import genanki

sys.path.insert(0, "abosarah2026/scripts")
from render_explain import render_explain

SOURCE_NAME = "AboSarah Jan-Sep 2026"
MODEL_ID = 1948372605  # fixed, never change
PARENT_DECK_NAME = "SMLE AboSarah Jan-Sep 2026"

FRONT_TEMPLATE = """
<div id="q" dir="ltr">{{Question}}</div>
<div id="opts" dir="ltr">
  {{#OptA}}<div class="opt" data-k="A"><span class="t">{{OptA}}</span><div class="why" dir="rtl">{{WhyA}}</div></div>{{/OptA}}
  {{#OptB}}<div class="opt" data-k="B"><span class="t">{{OptB}}</span><div class="why" dir="rtl">{{WhyB}}</div></div>{{/OptB}}
  {{#OptC}}<div class="opt" data-k="C"><span class="t">{{OptC}}</span><div class="why" dir="rtl">{{WhyC}}</div></div>{{/OptC}}
  {{#OptD}}<div class="opt" data-k="D"><span class="t">{{OptD}}</span><div class="why" dir="rtl">{{WhyD}}</div></div>{{/OptD}}
</div>
<div id="expBtn" class="expBtn" style="display:none">الشرح الكامل ▾</div>
<div id="exp" dir="rtl" style="display:none">{{Explain}}</div>
<div id="correct" style="display:none">{{Correct}}</div>
<div id="qid" style="display:none">{{QID}}</div>
<script>
(function () {
  var correct = document.getElementById('correct').textContent.trim();
  var opts = document.querySelectorAll('.opt');
  var expBox = document.getElementById('exp');
  var btn = document.getElementById('expBtn');
  var key = 'pick_' + document.getElementById('qid').textContent.trim();
  function hasSelection() {
    var s = window.getSelection ? window.getSelection().toString() : '';
    return s && s.length > 0;
  }
  var known = Array.prototype.some.call(opts, function (o) { return o.dataset.k === correct; });
  if (!opts.length) { btn.style.display = 'block'; }
  function reveal(picked) {
    if (!known) {
      opts.forEach(function (o) { o.classList.add('done'); });
      btn.style.display = 'block';
      var m0 = expBox.querySelector('#memo');
      if (m0) btn.parentNode.insertBefore(m0, btn);
      return;
    }
    opts.forEach(function (o) {
      var k = o.dataset.k;
      o.classList.add('done');
      if (k === correct) {
        o.classList.add('right');
      } else {
        o.classList.add('wrongOpt');
        if (k === picked) o.classList.add('picked');
      }
    });
    btn.style.display = 'block';
    var memo = expBox.querySelector('#memo');
    if (memo) btn.parentNode.insertBefore(memo, btn);
  }
  btn.addEventListener('click', function () {
    if (hasSelection()) return;
    var open = expBox.style.display === 'block';
    expBox.style.display = open ? 'none' : 'block';
    btn.textContent = open ? 'الشرح الكامل ▾' : 'إخفاء الشرح ▴';
  });
  opts.forEach(function (o) {
    o.addEventListener('click', function () {
      if (hasSelection()) return;
      if (document.querySelector('.opt.done')) return;
      try { sessionStorage.setItem(key, o.dataset.k); } catch (err) {}
      reveal(o.dataset.k);
    });
  });
  setTimeout(function () {
    if (document.getElementById('answer') && !document.querySelector('.opt.done')) {
      var p = null;
      try { p = sessionStorage.getItem(key); } catch (err) {}
      reveal(p);
    }
  }, 0);
})();
</script>
"""

BACK_TEMPLATE = """{{FrontSide}}
<hr id="answer">
"""

CSS = """
#q { direction:ltr; text-align:left; }
#q mark { background:#fff3a3; color:#000; padding:0 2px; border-radius:2px; }
.opt { display:block; padding:12px; margin:8px 0; border:1px solid #ccc; border-radius:10px; color:inherit; direction:ltr; text-align:left; cursor:pointer; }
#q, .opt, .opt .why, #exp, #memo { -webkit-user-select:text; user-select:text; }
.expBtn { cursor:pointer; }
.opt .why { display:none; font-size:14px; margin-top:6px; direction:rtl; text-align:right; }
.opt.done.wrongOpt .why { display:block; }
.opt.right { background:#d4f5dd; border-color:#2e9e56; }
.opt.picked { background:#fde0e0; border-color:#d33; }
.opt.picked .t { text-decoration:line-through; }
.expBtn { display:block; text-align:center; background:#2e9e56; color:#fff; padding:8px; border-radius:8px; margin-top:8px; text-decoration:none; direction:rtl; }
#exp { margin-top:8px; direction:rtl; text-align:right; }
#exp .star-badge { background:#fff3cd; border:2px solid #e0a800; color:#7a5c00; padding:10px; border-radius:10px; margin-bottom:10px; font-weight:bold; text-align:center; direction:rtl; }
#exp .fromfile { direction:ltr; text-align:left; margin-bottom:8px; padding:8px; background:#f2f2f2; border-radius:6px; }
#exp table.clues, #exp table.cmp { width:100%; border-collapse:collapse; margin:8px 0; direction:rtl; }
#exp table.clues td, #exp table.clues th, #exp table.cmp td, #exp table.cmp th { border:1px solid #ccc; padding:6px; text-align:center; font-size:13px; }
#exp p { margin:8px 0 4px 0; }
#exp ul { margin:4px 0; padding-inline-start:20px; }
#exp p.note { background:#fff8e1; padding:6px; border-radius:6px; }
#exp p.src { font-size:12px; color:#777; direction:ltr; text-align:left; }
#q mark.l2 { background:#ffca28; color:#000 !important; padding:0 2px; border-radius:3px; font-weight:bold; }
#q mark.l1 { background:#ffe9a8; color:#000 !important; padding:0 2px; border-radius:3px; }
#memo { margin-top:10px; padding:8px 10px; background:#e8f5e9; color:#000; border-radius:6px; font-size:14px; }
.night_mode #q mark.l2, .nightMode #q mark.l2, .night-mode #q mark.l2 { background:#caa400; color:#000 !important; }
.night_mode #q mark.l1, .nightMode #q mark.l1, .night-mode #q mark.l1 { background:#8a7a3a; color:#000 !important; }
.night_mode #memo, .nightMode #memo, .night-mode #memo { background:#3a4a40; color:#eee; }
#q mark { color:#000 !important; }

/* always-dark theme */
.card, body { background:#1c1c1e !important; color:#e6e6e6 !important; }
.opt { border-color:#444; color:#e6e6e6; }
.opt.right { background:#1f3a2a; border-color:#4caf78; color:#e6f4ea; }
.opt.picked { background:#3a2020; border-color:#e06666; color:#f6dede; }
.opt .why { color:#d0d0d0; }
.expBtn { background:#2e7d4f; color:#fff; }
#exp table.clues td, #exp table.clues th, #exp table.cmp td, #exp table.cmp th { border-color:#555; }
#exp .star-badge { background:#3a3420; color:#f1d98a; border-color:#a88a2a; }
#exp .fromfile { background:#2a2a2a; color:#ddd; }
#exp p.note { background:#3a3420; color:#f1e7c6; }
#exp p.src { color:#999; }
#exp details.topic { border-color:#3e5a4f; }
#exp details.topic summary { background:#25352f; color:#cfe8dd; }
#exp .topic-body p.pearl { background:#3a3420; color:#f1e7c6; }
#memo { background:#26352c; color:#e6f4ea; }
#q mark.l2 { background:#e0b400; color:#000 !important; }
#q mark.l1 { background:#8a7a3a; color:#000 !important; }
#exp details.topic { margin:10px 0; border:1px solid #9bbcae; border-radius:8px; overflow:hidden; }
#exp details.topic summary { cursor:pointer; padding:8px 10px; background:#e7f3ee; color:#1f4d40; font-weight:bold; list-style:none; }
#exp details.topic summary::-webkit-details-marker { display:none; }
#exp .topic-body { padding:8px 12px; text-align:left; font-size:14px; line-height:1.55; }
#exp .topic-body ul { padding-inline-start:20px; margin:4px 0; }
#exp .topic-body p.pearl { background:#fff8e1; color:#000; padding:6px 8px; border-radius:6px; margin-top:8px; }
.night_mode .opt.right, .nightMode .opt.right, .night-mode .opt.right { background:#1f3a2a; border-color:#4caf78; color:#e6f4ea; }
.night_mode .opt.picked, .nightMode .opt.picked, .night-mode .opt.picked { background:#3a2020; border-color:#e06666; color:#f6dede; }
.night_mode #exp p.note, .nightMode #exp p.note, .night-mode #exp p.note { background:#3a3420; color:#f1e7c6; }
.night_mode #exp .fromfile, .nightMode #exp .fromfile, .night-mode #exp .fromfile { background:#2a2a2a; color:#ddd; }
.night_mode #exp .star-badge, .nightMode #exp .star-badge, .night-mode #exp .star-badge { background:#3a3420; color:#f1d98a; border-color:#a88a2a; }
.night_mode #exp p.src, .nightMode #exp p.src, .night-mode #exp p.src { color:#aaa; }
.night_mode #exp details.topic summary, .nightMode #exp details.topic summary, .night-mode #exp details.topic summary { background:#25352f; color:#cfe8dd; }
.night_mode #exp details.topic, .nightMode #exp details.topic, .night-mode #exp details.topic { border-color:#3e5a4f; }
.night_mode #exp .topic-body p.pearl, .nightMode #exp .topic-body p.pearl, .night-mode #exp .topic-body p.pearl { background:#3a3420; color:#f1e7c6; }
"""

MODEL = genanki.Model(
    MODEL_ID,
    "AboSarah SMLE MCQ",
    fields=[
        {"name": "Question"},
        {"name": "OptA"}, {"name": "OptB"}, {"name": "OptC"}, {"name": "OptD"},
        {"name": "WhyA"}, {"name": "WhyB"}, {"name": "WhyC"}, {"name": "WhyD"},
        {"name": "Correct"},
        {"name": "Explain"},
        {"name": "QID"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": FRONT_TEMPLATE,
            "afmt": BACK_TEMPLATE,
        }
    ],
    css=CSS,
)


def deck_id_for(name):
    h = hashlib.md5(("abosarah2026-deck::" + name).encode("utf-8")).hexdigest()
    return int(h[:8], 16)


def guid_for(qno, topic):
    return genanki.guid_for(SOURCE_NAME, qno, topic)


def highlight_clues(stem, clue_terms):
    html = stem
    for term in clue_terms:
        pattern = re.compile(re.escape(term), re.IGNORECASE)
        if pattern.search(html):
            html = pattern.sub(lambda m: f"<mark>{m.group(0)}</mark>", html, count=1)
    return html


def highlight_memorize(stem, level2_terms, level1_terms):
    html = stem
    # longer terms first so overlapping substrings don't get double-wrapped
    ordered = sorted(level2_terms, key=len, reverse=True) + sorted(level1_terms, key=len, reverse=True)
    css_class = {t: "l2" for t in level2_terms}
    for t in level1_terms:
        css_class.setdefault(t, "l1")
    for term in ordered:
        pattern = re.compile(re.escape(term), re.IGNORECASE)
        cls = css_class[term]
        if pattern.search(html):
            html = pattern.sub(lambda m, cls=cls: f'<mark class="{cls}">{m.group(0)}</mark>', html, count=1)
    return html


def build():
    with open("abosarah2026/data/parsed_questions.json", encoding="utf-8") as f:
        questions = {q["qno"]: q for q in json.load(f)}
    with open("abosarah2026/data/explanations.json", encoding="utf-8") as f:
        explanations = json.load(f)
    with open("abosarah2026/data/why_wrong.json", encoding="utf-8") as f:
        why_wrong = json.load(f)
    with open("abosarah2026/data/highlight_terms.json", encoding="utf-8") as f:
        highlight_terms_map = json.load(f)
    with open("abosarah2026/data/progress.json", encoding="utf-8") as f:
        progress = set(json.load(f))
    try:
        with open("abosarah2026/data/doubtful.json", encoding="utf-8") as f:
            doubtful = json.load(f)
    except FileNotFoundError:
        doubtful = {}
    try:
        with open("abosarah2026/data/memorize.json", encoding="utf-8") as f:
            memorize_map = json.load(f)
    except FileNotFoundError:
        memorize_map = {}

    decks = {}
    parent_deck_id = deck_id_for(PARENT_DECK_NAME)
    parent_deck = genanki.Deck(parent_deck_id, PARENT_DECK_NAME)
    decks[PARENT_DECK_NAME] = parent_deck

    count = 0
    for qno in sorted(progress):
        q = questions.get(qno)
        if q is None:
            continue
        e = explanations[qno]
        ww = why_wrong.get(qno, {})
        topic = q["section"]

        reason = doubtful.get(qno)
        if reason == "answer":
            full_deck_name = f"{PARENT_DECK_NAME}::⚠ المشكوك فيهم"
            tags = ["مشكوك_الجواب"]
        elif reason == "explain":
            full_deck_name = f"{PARENT_DECK_NAME}::⚠ المشكوك فيهم::2 شرح يحتاج مراجعة"
            tags = ["شرح_يحتاج_مراجعة"]
        else:
            full_deck_name = f"{PARENT_DECK_NAME}::{topic}"
            tags = []
        if full_deck_name not in decks:
            decks[full_deck_name] = genanki.Deck(deck_id_for(full_deck_name), full_deck_name)
        deck = decks[full_deck_name]

        memo = memorize_map.get(qno)
        if memo:
            question_html = highlight_memorize(q["stem"], memo.get("level2", []), memo.get("level1", []))
            line = memo.get("line", "")
            head, _, rest = line.partition(":")
            memo_html = f'<b>{head}:</b> <bdi dir="ltr">{rest.strip()}</bdi>' if rest else line
        else:
            hl_terms = highlight_terms_map.get(qno, [])
            question_html = highlight_clues(q["stem"], hl_terms)
            memo_html = ""

        explain_html = render_explain(q, e, SOURCE_NAME)

        ans_letter = e["correct_letter"]
        why_fields = {}
        for L in "ABCD":
            if L == ans_letter:
                why_fields[L] = ""
            else:
                why_fields[L] = ww.get(L, "")

        fields = [
            question_html,
            q["OptA"] or "", q["OptB"] or "", q["OptC"] or "", q["OptD"] or "",
            why_fields["A"], why_fields["B"], why_fields["C"], why_fields["D"],
            ans_letter,
            (f'<div id="memo" dir="rtl">{memo_html}</div>' if memo_html else "") + explain_html,
            qno,
        ]

        note = genanki.Note(
            model=MODEL,
            fields=fields,
            guid=guid_for(qno, topic),
            tags=tags,
        )
        deck.add_note(note)
        count += 1

    print("built", count, "cards across", len(decks) - 1, "topic decks")

    pkg = genanki.Package(list(decks.values()))
    pkg.write_to_file("abosarah2026/build/abosarah_smle_2026.apkg")
    print("wrote abosarah2026/build/abosarah_smle_2026.apkg")


if __name__ == "__main__":
    build()
