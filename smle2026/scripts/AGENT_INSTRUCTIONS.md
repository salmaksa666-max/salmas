# Writing explanation batches for the SMLE 2026 Recalls Anki deck

You are writing structured explanation data for a slice of a ~2150-question
medical MCQ bank compiled from Saudi SMLE recall Telegram channels (Jan-28
Sep 2026). This is a MUCH messier source than a typical question bank: it's
a raw compilation, so expect imperfect question stems and options (stray
leftover words, odd capitalization, truncated phrases). **You never edit
the stem or option text** — it is pulled verbatim by the build script from
a slice file, not something you write. Your job is only the explanation
data. Read this whole file before writing anything.

## THE ONE RULE THAT MATTERS MOST: source answer vs. your own judgment

This source is very different from a normal confirmed answer key: **most
questions have NO answer stated in the source at all.** Your assigned
slice file tells you, per question, which case you're in:

- `"answer_letter": "C"` (some letter) → **the source confirms this is
  correct.** Treat it exactly like a confirmed answer key: never
  second-guess it even if you think another option is more correct
  (if you do think that, add a `guideline_note` explaining the
  discrepancy, same as the medicine-deck project before this one). Set
  `"correct_letter"` to that same letter and `"self_judged": False`.
- `"answer_letter": null` → **the source does NOT say what's correct.**
  You must solve the question yourself using standard, well-established
  medical knowledge, pick the single best answer, set `"correct_letter"`
  to your pick, and set `"self_judged": True`. The build script will then
  show a prominent yellow star badge on the card ("⭐ no answer in the
  source — this is my own clinical judgment") so the student always knows
  which is which. Write the explanation normally (idea/clues/why-correct/
  etc.) — you are not hedging in the prose itself, the badge already does
  that job. Never silently guess without setting `self_judged: True`.

Getting this flag right for every single question is the single most
important correctness requirement in this task. `scripts/validate_batch.py`
checks it mechanically (it cross-references your `correct_letter` and
`self_judged` against the slice file's `answer_letter`) and will reject
your batch if any question's flag doesn't match what the source actually
has — so you cannot get this wrong without the validator catching it,
but you must still think about it per-question rather than copy-pasting.

## Your inputs

- `smle2026/data/slices/batchNN.json` — your assigned slice: a JSON array
  of question objects with `num`, `stem`, `OptA`..`OptD` (English, as
  extracted — `OptD` may be `null` for 3-option questions), `answer_letter`
  (a letter or `null` — see above), `duplicate_of` (another question
  number if this is an exact duplicate stem — still write a full,
  independent explanation for it; never skip or merge it with the
  original).
- `smle2026/scripts/batches/batch_sample.py` — a fully worked reference
  example (6 questions: 5 self-judged, 1 source-confirmed). Study its
  structure, English/Arabic mixing density, and tone closely — match it
  exactly. Note how heavily English is used: not just disease/drug/sign
  names but also generic clinical nouns (patient, diagnosis, treatment,
  symptom, sign, cause, risk, step, management, case, factor,
  complication, result) and common descriptors (normal, acute, chronic,
  severe, mild, elevated, low, bilateral) — this project starts directly
  at that density, no lighter "first draft" style.
- `smle2026/scripts/render_explain.py` — shows exactly how your JSON
  fields (plus the star badge) become the card's HTML.
- `smle2026/scripts/validate_batch.py` — your self-check. Run
  `python3 smle2026/scripts/validate_batch.py <your_module_name>` (from
  the repo root `/home/user/salmas`, e.g.
  `python3 smle2026/scripts/validate_batch.py batch03`) before you are
  done, and fix every reported ERROR.

## Your task

You are assigned one slice file, e.g. `smle2026/data/slices/batch03.json`.
For **every** question object in that file, write, keyed by its `num`:

1. `TOPICS[num]` — the medical specialty, chosen **only** from this fixed
   list (exact string, no new categories):
   `Cardiology`, `Respiratory Medicine`, `Gastroenterology`, `Nephrology`,
   `Endocrinology`, `Neurology`, `Rheumatology`, `Hematology`,
   `Infectious Diseases`, `Psychiatry`, `Dermatology`,
   `Obstetrics & Gynecology`, `Pediatrics`, `General Surgery`,
   `Ophthalmology`, `ENT`, `Urology`, `Oncology`,
   `Preventive & Community Medicine`, `Geriatric Medicine`,
   `Emergency & Critical Care`, `Clinical Pharmacology & Toxicology`,
   `Musculoskeletal & Orthopedics`, `Biostatistics & Research Methods`,
   `Medical Ethics & Communication`.
   (The last two are new for this project — use them for stats/study-design
   questions and for communication-skills/consent/ethics vignettes
   respectively, instead of folding them into Preventive Medicine.)

2. `EXPLANATIONS[num]` — a dict:
   - `correct_letter` (required): "A"/"B"/"C"/"D" — see the rule above.
   - `self_judged` (required): `True`/`False` — see the rule above.
   - `idea` (str): 1-2 sentences, Arabic, what the question is really
     testing.
   - `clues` (list of `[label, meaning]` pairs): table rows. `label` can
     paraphrase, doesn't need to be a literal stem substring (that's what
     `HIGHLIGHT_TERMS` below is for).
   - `why_correct` (list, 2-4 bullets): step-by-step reasoning.
   - `when_changes` (list, 1-3 bullets): "لو تغيّر كذا، الجواب يصير كذا".
   - `rule` (str): one 1-2 sentence takeaway.
   - `comparison` (dict `{"headers":[...], "rows":[[...]]}` or `None`):
     only for genuinely confusable options/values worth a table.
   - `guideline_note` (str or `None`): only when a *source-confirmed*
     answer conflicts with well-established modern guidelines (same as
     before — state the modern guideline, keep the source's answer as
     correct on the card). Essentially never used for self-judged
     questions (there you already picked the best answer yourself).

3. `WHY_WRONG[num]` — dict keyed by the WRONG letters only (never the
   correct one), 1-2 short Arabic sentences each, specific to this
   patient/scenario, never generic.

4. `HIGHLIGHT_TERMS[num]` — 2-6 **exact, verbatim substrings** copied
   character-for-character from that question's `stem` (case-insensitive
   match, but words/punctuation must exist exactly). These get wrapped in
   `<mark>`. Given how messy this source's line-wrapping can be, there is
   no `<br>` tag to worry about here (stems are already flattened to
   single-line text) — just make sure the substring literally appears in
   the stem string you were given.

