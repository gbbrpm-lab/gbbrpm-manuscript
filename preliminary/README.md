# Preliminary pages

Everything before Chapter I, formatted to the CITC Manuscript Guidelines (2nd ed.), Article 3 and Article 8.

| File | Page | Guideline |
|---|---|---|
| `metadata.tex` | Shared title, authors, degree, date, signatories | 3.2, 3.3 |
| `setup.tex` | Preamble: page styles, contents and list formatting, equation list | 3.5, 3.6, 8.1 |
| `preliminary.tex` | Master file: order and numbering | 3.1, 8.1 |
| `title_page.tex` | Title page (i, number hidden) | 3.2 |
| `approval_sheet.tex` | Approval sheet (ii, number hidden) | 3.3 |
| `acknowledgment.tex` | Acknowledgement | 3.4 |
| `contents.tex` | Table of contents | 3.5 |
| `list_of_tables.tex`, `list_of_figures.tex`, `list_of_equations.tex` | Lists | 3.6 |
| `acronyms.tex` | Acronyms and abbreviations | 3.7 |
| `abstract.tex` | Abstract and keywords | 3.8 |

Fill in first (red text is a placeholder): middle names, signatory names (`metadata.tex`), acknowledgement, abstract.

Approval sheet: print the official FM-USTP-ACAD-11, sign it, scan it as `FM-USTP-ACAD-11.pdf` in this folder, and the build uses the scan instead of the typeset stand-in.

Lists build automatically from captions. In `\eqtag{3-1}`, add a description with `\eqtag[Short description]{3-1}` to show it in the List of Equations.

Build with two or three `pdflatex main.tex` passes.
