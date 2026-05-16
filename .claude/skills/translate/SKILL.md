---
name: translate
description: Translate a single Marethar source file from Italian to English. Use when the user names a specific file to translate (e.g. "translate parte2/02_culture.md").
arguments:
  - file
allowed-tools:
  - Read
  - Write
  - Edit
---

Translate the Italian source file `ambientazione/$file` to English.

## Steps

1. Read `GLOSSARY.md` — use it for every proper noun; never invent an English rendering mid-file.
2. Read `ambientazione/$file`.
3. Translate the full file following all guidelines in `CLAUDE.md`:
   - Prioritize atmospheric resonance over literal accuracy.
   - Preserve section glyphs, Markdown heading levels, and the "circles of information" structure.
   - Render poetic hooks, proverbs, and marginalia as stylized fragments — not flattened prose.
   - Sensory location intros ("Se chiudi gli occhi…"): keep present-tense, second-person, taut.
   - Archival/ritual/censored notes: preserve the framing device label in English.
   - Do not translate license blocks or © notices.
4. Write the English output to `en/<path>` where `<path>` is `$file` with `parte` replaced by `part`.
   - Example: `parte2/02_culture.md` → `en/part2/02_culture.md`
5. In `PROGRESS.md`, mark the file `[x]` and increment the "Complete" counter.

## After translating

Output a short summary (one paragraph) of the main choices made: idioms resolved, proverbs adapted, any terms not yet in `GLOSSARY.md` that should be added.
