-- strip_wikilinks.lua
-- Pandoc Lua filter: converts Obsidian-style wikilinks to plain text.
--   [[Page Name]]           → Page Name
--   [[Page Name|Display]]   → Display

local function process_inlines(inlines)
  local result = {}
  local i = 1
  while i <= #inlines do
    local el = inlines[i]
    -- Wikilinks appear as a sequence of Str/Space tokens: "[", "[", ..., "]", "]"
    -- Pandoc tokenises "[[Foo]]" as Str("[[Foo]]") in most cases, but
    -- when the content has spaces it may split differently.
    -- Safest: stringify the whole inline list and post-process.
    table.insert(result, el)
    i = i + 1
  end
  return result
end

-- Walk every paragraph/block and strip [[...]] patterns from the raw string.
local function strip(s)
  -- [[Page|Display]] → Display
  s = s:gsub("%[%[([^%]|]+)|([^%]]+)%]%]", "%2")
  -- [[Page]] → Page
  s = s:gsub("%[%[([^%]]+)%]%]", "%1")
  return s
end

function Str(el)
  local new = strip(el.text)
  if new ~= el.text then
    return pandoc.Str(new)
  end
end

-- Handle raw strings that Pandoc sometimes keeps as a single Str token
-- containing the whole wikilink (common when no spaces inside).
-- The Str walker above covers that case.

-- For wikilinks that span multiple tokens (spaces inside the link text),
-- we walk the full inline list of each block element.
local function walk_inlines(ils)
  local buf = pandoc.utils.stringify(pandoc.Inlines(ils))
  local stripped = strip(buf)
  if stripped == buf then
    return nil  -- no change needed
  end
  -- Re-parse the stripped string as plain inlines
  local doc = pandoc.read(stripped, "markdown")
  local new_inlines = {}
  for _, block in ipairs(doc.blocks) do
    if block.t == "Para" or block.t == "Plain" then
      for _, il in ipairs(block.content) do
        table.insert(new_inlines, il)
      end
    end
  end
  return new_inlines
end

function Para(el)
  local new = walk_inlines(el.content)
  if new then return pandoc.Para(new) end
end

function Plain(el)
  local new = walk_inlines(el.content)
  if new then return pandoc.Plain(new) end
end

function Header(el)
  local new = walk_inlines(el.content)
  if new then return pandoc.Header(el.level, new, el.attr) end
end
