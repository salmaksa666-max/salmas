# Writing explanation batches for the Medicine (MG) Anki deck

You are writing structured explanation data for a slice of a 976-question
medical MCQ bank (Saudi SMLE-style internal medicine question bank called
"Full_MG_Confirmed_internal_2_File"). Your output is a single Python file
that a build script consumes to render Anki flashcards. Read this whole
file before writing anything.

## Your inputs

- `data/parsed_questions.json` — the full parsed question bank. Each entry
  has: `num` (question number), `stem` (the English question stem, HTML
  with literal `<br>` line breaks — **never alter this text**), `OptA`..`OptD`
  (English option text, `OptD` may be `null` for 3-option questions),
  `answer_letter` (A/B/C/D — this is the ONLY correct answer; it comes from
  the source file's answer key and must never be second-guessed or
  "corrected" even if you believe real-world guidelines differ — in that
  case add a `guideline_note` instead, see below), `extra_note` (a rare,
  short original annotation from the source file — usually empty).
- `scripts/data_batch1.py` — a fully worked reference example (13 finished
  questions). Study its structure and Arabic writing style closely; match
  its tone and depth exactly.
- `scripts/render_explain.py` — shows exactly how your JSON fields get
  turned into the card's HTML. Useful to understand what each field is for.
- `scripts/validate_batch.py` — a self-check script. Run
  `python3 scripts/validate_batch.py <your_module_name>` (from the repo
  root, e.g. `python3 scripts/validate_batch.py data_batch3`) before you are
  done, and fix every reported ERROR (warnings are informational).

## Your task

You are assigned a contiguous range of question numbers (given to you in
the task prompt). For every question in that range, write:

1. `TOPICS[num]` — the medical specialty this question belongs to, chosen
   **only** from this fixed list (use the exact string, do not invent new
   categories, do not translate them):
   `Cardiology`, `Respiratory Medicine`, `Gastroenterology`, `Nephrology`,
   `Endocrinology`, `Neurology`, `Rheumatology`, `Hematology`,
   `Infectious Diseases`, `Psychiatry`, `Dermatology`,
   `Obstetrics & Gynecology`, `Pediatrics`, `General Surgery`,
   `Ophthalmology`, `ENT`, `Urology`, `Oncology`,
   `Preventive & Community Medicine`, `Geriatric Medicine`,
   `Emergency & Critical Care`, `Clinical Pharmacology & Toxicology`,
   `Musculoskeletal & Orthopedics`.
   Pick the single best fit for each question based on what it actually
   tests (the underlying disease/system), not superficial wording.
   Consecutive questions in the source file are usually (not always) from
   the same specialty block — read a few around each question to spot
   block boundaries, but classify each question on its own merits.

2. `EXPLANATIONS[num]` — a dict with these keys (all required unless noted):
   - `idea` (str): 1-2 sentences, Arabic — what the question is really
     testing / the likely diagnosis or concept.
   - `clues` (list of `[label, meaning]` pairs): the table of clues shown
     to the learner ("من السؤال" / "يعني وش"). `label` can be a short
     paraphrase (does not need to be a literal substring of the stem) but
     must clearly point to something actually in the stem — never invent a
     finding that isn't there. `meaning` is the Arabic explanation of why
     that detail matters.
   - `why_correct` (list of str, 2-4 bullet points): step-by-step reasoning
     for why the file's answer is right.
   - `when_changes` (list of str, 1-3 bullet points): "لو تغيّر كذا، الجواب
     يصير كذا" — a changed detail and the new answer.
   - `rule` (str): one 1-2 sentence memorable takeaway.
   - `comparison` (dict `{"headers": [...], "rows": [[...], ...]}` or
     `None`): only when there are genuinely confusable options/values worth
     a table (drug choices, lab value comparisons, disease look-alikes).
     Omit (use `None`) when it would just repeat `why_correct`.
   - `guideline_note` (str or `None`): **only** set this when the file's
     answer conflicts with a real, well-established modern guideline you
     are confident about (e.g. an outdated vaccine schedule, an old staging
     system). State the current guideline briefly, but make clear the
     file's answer is what stays correct on the card. Leave `None` in the
     overwhelming majority of questions — do not invent conflicts.

