# Writing explanation batches for the AboSarah SMLE 2026 Anki deck

You are writing structured explanation data for a slice of a 2602-question
medical MCQ bank: a cleaned, already-curated Anki deck ("AboSarah Jan-Sep
2026") compiled by a student from Saudi SMLE recalls. Unlike a raw PDF dump,
this source already has a confirmed answer and a written explanation for
~90% of questions, and clearly flags the rest as uncertain. Your job is to
**translate and restructure this existing source material** into our
bilingual interactive-card format — not to re-derive medical reasoning
from scratch when good source material already exists. Read this whole
file before writing anything.

## Your inputs

- `abosarah2026/data/slices/batchNN.json` — your assigned slice: a JSON
  array of question objects with:
  - `qno` (str, e.g. `"AS-0045"`) — use this exact string as the dict key
    everywhere (not an int).
  - `section` (str) — the topic/deck, already fixed by the source (e.g.
    `"01- Medicine"`). You do NOT assign topics — this is handled
    automatically from this field, skip it entirely in your output.
  - `stem`, `OptA`..`OptD` (English, `OptD` may be `null` for 3-option
    questions) — never edit these, they are pulled verbatim by the build
    script.
  - `answer_letter` — a letter or `null`. **This is the single most
    important field.** If non-null, the source confirms this is correct —
    never override it. If `null`, the source has no confirmed answer and
    you must solve it yourself (see the rule below).
  - `answer_state` — `"sourced"` (confident), `"uncertain"`, or
    `"provisional"` (the source itself flags low confidence even when it
    did commit to a letter). The build script shows a different warning
    badge for `uncertain`/`provisional` automatically — you don't need to
    handle this, just write a normal explanation for the given
    `answer_letter`.
  - `highlight_terms_source` — keyword phrases the ORIGINAL compiler
    already tagged as important in the stem (as literal substrings).
    **Prefer reusing these directly** for your `HIGHLIGHT_TERMS` output —
    they are usually already correct and complete. Only add/adjust if a
    key clue was clearly missed.
  - `why_right` — the source's own English explanation of why the answer
    is correct. **Use this as your primary source of truth** for the
    `why_correct` content — translate/restructure it into Arabic with
    `<bdi>` terms, don't invent a different rationale.
  - `why_wrong_block` — the source's own English text covering why the
    wrong options are wrong, usually formatted as `<b>A.</b> reason...
    <br><b>B.</b> reason...`. Parse this to populate `WHY_WRONG` per
    letter — translate, don't invent.
  - `key_concept` — background teaching content from the source (often has
    an HTML `<ul>` list) — good material for `idea` and `rule`.
  - `exam_pearl` — a short source tip — good material for `rule`.
  - `compiler_note` — the original recall-compiler's raw note — background
    context only, lower priority than the three fields above.
  - `status_label` — e.g. `"Debated in source — see note"`,
    `"Duplicate"`, `"Conflicting answer in source"`. If this says the
    source itself is debating/conflicted, consider a `guideline_note`
    explaining the tension (still keep the source's `answer_letter` as
    `correct_letter` per the rule below).

- `abosarah2026/scripts/batches/batch_sample.py` — a fully worked
  reference example (AS-0001). Study its structure and English/Arabic
  density closely.
- `abosarah2026/scripts/render_explain.py` — shows exactly how your JSON
  becomes the card's HTML, including the new `labs` table feature (see
  below).
- `abosarah2026/scripts/validate_batch.py` — your self-check. Run
  `python3 abosarah2026/scripts/validate_batch.py <your_module_name>`
  (from the repo root `/home/user/salmas`) before you are done.

## THE ONE RULE THAT MATTERS MOST: source answer vs. your own judgment

- `"answer_letter": "C"` (a letter) → source-confirmed. Set
  `"correct_letter"` to that letter, `"self_judged": False`. Never
  second-guess it, even if you disagree (use `guideline_note` instead).
- `"answer_letter": null` → **no confirmed source answer.** Solve it
  yourself with real medical knowledge (the `key_concept`/`compiler_note`
  fields may still have useful partial context even when no answer was
  settled on), pick the best option, set `"correct_letter"` to your pick,
  and `"self_judged": True`. The build script shows a star badge
  automatically.

