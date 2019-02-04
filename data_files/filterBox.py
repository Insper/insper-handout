#!/usr/bin/env python3

"""
Pandoc filter to convert divs with class="theorem" to LaTeX
theorem environments in LaTeX output, and to numbered theorems
in HTML output.
"""

from pandocfilters import toJSONFilter, RawBlock, Div

theoremcount = 0

def latex(x):
    return RawBlock('latex', x)

def html(x):
    return RawBlock('html', x)

def box(key, value, format, meta):
    if key == 'Div':
        [[ident, classes, kvs], contents] = value
        if "alert" in classes:
            if format == "latex":
                if ident == "":
                    label = ""
                else:
                    label = '\\label{' + ident + '}'
                return([latex('\\begin{boxAlert}' + label)] + contents +
                       [latex('\\end{boxAlert}')])
            elif format == "html" or format == "html5":
                global theoremcount
                theoremcount = theoremcount + 1
                newcontents = [html('<dt>Theorem ' + str(theoremcount) + '</dt>'),
                               html('<dd>')] + contents + [html('</dd>\n</dl>')]
                return Div([ident, classes, kvs], newcontents)
        elif "question" in classes:
                  if format == "latex":
                      if ident == "":
                          label = ""
                      else:
                          label = '\\label{' + ident + '}'
                      return([latex('\\begin{boxQuestion}' + label)] + contents +
                              [latex('\\end{boxQuestion}')])
        elif "box" in classes:
                  if format == "latex":
                      if ident == "":
                          label = ""
                      else:
                          label = '\\label{' + ident + '}'
                      return([latex('\\begin{tcolorbox}[arc=4mm,outer arc=1mm]' + label)] + contents +
                              [latex('\\end{tcolorbox}')])

if __name__ == "__main__":
  toJSONFilter(box)
