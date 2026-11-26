# Approval sheet and acknowledgement restored

> Historical revision record. It describes the authoring pass below, not the current source configuration or newly reproduced tests. For current scope, evidence, inventory, and remaining work, use [CURRENT_PROPOSAL_STATUS.md](CURRENT_PROPOSAL_STATUS.md) and [NEXT_STEPS.md](NEXT_STEPS.md). Chapters I–III govern; the new benchmark remains planned. Earlier front-matter, page-count, compile, and test statements must not be read as current verification.

> Source check on 15 October 2026: `preliminary/preliminary.tex` currently omits approval, acknowledgement, and abstract pages; `main.tex` includes Appendices A–E and loads `pdfpages` unconditionally. Existing page-source files and an earlier restoration/repair report do not override those active includes. No LaTeX change is made by this note.

This note supersedes the preliminary-page omission described in
`PRELIMINARY_ADJUSTMENT_NOTES.md` for the current compilation. The authors
requested both pages back. The current order is title, approval sheet,
acknowledgement, table of contents, lists, acronyms, and abstract. The body
still starts at Arabic page 1, and the abstract remains a proposal placeholder.
The tested PDF has 85 physical pages, including 12 preliminary pages; the
contents occupies three pages. The restored pages added two physical pages
relative to the prior build, with the chapter text unchanged.

The attached CITC second-edition guidelines discuss the official updated
FM-USTP-ACAD-11 form in Section 3.3, acknowledgment layout in Section 3.4,
and imaginary Roman page numbers for the title and approval pages in Section
8.1. The PDF from the institution that is signed by the designated people
has not been provided. The compiled approval page is therefore marked as a
draft pending approval and does not assert acceptance or invent names,
signatures, or dates. The project will include the first page of
`preliminary/FM-USTP-ACAD-11.pdf` in its place if the official file is later
supplied. The source puts the contents entry on whichever page is used, and
the root loads `pdfpages` for that conditional route.

The restored acknowledgement contains a prompt for the authors' own words,
not an AI-written expression of thanks. The CITC guideline allows up to five
pages and calls for a centered uppercase heading, justified text, and no
figures. Only the one-page placeholder is present now. It and the official
approval form need author input before final submission.
