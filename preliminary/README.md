# Current proposal preliminaries

The compiled proposal includes the title page, a pending approval-sheet page,
an author-text acknowledgement placeholder, table of contents, lists of
tables/figures/equations, acronyms, and an abstract placeholder.

The approval and acknowledgement source layouts were restored at the authors'
request. The previous draft abstract remains archived and is not compiled.
The approval page is not an institutional approval. If the approved signed
FM-USTP-ACAD-11 first-page PDF is supplied, put it at the path in
`approval_sheet.tex`; that route will replace the text placeholder.

The title is counted as Roman page i with its number hidden; the approval
page is ii with its number hidden. The acknowledgement begins at iii and
contents follows. Body numbering restarts at Arabic 1. The contents retains
all heading levels, with a small gap
between entries and shortened appendix labels. Body tables and the other
preliminary lists retain the previous spacing.

The build loads pdfpages for the conditional institutional form and does not
load pdflscape.

Build main.tex with latexmk. Equation descriptions and PDF destinations remain
automatic through setup.tex and equation_descriptions.tex.
