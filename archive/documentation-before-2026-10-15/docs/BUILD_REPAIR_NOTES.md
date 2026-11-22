# LaTeX build repair — 13 October 2026

The uploaded source files match the previously delivered integrated proposal.
The differences were generated Windows build files and the absent main.pdf;
no source merge conflict was found.

The supplied MiKTeX log shows pdfpages loading successfully, then a fatal
missing pdflscape.sty error at begin-document. The installed pdfpages source
confirms that it requests pdflscape in its begin-document hook. The current
proposal uses a text placeholder for its pending official approval sheet, so
loading that optional PDF-insertion package was unnecessary.

main.tex now loads pdfpages only if preliminary/FM-USTP-ACAD-11.pdf exists.
The existing placeholder and future official-sheet insertion logic are retained.
When the official form is supplied later, the TeX installation must provide
pdfpages and its dependencies, including pdflscape.

The proposal chapters, equations, preliminary evidence, prototype sections,
and timeline are unchanged by this repair. Generated build-cache files from
the uploaded Windows project are excluded from the corrected delivery.

The corrected source was compiled from a clean output directory. The default
draft build does not load pdfpages or pdflscape. The rebuilt PDF is included
with the editable source. README.md includes cache-cleaning and rebuild commands.
