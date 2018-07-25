#!/usr/bin/env python

from pathlib import Path
import subprocess
import sys
import os.path
import argparse

if __name__ == "__main__":
        
    parser = argparse.ArgumentParser(prog="Insper Handout")
    parser.add_argument('filename')
    parser.add_argument('--format', action='store', default='latex')
    parser.add_argument('--output', action='store', default=None)
    
    arguments = parser.parse_args()
    name = os.path.splitext(arguments.filename)[0]
    if not arguments.output is None:
        name = arguments.output

    script_home = os.path.join(Path.home(), '.insper_handout') 

    if arguments.format == 'latex':
        if name[-4:] != '.pdf':
            name += '.pdf'
        cmd_line = 'pandoc -f markdown+tex_math_double_backslash -t latex -o %s %s --data-dir=%s --filter include.py --filter filterBox.py --variable logo=%s/logo.pdf --variable header=%s/cabecalho.png --template %s/InsperTemplate.tex'%(name, arguments.filename, script_home, script_home, script_home, script_home )
    elif arguments.format == 'html':
        if name[-5:] != '.html':
            name += '.html'
        cmd_line = 'pandoc -f markdown+tex_math_double_backslash -s -o %s %s --data-dir=%s --filter include.py --filter filterBox.py --template %s/InsperTemplate.html'%(name, arguments.filename, script_home, script_home)
    else:
        print('Unknown format:', arguments.format)
        sys.exit(-1)
        
    res = subprocess.run(cmd_line.split())
