# Produce PDFs from all Markdown files in a directory
# Lincoln Mullen | http://lincolnmullen.com | lincoln@lincolnmullen.com

## Markdown Template
PWD = /home/corsi/tmp/Corsi-Pandoc-Class-Handout
TEXT = $(PWD)/InsperTemplate.tex
SLIDE = $(PWD)/InsperTemplateSlide.tex
FILTER = $(PWD)/filterBox.py
GITHUB = $(PWD)/toGitHub.py
LOGO = $(PWD)/logo.pdf

# List files to be made by finding all *.md files and appending .pdf
PDFS := $(patsubst %.md,%.pdf,$(wildcard *.md))
MD   := $(patsubst %.md,%.gh,$(wildcard *.md))
TEX  := $(patsubst %.md,%.md.tex,$(wildcard *.md))

# The all rule makes all the PDF files listed
all : $(PDFS)
gh : $(MD)
tex : $(TEX)

# This generic rule accepts PDF targets with corresponding Markdown
# source, and makes them using pandoc
%.pdf : %.md
	pandoc $< --template=$(TEXT) --variable logo=$(LOGO) -f markdown --filter pandoc-latex-tip --filter $(FILTER) --pdf-engine=xelatex	-o $@

%.gh : %.md
	python $(GITHUB) -f $< -o $@

%.md.tex : %.md
	pandoc $< --template=$(TEXT) --variable logo=$(LOGO) -f markdown --filter pandoc-latex-tip --filter $(FILTER) -o $@

# Remove all PDF outputs
clean :
	rm $(PDFS)

# Remove all PDF outputs then build them again
rebuild : clean all



