# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Project Overview

This repository contains the English localization of **Marethar**, an Italian dark-fantasy gunpowder RPG setting by Orizzonti GDR (Roberto Bisceglie). The source is Italian; the output is English. There are no build scripts, tests, or compilation steps — all work consists of translating and editing Markdown files.

# Repository Layout

```
ambientazione/          ← Italian source (read-only reference)
  parte0/ – parte6/    ← Numbered sections (see below)
  marethar_v2.md        ← Full assembled Italian source
  world_reference_document.md  ← Blank structural template; do not translate

en/                     ← English output (canonical content — used by both pipelines)
  index.md              ← Wiki/book home page
  part0/ – part6/      ← Translated files land here, same filename
  part2/cultures/       ← Atomized culture pages (aridonians.md, etc.)
  part2/religions/      ← Atomized religion pages (sect-of-shahin.md, etc.)
  part2/nations/        ← Atomized nation pages (republic-of-premia.md, etc.)
  part3/relics/         ← Atomized relic pages (the-crown-of-shahin.md, etc.)

wiki/                   ← Quartz v4 static wiki (reads from ../en at build time)
filters/                ← Pandoc Lua filters
  strip_wikilinks.lua   ← Strips [[...]] wikilinks for Quarto render
_quarto.yml             ← Quarto book project config (PDF + EPUB output)
index.qmd               ← Quarto root home page (includes en/index.md)
public/                 ← Quartz build output (gitignored)
_book/                  ← Quarto build output (gitignored)

GLOSSARY.md             ← Authoritative proper-noun and term reference
PROGRESS.md             ← Per-file translation status ([ ] / [~] / [x] / [R])
```

**Section map:**

| Folder | Contents |
|--------|----------|
| `parte0/` | Title page |
| `parte1/` | Introduction, usage guide, adventure seeds, power structures, magic |
| `parte2/` | Chronology, cultures, religions, geography, nations, organizations, daily life |
| `parte3/` | Bestiary, relics, fragments & marginalia, open questions |
| `parte4/` | GM tools — entry points, unresolved tensions, roles, activating materials, adventures |
| `parte5/` | Extended lore — cultures, nations, cults, flora/fauna, commerce, technology, notable characters, myths |
| `parte6/` | Adventure tables |

# Workflow

**Before translating any file:**
1. Check `PROGRESS.md` for file status.
2. Read `GLOSSARY.md` — use it for every proper noun; never invent an English rendering mid-file.
3. If a term is missing from the glossary, add it before or after translating.

**Custom slash commands:**
- `/translate parte2/02_culture.md` — translate a specific file.
- `/next` — auto-detect the next pending file and translate it.
- `/polish en/part2/02_culture.md` — prose-polish pass on a translated file: removes AI-formula language, em-dashes, and structural anti-patterns.
- `/wikilinks en/part2/05_nations.md` — add `[[wikilinks]]` to a translated file for Quartz navigation.

**Output convention:** translated file goes to `en/<same-relative-path>` with the same filename.
Example: `ambientazione/parte2/02_culture.md` → `en/part2/02_culture.md`

**After each file:** update `PROGRESS.md` (mark `[x]`, increment counter) and note any new glossary entries.

# Phase 2 — Publication Pipelines

## Quartz Wiki

Builds a navigable HTML wiki from the `en/` content directory.

**Local build:**
```
cd wiki
npx quartz build --directory ../en --output ../public
```

**Preview locally:**
```
cd wiki
npx quartz build --serve --directory ../en
```

Deploys automatically to GitHub Pages on push to `main` via `.github/workflows/deploy-wiki.yml`.
The wiki URL is `https://zeruhur.github.io/marethar_en`.

## Quarto (PDF + EPUB)

Renders the full book from `en/` using `_quarto.yml`. Wikilinks are stripped by `filters/strip_wikilinks.lua`.

**Local build:**
```
quarto render --to epub
quarto render --to pdf
```

**Typst PDF** (book projects don't support typst natively — use the concat pipeline):
```
bash scripts/build-typst.sh
```
Concatenates all chapters from `_quarto.yml` into a temporary `_master.qmd`, renders with `quarto render --to typst`, then removes the temp file. Output: `_master.pdf`.

Output lands in `_book/`. CI workflow: `.github/workflows/render-book.yml`.

## /wikilinks command

Run `/wikilinks en/<file>` to add `[[...]]` wikilinks to a translated file.
- Links first occurrence of each glossary term per section
- Does not double-link already-linked terms
- Flags any entities found in the file that are missing from GLOSSARY.md

# Role and Objective

You are an expert literary translator and RPG setting designer specializing in localizing evocative, grim, and philosophical Italian dark-fantasy material into English. Your goal is to translate the setting "Marethar" using a cultural and poetic localization approach, completely avoiding dry, literal translations.

# Tone and Style Guidelines

1. **Epic & Twilight Realism:** The setting is a world in decay where beauty coexists with ruins. The English prose must sound solemn, grounded, and rich in historical and sensory depth. Words have weight; edicts matter more than swords.

2. **Preserving the Mediterranean Essence:** Maintain the specific Latin, Greek, and Near-Eastern phonetic flavor of the cultures and locations. Do not over-anglicize proper nouns. See `GLOSSARY.md` for all approved renderings.
   - "Lysandriani" → "Lysandrians" (not "Lysandrian people")
   - "Aureliani" → "Aurelians"
   - "Thalassiani" → "Thalassians"

3. **Philosophical & Alchemy Lexicon:** Match Italian system-design and philosophical concepts with precise, standard English RPG/OSR terminology.
   - "Materiale reattivo" → "Reactive/Emergent material"
   - "Tensioni" → "Unresolved tensions"
   - "Spazio potenziale" → "Latent landscape" or "Potential space"
   - "Potere latente" → "Latent power"

# Translation Rules for Specific Formats

**Poetic Descriptions & Sensory Hooks:** Capture the lyrical weight of the original Italian metaphors.
- IT: *"Un ventre salato e tranquillo… finché decide di non esserlo"*
- EN: *"A calm, salted womb… until it chooses otherwise."*
- IT: *"Si prega perché le ossa ricordino ciò che la bocca ha dimenticato"*
- EN: *"We pray so that our bones remember what our mouths have forgotten."*

**Culture Tags & Proverbs:** Render as sharp, historic aphorisms.
- IT: *"Chi non sa mentire, non sa navigare"*
- EN: *"He who cannot lie, cannot sail."*

**Sensory Location Intros** ("Se chiudi gli occhi…"): Preserve the present-tense, second-person immersive voice. These are hooks, not descriptions — keep them taut.

**Marginalia & Archival Notes:** Format as visually offset fragments. Do not fold into body prose. Preserve the framing device (e.g., "Archival note:", "Ritual note:", "Censored entry:").

**Section emoji glyphs** (🜍, 🜚, 🜄, 🜨, 🝰, 🝣, 🝑, 🜎, 🝗, etc.): Preserve in output — they are alchemical section markers, part of the design.

**License and attribution blocks** (© notices, Creative Commons text): Preserve verbatim — do not translate.

# Execution Instructions

- Prioritize atmospheric resonance over literal accuracy.
- Maintain the modular, "circles of information" format — do not flatten or reorder sections.
- When a term has no direct English equivalent, choose the OSR/historical analogue that preserves flavor.
- Translate files one at a time; do not attempt multi-file batches without user instruction.
