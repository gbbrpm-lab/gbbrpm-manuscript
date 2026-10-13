# Current proposal preliminaries

The compiled proposal includes the title page, table of contents, lists of
tables/figures/equations, acronyms, and an abstract placeholder.

The approval sheet and acknowledgement are omitted at the authors’ request.
Their earlier source layouts, together with the previous draft abstract, are
preserved in archive/preliminary/ and are not compiled.

The title is counted as Roman page i with its number hidden. Contents begins
at ii; body numbering restarts at Arabic 1. No blank pages are reserved for
omitted material. The contents retains all heading levels, with a small gap
between entries and shortened appendix labels. Body tables and the other
preliminary lists retain the previous spacing.

The current build does not load pdfpages or pdflscape. A future approved form
would require explicit source inclusion and its appropriate dependencies.

Build main.tex with latexmk. Equation descriptions and PDF destinations remain
automatic through setup.tex and equation_descriptions.tex.
