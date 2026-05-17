Add Obsidian-style wikilinks to a translated Marethar file.

## Usage

```
/wikilinks en/part2/04_geography.md
```

## What this command does

1. Reads `GLOSSARY.md` to get the full canonical list of proper nouns (nations, cities, peoples, etc.).
2. Reads the target file.
3. For each glossary term that appears in the file, wraps the **first occurrence per section** (between `---` or heading boundaries) in `[[...]]`.
   - Exact match on the English form from the GLOSSARY.
   - Do not link terms that are already inside `[[...]]`.
   - Do not link terms inside code blocks, blockquotes used as table data, or YAML frontmatter.
   - Use `[[Term]]` for direct matches; use `[[Term|Display text]]` only when the text in the file is a grammatical variant (e.g. "Premian" → `[[Republic of Premia|Premian]]`).
4. Writes the modified file in place.
5. Reports: how many links were added, which terms were linked, and any terms found in the file that are **missing from** GLOSSARY (flag these for glossary update).

## Rules

- Link the first occurrence per section only — not every occurrence. Over-linking clutters the graph.
- Never link generic English words even if they appear in the glossary (e.g. "culture", "empire" as common nouns).
- Proper nouns only: city names, nation names, people names, cult names, artifact names, religion names.
- Do not reorder or reformat any prose — only insert `[[` and `]]` around existing text.
- After finishing, if any new entity names were found that aren't in GLOSSARY, append them to `GLOSSARY.md` under the appropriate section with a `— TO VERIFY` note.

## Wikilink targets — post-atomization structure

Named entities now have **individual pages**. Always prefer the specific entity page over the section hub.

### Individual entity pages (use these directly)

**Cultures** — link to the culture's own page:
| Display text | Link |
|---|---|
| Aridonians / Aridonian | `[[Aridonians]]` / `[[Aridonians\|Aridonian]]` |
| Aurelians / Aurelian | `[[Aurelians]]` / `[[Aurelians\|Aurelian]]` |
| Lysandrians / Lysandrian | `[[Lysandrians]]` / `[[Lysandrians\|Lysandrian]]` |
| Orethians / Orethian | `[[Orethians]]` / `[[Orethians\|Orethian]]` |
| Thalassians / Thalassian | `[[Thalassians]]` / `[[Thalassians\|Thalassian]]` |
| Naharim | `[[Naharim]]` |
| Rashians / Rashian | `[[Rashian Empire\|Rashian]]` (no separate culture page) |

**Nations** — link to the nation's own page:
| Display text | Link |
|---|---|
| Republic of Premia / Premia / Premian | `[[Republic of Premia]]` / `[[Republic of Premia\|Premia]]` / `[[Republic of Premia\|Premian]]` |
| Diarchy of Ashania / Ashania / Ashanian | `[[Diarchy of Ashania]]` / `[[Diarchy of Ashania\|Ashania]]` |
| Empire of Linia / Linia | `[[Empire of Linia]]` / `[[Empire of Linia\|Linia]]` |
| Republic of Meshdad / Meshdad | `[[Republic of Meshdad]]` / `[[Republic of Meshdad\|Meshdad]]` |
| Grand Duchy of Hamania / Hamania | `[[Grand Duchy of Hamania]]` / `[[Grand Duchy of Hamania\|Hamania]]` |
| City-State of Allasia / Allasia | `[[City-State of Allasia]]` / `[[City-State of Allasia\|Allasia]]` |
| Rashian Empire / Rashia | `[[Rashian Empire]]` / `[[Rashian Empire\|Rashia]]` |
| Kingdom of Vallan / Vallan | `[[Kingdom of Vallan]]` / `[[Kingdom of Vallan\|Vallan]]` |
| Empire of Doria / Doria | `[[Empire of Doria]]` / `[[Empire of Doria\|Doria]]` |
| Principality of Dajilia / Dajilia | `[[Principality of Dajilia]]` / `[[Principality of Dajilia\|Dajilia]]` |
| Rhithian League / Rhithia | `[[Rhithian League]]` / `[[Rhithian League\|Rhithia]]` |

