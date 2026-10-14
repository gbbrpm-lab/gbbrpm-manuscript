# Current proposal preliminaries

The compiled proposal includes the title page, table of contents, lists of
tables/figures/equations, and acronyms. The approval sheet, acknowledgement,
and abstract source files remain available but are not included in the build.

The title is counted as Roman page i with its number hidden. Contents follows
the title; body numbering restarts at Arabic 1. The contents retains all
heading levels, with a small gap
between entries and shortened appendix labels. Body tables and the other
preliminary lists retain the previous spacing.

Build main.tex with latexmk. Equation descriptions and PDF destinations remain
automatic through setup.tex and equation_descriptions.tex.