## Hard content rules (same spirit as before, read carefully)

- **Never invent or guess medical facts.** For self-judged questions,
  "guess" means picking without real justification — you must still
  reason to a genuine best answer using standard medical knowledge, not
  flip a coin. If the stem is too garbled/incomplete to safely determine
  an answer (this source has some genuinely broken entries), pick the
  most defensible option and say so plainly in `idea` (e.g. note the stem
  is incomplete) — never fabricate missing clinical details that aren't
  in the stem to make an answer "work".
- **A source-confirmed answer is always correct on the card**, even if
  you disagree — use `guideline_note` to flag it, never override
  `correct_letter`.
- **English stays English, literally** — you only ever read the stem and
  options from the slice file, never rewrite them.
- Arabic explanation text: **Saudi colloquial, simple.** Wrap ALL medical
  terms AND the generic clinical vocabulary listed above in `<bdi>...
  </bdi>`. Follow `batch_sample.py`'s density, not a lighter version of it.
- **Every line/bullet starts with an Arabic word** — never an English
  term, number, or symbol.
- **Never use arrows (→).** Use "يعني", "فالجواب", "إذن".
- Use a `comparison` table for 2+ compared terms/values, not a run-on
  sentence.
- Give lab values both units only when you're sure of the exact
  conversion factor; otherwise use the source's unit as-is.
- Total explanation length (idea + why_correct + when_changes + rule)
  should be roughly 150-250 words, matching `batch_sample.py`'s depth.
- Every wrong option needs a real, specific reason — never generic.

## Deliverable

Create exactly one new file: `smle2026/scripts/batches/batchNN.py`
(matching your assigned slice number, e.g. `batch03.py` for
`batch03.json`), shaped exactly like `batch_sample.py`:

```python
TOPICS = {1: "General Surgery", 2: "...", ...}
EXPLANATIONS = {1: {...}, ...}
WHY_WRONG = {1: {...}, ...}
HIGHLIGHT_TERMS = {1: [...], ...}
```

Cover **every** question `num` present in your slice file, with no gaps —
including duplicates (`duplicate_of` set) and 3-option questions (`OptD`
is `null` — just never write a `WHY_WRONG["D"]` or highlight anything
about a D option for those).

Before finishing, run (from the repo root `/home/user/salmas`):

```
python3 smle2026/scripts/validate_batch.py batchNN
```

and fix every ERROR it reports. Do not modify any other file in the
repository, and do not modify your own slice JSON file.
