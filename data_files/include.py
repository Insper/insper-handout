import pandocfilters as pf
import sys

def get_attr_in_list(attrs, at):
    for (a, v) in attrs:
        if a == at:
            return v
    return None

def include_filter(k, v, f, m):
    if k == 'Div':
        [[ident, classes, attrs], content] = v
        if 'include' in classes:
            with open(ident, 'r') as f:
                content = f.read()
                if 'code' in classes:
                    return pf.CodeBlock((ident, [get_attr_in_list(attrs, 'language')], []), content)
                else:
                    return [pf.Para([pf.Str(content)])]

if __name__ == '__main__':
    pf.toJSONFilter(include_filter)