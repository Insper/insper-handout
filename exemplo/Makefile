# Produce PDFs from all Markdown files in a directory
# Lincoln Mullen | http://lincolnmullen.com | lincoln@lincolnmullen.com

## Markdown Template
TEMP-PWD =/home/corsi/Dropbox/Insper/Markdown
TEMP-TEXT = $(TEMP-PWD)/InsperTemplate.tex
TEMP-SLIDE = $(TEMP-PWD)/InsperTemplateSlide.tex
TEMP-FILTER = $(TEMP-PWD)/filterBox.py
LOGO = $(TEMP-PWD)/logo.pdf


# List files to be made by finding all *.md files and appending .pdf
PDFS := $(patsubst %.md,%.md.pdf,$(wildcard *.md))

TEX := $(patsubst %.md,%.md.tex,$(wildcard *.md))

# The all rule makes all the PDF files listed
all : $(PDFS)

tex : $(TEX)

# This generic rule accepts PDF targets with corresponding Markdown
# source, and makes them using pandoc
%.md.pdf : %.md
	pandoc --template=$(TEMP-TEXT) $< --variable logo=$(LOGO) -f markdown --filter pandoc-latex-tip --filter $(TEMP-FILTER) --pdf-engine=xelatex	-o $@
# This generic rule accepts PDF targets with corresponding Markdown

%.md.tex : %.md
	pandoc --template=$(TEMP-TEXT) $< --variable logo=$(LOGO) -f markdown --filter pandoc-latex-tip --filter $(TEMP-FILTER) -o $@
# This generic rule accepts PDF targets with corresponding Markdown

# Remove all PDF outputs
clean :
	rm $(PDFS)

# Remove all PDF outputs then build them again
rebuild : clean all