**Religions** — link to the religion's own page:
| Display text | Link |
|---|---|
| Sect of Shahin / Shahin / Tree Sect | `[[Sect of Shahin]]` / `[[Sect of Shahin\|Shahin]]` |
| Faith of Shemshahva / Shemshahva | `[[Faith of Shemshahva]]` / `[[Faith of Shemshahva\|Shemshahva]]` |
| Cult of Carthara / Carthara | `[[Cult of Carthara]]` / `[[Cult of Carthara\|Carthara]]` |
| Golat Tradition / Golat | `[[Golat Tradition]]` / `[[Golat Tradition\|Golat]]` |
| Gods of Ralertis / Ralertis | `[[Gods of Ralertis]]` / `[[Gods of Ralertis\|Ralertis]]` |
| Spirits of Thalaran / Thalaran | `[[Spirits of Thalaran]]` / `[[Spirits of Thalaran\|Thalaran]]` |
| Druidic Orders of Dimilalica / Dimilalica | `[[Druidic Orders of Dimilalica]]` / `[[Druidic Orders of Dimilalica\|Dimilalica]]` |
| Marethan Atheism | `[[Marethan Atheism]]` |
| Faith of Pulbium / Pulbium | `[[Faith of Pulbium]]` / `[[Faith of Pulbium\|Pulbium]]` |
| Faith of Tudeshkhast / Tudeshkhast | `[[Faith of Tudeshkhast]]` / `[[Faith of Tudeshkhast\|Tudeshkhast]]` |
| Sect of the Victory Bull | `[[Sect of the Victory Bull]]` |

**Relics** — link to the relic's own page:
| Display text | Link |
|---|---|
| Crown of Shahin | `[[The Crown of Shahin]]` |
| Sword of Ser Athelstan | `[[The Sword of Ser Athelstan]]` |
| Flame of Ralertis | `[[The Flame of Ralertis]]` |
| Mirror of Carthara | `[[The Mirror of Carthara]]` |
| Amulet of Shahin | `[[The Amulet of Shahin]]` |
| Wanderer's Compass | `[[The Wanderer's Compass]]` |
| Book of the Second Life | `[[The Book of the Second Life]]` |
| Imperial Seal / Lost Imperial Seal | `[[The Lost Imperial Seal]]` |

### Section hub pages (use when no individual entity page exists)

| Content | Link target |
|---------|-------------|
| Cultures overview | `[[Cultures of Marethar]]` |
| Religions overview | `[[Religions and Beliefs]]` |
| Nations overview | `[[The Great Nations]]` |
| Bestiary | `[[Bestiary]]` |
| Relics overview | `[[Lost Objects, Relics, Artifacts]]` |
| Organizations / Guilds | `[[Guilds, Orders, and Academies]]` |
| Chronology | `[[Chronology]]` |
| Geography | `[[Geography]]` |
| Magic | `[[Magic, Alchemy, Knowledge]]` |
| Notable Characters | `[[Notable Characters]]` |
| Myths | `[[Myths]]` |
| Flora & Fauna | `[[Flora & Fauna]]` |

### Cities — no individual pages; link to the nation page

| City | Link |
|------|------|
| Preiacoria, Livia, Aurelinum | `[[Republic of Premia\|Preiacoria]]` etc. |
| Marnorum, Corvalis, Lutria | `[[Empire of Linia\|Marnorum]]` etc. |
| Durtus, Mirath, Elaranor | `[[Diarchy of Ashania\|Durtus]]` etc. |
| Fahya | `[[Republic of Meshdad\|Fahya]]` (major knowledge hub) |
| Nabad | `[[Principality of Dajilia\|Nabad]]` |
| Lysandria (city) | `[[Lysandrians\|Lysandria]]` |
