## Instalação e uso

Para instalar execute:

```bash
$ sudo apt install texlive texlive-xetex texlive-pictures texlive-latex-extra pandoc python3-pandocfilters
$ pipx install pandoc-latex-tip
$ sudo pip install setuptools
$ pip install setuptools pandocfilters
$ sudo python3 setup.py install
$ python3 setup.py install
```

Ignore os warnings

Será instalado um script `insper_handout.py` na pasta de executáveis do python. Para usar basta rodar

```bash
$ insper_handout.py roteiro.md
```

Será gerado um arquivo `roteiro.pdf` com o resultado final da compilação do arquivo Markdown.

Além disto, são instalados arquivos de *template* em `~/.insper_handout`. Eles podem ser editados manualmente por sua própria conta e risco.

## Arquivos modelo instalados

- filterBox.py : filtro aplicado durante a conversão do doc de .md para .pdf para incluir caixas especiais no documento. 
- include.py: filtro para inclusão verbatim de arquivos e colorização de código fonte. 
- InsperTemplate.tex : Template latex utilizado pelo pandoc para a conversão de .md para .pdf
- logo.png e cabecalho.png : Imagens usadas na capa
