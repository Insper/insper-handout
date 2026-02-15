function Div(el)
  if not el.classes:includes("notes") then
    return nil
  end

  -- Count the number of \newcolumn
  local count = 0
  for _, block in ipairs(el.content or {}) do
    if block.t == "RawBlock" and block.text:find("newcolumn") then
      count = count + 1
    elseif block.t == "Para" and block.inlines then
      for _, inline in ipairs(block.inlines) do
        if inline.text and inline.text:find("newcolumn") then
          count = count + 1
        end
      end
    end
  end

  local n = count + 1
  local width = n == 2 and "0.48\\linewidth" or string.format("%.3f\\linewidth", 0.98 / n)
  local switch = "\\end{minipage}\\hfill\\begin{minipage}[t]{" .. width .. "}"

  -- Function to process blocks
  local function process_block(block)
    if block.t == "RawBlock" and block.text:find("\\newcolumn") then
      return pandoc.RawBlock("latex", switch)
    elseif block.t == "Para" and block.inlines then
      local new_inlines = {}
      for _, inline in ipairs(block.inlines) do
        if inline.text and inline.text:find("\\newcolumn") then
          table.insert(new_inlines, pandoc.RawInline("latex", switch))
        else
          table.insert(new_inlines, inline)
        end
      end
      return pandoc.Para(new_inlines)
    else
      return block
    end
  end

  local processed_blocks = {}
  for _, block in ipairs(el.content or {}) do
    table.insert(processed_blocks, process_block(block))
  end

  local blocks = {}
  table.insert(blocks, pandoc.RawBlock("latex", "\\begin{notes}"))
  table.insert(blocks, pandoc.RawBlock("latex", "\\noindent"))
  table.insert(blocks, pandoc.RawBlock("latex", "\\begin{minipage}[t]{" .. width .. "}"))
  for _, b in ipairs(processed_blocks) do
    table.insert(blocks, b)
  end
  table.insert(blocks, pandoc.RawBlock("latex", "\\end{minipage}"))
  table.insert(blocks, pandoc.RawBlock("latex", "\\end{notes}"))

  return blocks
end
