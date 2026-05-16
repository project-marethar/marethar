---
name: next
description: Find the next untranslated Marethar file and translate it. Use when the user says "next", "translate next", or wants to continue where translation left off.
allowed-tools:
  - Read
  - Write
  - Edit
---

Find the next untranslated file and translate it.

## Steps

1. Read `PROGRESS.md` and find the first file whose status is `[ ]` (pending).
2. In `PROGRESS.md`, mark it `[~]` (in progress).
3. Read `GLOSSARY.md` — use it for every proper noun; never invent an English rendering mid-file.
4. Read the source file at `ambientazione/<file>`.
5. Translate the full file following all guidelines in `CLAUDE.md`:
   - Prioritize atmospheric resonance over literal accuracy.
   - Preserve section glyphs, Markdown heading levels, and the "circles of information" structure.
   - Render poetic hooks, proverbs, and marginalia as stylized fragments — not flattened prose.
   - Sensory location intros ("Se chiudi gli occhi…"): keep present-tense, second-person, taut.
   - Archival/ritual/censored notes: preserve the framing device label in English.
   - Do not translate license blocks or © notices.
6. Write the English output to `en/<path>` where `<path>` is the file path with `parte` replaced by `part`.
   - Example: `parte3/01_bestiario.md` → `en/part3/01_bestiario.md`
7. In `PROGRESS.md`, change the file's status from `[~]` to `[x]` and increment the "Complete" counter.

## After translating

Output a short summary (one paragraph) of the main choices made, plus a list of any new proper nouns or terms that should be added to `GLOSSARY.md`.
