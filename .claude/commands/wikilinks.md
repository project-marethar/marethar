Add Obsidian-style wikilinks to a translated Marethar file.

## Usage

```
/wikilinks en/part2/05_nations.md
```

## What this command does

1. Reads `GLOSSARY.md` to get the full canonical list of proper nouns (nations, cities, peoples, etc.).
2. Reads the target file.
3. For each glossary term that appears in the file, wraps the **first occurrence per section** (between `---` or heading boundaries) in `[[...]]`.
   - Exact match on the English form from the GLOSSARY.
   - Do not link terms that are already inside `[[...]]`.
   - Do not link terms inside code blocks, blockquotes used as table data, or YAML frontmatter.
   - Use `[[Term]]` for direct matches; use `[[Term|Display text]]` only when the text in the file is a grammatical variant (e.g. "Premian" → `[[Republic of Premia|Premian]]`).
4. Also adds cross-section links where natural: if a nation is discussed in a culture file, link to the nations file; if a cult is mentioned in the daily life file, link to the religions file. Use the filename as the link target (e.g. `[[Nations]]`, `[[Religions and Beliefs]]`).
5. Writes the modified file in place.
6. Reports: how many links were added, which terms were linked, and any terms found in the file that are **missing from** GLOSSARY (flag these for glossary update).

## Rules

- Link the first occurrence per section only — not every occurrence. Over-linking clutters the graph.
- Never link generic English words even if they appear in the glossary (e.g. "culture", "empire" as common nouns).
- Proper nouns only: city names, nation names, people names, cult names, artifact names.
- Do not reorder or reformat any prose — only insert `[[` and `]]` around existing text.
- After finishing, if any new entity names were found that aren't in GLOSSARY, append them to `GLOSSARY.md` under the appropriate section with a `— TO VERIFY` note.

## Wikilink targets

All current section files exist in `en/` and are valid link targets. Quartz resolves links by filename stem. Use the stem (without extension) or the full title from the file's first `#` heading.

| Section | Link target |
|---------|-------------|
| Nations | `[[Nations]]` or specific nation name |
| Cultures | `[[Cultures of Marethar]]` |
| Religions | `[[Religions and Beliefs]]` |
| Bestiary | `[[Bestiary]]` |
| Relics | `[[Relics]]` |
| Notable Characters | `[[Notable Characters]]` |
| Organizations | `[[Organizations]]` |
| Chronology | `[[Chronology]]` |
| Geography | `[[Geography]]` |
| Magic | `[[Magic, Alchemy, and Knowledge]]` |
| Myths | `[[Myths]]` |

Individual named entities (specific nations, characters, cities) do not yet have their own pages — link to the section page that describes them, not to a non-existent entity page. Future Phase 3 work may split these out.
