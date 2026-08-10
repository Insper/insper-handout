## Instalação e uso

Instale primeiro as dependências de sistema:

```bash
$ sudo apt install texlive texlive-xetex texlive-pictures texlive-latex-extra pandoc python3-pandocfilters
```

Para instalar o `insper-handout` a partir deste repositório:

```bash
$ pipx install .
```

Durante desenvolvimento, use uma instalação editável:

```bash
$ python3 -m pip install -e .
```

Será instalado o comando `insper_handout.py` no ambiente Python. Para usar basta rodar:

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
