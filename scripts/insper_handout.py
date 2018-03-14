#!/usr/bin/env python

from pathlib import Path
import subprocess
import sys
import os.path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: insper_handout handout.md')
        sys.exit(-1)

    full_name = sys.argv[1]
    name = os.path.splitext(full_name)[0]
    script_home = os.path.join(Path.home(), '.insper_handout') 

    cmd_line = 'pandoc -f markdown+tex_math_double_backslash -t latex -o %s.pdf %s --data-dir=%s --filter include.py --filter filterBox.py --variable logo=%s/logo.pdf --variable header=%s/cabecalho.png --template %s/InsperTemplate.tex'%(name, full_name, script_home, script_home, script_home, script_home )
    
    print(cmd_line)
    res = subprocess.run(cmd_line.split())
