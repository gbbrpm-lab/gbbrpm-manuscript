# Current Preliminary-Page Source Configuration

Checked against `preliminary.tex` and `../main.tex` on 15 October 2026. This describes source inclusion, not a newly rendered PDF.

The active sequence is title, contents, lists of tables/figures/equations, and acronyms, followed by Arabic body numbering. Approval, acknowledgement, and abstract files are present but **not included** by `preliminary.tex`. Their text and placeholders therefore do not establish the current compiled page order. Earlier restoration/integration notes describe previous passes.

Roman numbering begins before the title. `setup.tex` controls preliminary styles and equation destinations; `metadata.tex` holds title/author/degree and provisional submission fields. Do not infer imaginary approval-page numbering from an older README.

`../main.tex` currently loads `pdfpages` unconditionally. The official-form insertion route in the inactive approval source is not proof that the root loads it conditionally. If a local installation reports a missing indirect dependency such as pdflscape, handle that as a separate toolchain/source repair. No such repair is performed here.

Confirm the intended proposal/submission front matter, names, institutional form, signatories, date, and exact font before including or finalizing those pages. Build `../main.tex` from the project root. This documentation update leaves all LaTeX files and the uploaded PDF unchanged.
