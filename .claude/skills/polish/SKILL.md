---
name: polish
description: AI prose polish pass on a translated Marethar file. Removes AI-formula language, em-dashes, and structural anti-patterns. Use after translating a file, e.g. "polish en/part2/02_culture.md".
arguments:
  - file
allowed-tools:
  - Read
  - Edit
  - Bash
---

Run a full prose-polish pass on `$file`. This file is a translated dark-fantasy RPG setting document. The goal is to remove AI-formula language that has crept into the translation while preserving the solemn, atmospheric, Mediterranean-flavored prose the setting demands.

## Step 1 — Read the file

Read `$file` in full before making any changes.

## Step 2 — Word-level replacements (Task 1)

Scan the entire document and replace the following. **Do not change legitimate uses** — e.g., "navigate" meaning literal sailing, "journey" meaning literal travel, "fluid" describing actual liquid.

| Find | Replace with |
|------|-------------|
| `navigate / navigating` (metaphorical only) | plain, specific language for what is actually happening |
| `journey` (metaphorical only) | plain statement of what happens |
| `immersive / immersion / immerse` | what the immersion actually means: "present in the fiction", "grounded", etc. |
| `fluid` (narrative/storytelling) | "quick", "smooth", or cut |
| `unfolding` (story/narrative) | "story" or cut |
| `weave` (metaphorical narrative use) | plain verb |
| `breathe life into` | cut or describe what specifically happens |
| `lean into` | the specific action it describes |
| `seamlessly` | cut |
| `one decision at a time` / `one choice at a time` | cut |
| `dive into` / `dive deeper` | "start", "read", "look at", etc. |
| `unlock its full potential` | what specifically becomes possible, or cut |
| `feels alive` / `world that feels alive` / `layered and alive` | what makes it specific or active |
| `genuine` as intensifier | cut the word |
| `[X] is where [Y] lives` | direct statement |
| `enjoy the journey` | cut or plain statement of purpose |
| `adapt to your vision` / `adapts to your vision` | what the system actually does |
| `deepen your [journey/connection/experience]` | what specifically changes |
| `rich and immersive` / `rich, immersive` | cut both adjectives, describe what is actually there |
| `tapestry` | always cut |
| `spotlight` (metaphor) | rephrase |
| `the stakes are real` | cut |
| `robust` (describing systems/design) | what it actually does |
| `powerful` (content-free intensifier) | what it specifically enables |
| `dynamic` (describing narrative or characters) | what changes and how |
| `vibrant` | almost always cut; describe what is actually there |
| `compelling` (filler for story/characters) | cut or describe the mechanism |
| `engaging` | describe the mechanism, not the effect |
| `meaningful` (generic closer) | what the choice or moment actually does |
| `authentic` (non-specific use) | cut or contrast with what it replaces |
| `nuanced` (without explanation) | explain the nuance or cut |
| `complex / complexity` (used as praise without elaboration) | cut or elaborate |
| `the rest is up to you` | always cut |
| `endless possibilities` / `the possibilities are endless` | always cut |
| `only your imagination limits` | cut |
| `and so much more` | cut |
| `at its core` | cut; start with the statement directly |
| `at the heart of [X] is Y` | rewrite as direct statement |
| `[X] ensures that [positive outcome]` | replace with how it actually works |
| `[X] allows you to [vague empowerment]` | replace with what the mechanic concretely does |
| em-dash `—` | comma, colon, or semicolon as appropriate |

**High-frequency words** (`dynamic`, `powerful`, `engaging`, `meaningful`, `authentic`, `ultimately`) appear too often to catch reliably by eye alone. After completing the table above, do a separate pass for each word and evaluate in context. Fix only the filler uses.

## Step 3 — Structural rewrites (Task 2)

These are **mandatory**. Find every instance and apply the fix. Do not leave any instance unchanged.

**Pattern A — "This isn't just X, it's Y" openers**
Find: Sentences opening with "This isn't just [X], it's [Y]", "It's not just...", "More than just...", "[X] is more than just [Y]".
Fix: Delete the meta-commentary. Open directly with the actual content.

**Pattern B — "Welcome to..." / "Think of this as..." openers**
Find: Section or paragraph openers using "Welcome to [X]" or "Think of this as [X]".
Fix: Delete the opener. Begin with the first substantive sentence.

**Pattern C — Closing summary sentences**
Find: Final sentences of sections that restate what was just said and label it meaningful, memorable, impactful, or similar.
Fix: Delete the sentence entirely.

**Pattern D — Trailing clauses on bullet points**
Find: Bullet points ending with "...making each moment feel meaningful and true to your character's journey", "...creating a more engaging and authentic experience", or similar positive-adjective finishers.
Fix: Cut the trailing clause at the comma or conjunction that introduces it. Keep only the functional part.

**Pattern E — Adjective-saturated paragraphs**
Find: Paragraphs where three or more sentences end with a positive adjective or adjective phrase ("authentic", "meaningful", "engaging", "compelling", "memorable", "rewarding", "dynamic", "vibrant").
Fix: Rewrite the paragraph. Remove at least half of those adjectives. Where an adjective was doing work, replace it with a concrete description.

**Pattern F — Rhetorical sweep sentences**
Find: "Whether [X] or [Y], [Z]" sentences gesturing at inclusivity; "from [X] to [Y], every [Z]" summary sentences.
Fix: Cut entirely or replace with a direct, specific statement about what the system or section actually does.

**Pattern G — "Above all" and "Ultimately" closers**
Find: Paragraphs or sections ending with a sentence opening "Above all," or "Ultimately,".
Fix: Delete the sentence. If it contains a specific point not made elsewhere, extract and integrate it as a plain statement in the paragraph body.

## Step 4 — Verification

Run both grep commands. Fix any remaining hits before finishing.

```bash
grep -in "navigate\|immersive\|immerse\b\|fluid\b\|lean into\|one decision at a time\|one choice at a time\|dive deeper\|dive into\|unlock its\|feels alive\|layered and alive\|deepen your\|seamlessly\|tapestry\|unfolding narrative\|weave.*story\|breathe life\|adapt.*vision\|enjoy the journey\|isn't just\|is not just\|more than just\|welcome to\|think of this as\|making each moment\|feel meaningful\|feel memorable\|feel impactful\|robust\|vibrant\|nuanced\|at its core\|at the heart of\|the rest is up to you\|endless possibilities\|only your imagination\|and so much more" "$file"
```

```bash
grep -in "whether you\|whether.*or.*you\|from.*to.*every\|allows you to\|ensures that\|above all,\|ultimately," "$file"
```

If either grep returns hits, fix them before proceeding.

## Step 5 — Report

Output a short summary: how many passages were revised, which patterns were most prevalent, and any cases where a change felt uncertain (so the author can review).

**Scope reminder:** This is a translated dark-fantasy RPG setting with a solemn, Mediterranean, historical tone. Do not add color, enthusiasm, or elaboration. Only remove or replace what is already there.