`validate_batch.py` mechanically checks this against the slice file and
will reject your batch if it's wrong — but you must still reason it
correctly per-question.

## Your task

For **every** question in your slice file, write, keyed by its `qno`
string:

1. `EXPLANATIONS[qno]`:
   - `correct_letter`, `self_judged` — per the rule above.
   - `idea` (1-2 sentences, Arabic): what the question is really testing.
   - `clues` (list of `[label, meaning]` pairs): the clue table. Base this
     on `highlight_terms_source` plus any other clue worth calling out.
   - `why_correct` (list, 2-4 bullets): translate/restructure `why_right`.
   - `when_changes` (list, 1-3 bullets): "لو تغيّر كذا، الجواب يصير كذا" —
     this is YOUR addition (teaching value), not usually in the source.
   - `rule` (str): 1-2 sentence takeaway, drawing on `exam_pearl`/
     `key_concept`.
   - `comparison` (dict or `None`): only for genuinely confusable
     options/values worth a table.
   - `labs` (list of `[test_name, value, normal_range]` or `None`): **new
     field.** Whenever the stem contains lab values or vital signs, pull
     them into this structured table instead of leaving them as prose —
     e.g. `[["Potassium", "2.9 mmol/L", "3.5-5.1 mmol/L"], ...]`. Only
     include the normal range when you are confident of the real
     reference range; never invent one. This renders as its own "التحاليل"
     table on the card, separate from the `clues` table.
   - `guideline_note` (str or `None`): only when a source-confirmed answer
     conflicts with modern guidelines, or `status_label` flags real
     source disagreement — explain briefly, keep the source's answer.

2. `WHY_WRONG[qno]`: dict keyed by WRONG letters only. Parse
   `why_wrong_block`'s per-letter text and translate it (don't invent new
   reasoning when the source already explains it).

3. `HIGHLIGHT_TERMS[qno]`: list of exact, verbatim substrings from the
   stem. **Use complete, meaningful phrases** — the student was
   previously confused when a highlight was cut short mid-phrase, so
   prefer the full `highlight_terms_source` entries as-is over inventing
   shorter fragments.

## Hard content rules

- **Never invent or guess medical facts.** For self-judged questions you
  must still reason to a real, defensible answer, not flip a coin.
- **A source-confirmed answer is always correct on the card.**
- **English stays English, literally** — stems/options are never
  rewritten by you.
- Arabic text: **Saudi colloquial, simple.** Wrap ALL medical terms AND
  generic clinical vocabulary (patient, diagnosis, treatment, symptom,
  sign, cause, risk, step, management, case, factor, complication,
  result, normal, acute, chronic, severe, mild, elevated, low, bilateral,
  etc.) in `<bdi>...</bdi>` — match `batch_sample.py`'s density exactly.
  This is the single thing the student cares about most: **never
  translate a medical term into Arabic** (no "العصب الحائر" — always the
  English name inside `<bdi>`).
- **Every line/bullet starts with an Arabic word.** Never arrows (→) —
  use "يعني", "فالجواب", "إذن".
- Lab/vital values go in the `labs` table (see above), not prose,
  whenever present in the stem.
- Total explanation length (idea + why_correct + when_changes + rule)
  roughly 150-250 words, matching `batch_sample.py`'s depth.
- Every wrong option needs a real, specific reason — never generic.

## Deliverable

Create exactly one new file: `abosarah2026/scripts/batches/batchNN.py`
(matching your assigned slice number), shaped like `batch_sample.py`:

```python
EXPLANATIONS = {"AS-0001": {...}, ...}
WHY_WRONG = {"AS-0001": {...}, ...}
HIGHLIGHT_TERMS = {"AS-0001": [...], ...}
```

Cover **every** `qno` in your slice file, no gaps. Before finishing, run
(from the repo root `/home/user/salmas`):

```
python3 abosarah2026/scripts/validate_batch.py batchNN
```

and fix every ERROR. Do not modify any other file.