3. `WHY_WRONG[num]` — a dict keyed by the WRONG letters only (never include
   the correct letter), e.g. `{"B": "...", "C": "...", "D": "..."}` for a
   question whose answer is A. Each value is 1-2 short Arabic sentences
   explaining why that specific option is wrong for THIS patient/scenario.

4. `HIGHLIGHT_TERMS[num]` — a list of 2-6 **exact, verbatim substrings**
   copied character-for-character from that question's `stem` field (case
   can differ, matching is case-insensitive, but the words and punctuation
   must exist exactly as in the stem). These get wrapped in `<mark>` on the
   card front to highlight key clues. **A term must never span across a
   `<br>`** — if the phrase you want crosses a line break in the stem, stop
   the term before the `<br>` or start it after. Pick the single most
   clinically important words/phrases (ages, key symptoms, lab values,
   timing, negatives like "no fever"). This is separate from `clues` above
   — `clues` can paraphrase, `HIGHLIGHT_TERMS` cannot.

## Hard content rules — read carefully, these are non-negotiable

- **Never invent or guess medical facts.** Everything must come from the
  question itself or well-established, undisputed medical knowledge
  (textbook-level teaching points). If something needed to fully explain a
  question isn't clear from the stem, leave it out rather than guessing.
- **The file's `answer_letter` is always "correct" on the card**, even in
  the rare case you think a guideline disagrees — explain the file's
  answer normally and add a `guideline_note` only in that case.
- **English stays English, literally.** Never translate or reword the
  question stem or options — you only ever read them, you never rewrite
  them (the build script pulls them straight from `parsed_questions.json`).
- Arabic explanation text: **Saudi colloquial, simple, as if explaining to
  a colleague before an exam.** Medical terms, drug names, disease names,
  investigations and key symptoms stay in English, wrapped in `<bdi>...
  </bdi>` (e.g. `تعتبر <bdi>hypercalcemia</bdi> شديدة`).
- **Every line/bullet must start with an Arabic word** — never start a
  sentence with an English term, a number, or a symbol.
- **Never use arrows (→).** Use words like "يعني", "فالجواب", "إذن".
- Don't end a sentence with a lone English word in parentheses.
- When comparing 2+ terms or values, use a `comparison` table, not a
  run-on sentence.
- When you state a lab value with a known unit conversion you are sure of,
  give both units (e.g. mmol/L and mg/dL for calcium/glucose) — otherwise
  just use the file's unit, don't guess a conversion.
- Total explanation length (idea + why_correct + when_changes + rule,
  excluding the clues/comparison tables) should be roughly 150-250 words —
  same depth as `data_batch1.py`, not shorter. Don't pad, but don't
  skeleton it either.
- Every wrong option needs its own real, specific reason tied to this
  patient/scenario — never a generic "غلط" or a reason copy-pasted across
  options.

## Deliverable

Create exactly one new file: the module name you were given in the task
prompt (e.g. `scripts/data_batchN.py`), following the exact shape of
`scripts/data_batch1.py`:

```python
TOPICS = {14: "Infectious Diseases", 15: "Infectious Diseases", ...}
EXPLANATIONS = {14: {...}, 15: {...}, ...}
WHY_WRONG = {14: {...}, ...}
HIGHLIGHT_TERMS = {14: [...], ...}
```

Cover **every** question number in your assigned range, with no gaps.
Before finishing, run (from the repo root `/home/user/salmas`):

```
python3 scripts/validate_batch.py data_batchN
```

(replace `data_batchN` with your actual module name) and fix every ERROR
it reports. Warnings about length are fine to leave if you're confident the
content is complete. Do not modify any other file in the repository.
