import json
import hashlib
import re
import sys
import genanki

sys.path.insert(0, "scripts")
from render_explain import render_explain

SOURCE_FILENAME = "Full_MG_Confirmed_internal_2_File"
MODEL_ID = 1901820391  # fixed, never change
PARENT_DECK_NAME = "Medicine (MG)"

FRONT_TEMPLATE = """
<div id="q" dir="ltr">{{Question}}</div>
<div id="opts" dir="ltr">
  {{#OptA}}<a href="#" class="opt" data-k="A"><span class="t">{{OptA}}</span><div class="why" dir="rtl">{{WhyA}}</div></a>{{/OptA}}
  {{#OptB}}<a href="#" class="opt" data-k="B"><span class="t">{{OptB}}</span><div class="why" dir="rtl">{{WhyB}}</div></a>{{/OptB}}
  {{#OptC}}<a href="#" class="opt" data-k="C"><span class="t">{{OptC}}</span><div class="why" dir="rtl">{{WhyC}}</div></a>{{/OptC}}
  {{#OptD}}<a href="#" class="opt" data-k="D"><span class="t">{{OptD}}</span><div class="why" dir="rtl">{{WhyD}}</div></a>{{/OptD}}
</div>
<div id="exp" dir="rtl" style="display:none">{{Explain}}</div>
<div id="correct" style="display:none">{{Correct}}</div>
<div id="qid" style="display:none">{{QID}}</div>
<script>
(function () {
  var correct = document.getElementById('correct').textContent.trim();
  var opts = document.querySelectorAll('.opt');
  var expBox = document.getElementById('exp');
  var key = 'pick_' + document.getElementById('qid').textContent.trim();
  function reveal(picked) {
    opts.forEach(function (o) {
      var k = o.dataset.k;
      o.classList.add('done');
      if (k === correct) {
        o.classList.add('right');
        o.appendChild(expBox);
        expBox.style.display = 'none';
        addButton(o);
      } else {
        o.classList.add('wrongOpt');
        if (k === picked) o.classList.add('picked');
      }
    });
  }
  function addButton(o) {
    var b = document.createElement('a');
    b.href = '#'; b.className = 'expBtn'; b.textContent = 'الشرح الكامل ▾';
    b.addEventListener('click', function (e) {
      e.preventDefault(); e.stopPropagation();
      var open = expBox.style.display === 'block';
      expBox.style.display = open ? 'none' : 'block';
      b.textContent = open ? 'الشرح الكامل ▾' : 'إخفاء الشرح ▴';
    });
    o.appendChild(b);
  }
  opts.forEach(function (o) {
    o.addEventListener('click', function (e) {
      e.preventDefault(); e.stopPropagation();
      if (document.querySelector('.opt.done')) return;
      try { sessionStorage.setItem(key, o.dataset.k); } catch (err) {}
      reveal(o.dataset.k);
    });
  });
  // deferred: the trailing #answer marker (back template only) is parsed
  // AFTER this inline script runs, so check for it on the next tick.
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
.opt { display:block; padding:12px; margin:8px 0; border:1px solid #ccc; border-radius:10px; text-decoration:none; color:inherit; direction:ltr; text-align:left; }
.opt .why { display:none; font-size:14px; margin-top:6px; direction:rtl; text-align:right; }
.opt.done.wrongOpt .why { display:block; }
.opt.right { background:#d4f5dd; border-color:#2e9e56; }
.opt.picked { background:#fde0e0; border-color:#d33; }
.opt.picked .t { text-decoration:line-through; }
.expBtn { display:block; text-align:center; background:#2e9e56; color:#fff; padding:8px; border-radius:8px; margin-top:8px; text-decoration:none; direction:rtl; }
#exp { margin-top:8px; direction:rtl; text-align:right; }
#exp .fromfile { direction:ltr; text-align:left; margin-bottom:8px; padding:8px; background:#f2f2f2; border-radius:6px; }
#exp table.clues, #exp table.cmp { width:100%; border-collapse:collapse; margin:8px 0; direction:rtl; }
#exp table.clues td, #exp table.clues th, #exp table.cmp td, #exp table.cmp th { border:1px solid #ccc; padding:6px; text-align:center; font-size:13px; }
#exp p { margin:8px 0 4px 0; }
#exp ul { margin:4px 0; padding-inline-start:20px; }
#exp p.note { background:#fff8e1; padding:6px; border-radius:6px; }
#exp p.src { font-size:12px; color:#777; direction:ltr; text-align:left; }
"""

MODEL = genanki.Model(
    MODEL_ID,
    "Medicine MG MCQ",
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
    h = hashlib.md5(("medicine-mg-deck::" + name).encode("utf-8")).hexdigest()
    return int(h[:8], 16)


def guid_for(num, topic):
    return genanki.guid_for(SOURCE_FILENAME, str(num), topic)


CLUE_WORDS = None


def highlight_clues(stem, clue_terms):
    html = stem
    for term in clue_terms:
        pattern = re.compile(re.escape(term), re.IGNORECASE)
        if pattern.search(html):
            html = pattern.sub(lambda m: f"<mark>{m.group(0)}</mark>", html, count=1)
    return html


def build():
    with open("data/parsed_questions.json", encoding="utf-8") as f:
        questions = json.load(f)
    with open("data/topics.json", encoding="utf-8") as f:
        topics = json.load(f)
    with open("data/explanations.json", encoding="utf-8") as f:
        explanations = json.load(f)
    with open("data/why_wrong.json", encoding="utf-8") as f:
        why_wrong = json.load(f)
    with open("data/highlight_terms.json", encoding="utf-8") as f:
        highlight_terms_map = json.load(f)
    with open("data/progress.json", encoding="utf-8") as f:
        progress = set(json.load(f))

    decks = {}
    package_media = []

    parent_deck_id = deck_id_for(PARENT_DECK_NAME)
    parent_deck = genanki.Deck(parent_deck_id, PARENT_DECK_NAME)
    decks[PARENT_DECK_NAME] = parent_deck

    count = 0
    for q in questions:
        num = q["num"]
        if num not in progress:
            continue
        key = str(num)
        topic = topics.get(key)
        if not topic:
            continue
        e = explanations[key]
        ww = why_wrong.get(key, {})

        full_deck_name = f"{PARENT_DECK_NAME}::{topic}"
        if full_deck_name not in decks:
            decks[full_deck_name] = genanki.Deck(deck_id_for(full_deck_name), full_deck_name)
        deck = decks[full_deck_name]

        hl_terms = highlight_terms_map.get(key, [])
        question_html = highlight_clues(q["stem"], hl_terms)

        explain_html = render_explain(q, e, SOURCE_FILENAME)

        ans_letter = q["answer_letter"]
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
            explain_html,
            str(num),
        ]

        note = genanki.Note(
            model=MODEL,
            fields=fields,
            guid=guid_for(num, topic),
        )
        deck.add_note(note)
        count += 1

    print("built", count, "cards across", len(decks) - 1, "topic decks")

    pkg = genanki.Package(list(decks.values()))
    pkg.write_to_file("build/medicine_mg.apkg")
    print("wrote build/medicine_mg.apkg")


if __name__ == "__main__":
    build()
