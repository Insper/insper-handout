from distutils.core import setup
from pathlib import Path
import os.path


setup(name='insper_handout' ,
      version='0.1',
      scripts=['scripts/insper_handout.py'],
      data_files=[(os.path.join(Path.home(), '.insper_handout'), 
                    ['data_files/InsperTemplate.tex', 
                     'data_files/InsperTemplate.html', 
                     'data_files/logo.pdf',
                     'data_files/cabecalho.png']),
                  (os.path.join(Path.home(), '.insper_handout/filters'),
                    ['data_files/include.py',
                     'data_files/pandoc-svg.py',
                     'data_files/filterBox.py']), ],
      py_modules=[]
    )
