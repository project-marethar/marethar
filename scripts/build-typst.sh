#!/usr/bin/env bash
# Build a single Typst PDF from all chapters.
# Usage: bash scripts/build-typst.sh
# Output: _book/marethar.pdf (or _master.typ if --typst-only)

set -euo pipefail

MASTER="_master.qmd"

cat > "$MASTER" << 'FRONTMATTER'
---
title: "Marethar"
subtitle: "A Dark-Fantasy Gunpowder Setting"
author: "Roberto Bisceglie (Orizzonti GDR)"
date: "2026"
format:
  typst:
    toc: true
    toc-depth: 2
    number-sections: false
filters:
  - filters/strip_wikilinks.lua
---
FRONTMATTER

grep -E '^\s+- (index\.qmd|en/)' _quarto.yml \
  | sed 's/^\s*- //' \
  | while IFS= read -r file; do
      [[ -f "$file" ]] || continue
      printf '\n\n' >> "$MASTER"
      cat "$file" >> "$MASTER"
    done

quarto render "$MASTER" --to typst

rm -f "$MASTER"
