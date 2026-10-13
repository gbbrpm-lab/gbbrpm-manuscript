# GBBRPM Three-Chapter Research Proposal

This project incorporates the October 12, 2026 consultation and the additional
request to distinguish the **GBBRPM evaluation engine** from the mathematical
model. The title retains cross-domain emphasis and explicitly limits the proposed
core to **directed acyclic graphs**.

Build **main.tex**. Its main chapter sequence is Chapters I–III, followed by
references and Appendices A–D. **main.pdf** is the compiled proposal.

## Current structure

- Chapter I: model identity, problem and questions, aligned objectives,
  theoretical/practical significance, separate scope and limitations, framework,
  and operational definitions.
- Chapter II: source-based literature regrouped into a connected argument about
  local/structural assessment, state semantics, propagation mechanisms, ranking,
  computational/input tradeoffs, reusable formulations, and the research gap.
- Chapter III: design requirements and detailed formulation; evaluation-engine
  and prototype specification; domain data and mappings; controlled comparisons;
  property, sensitivity, robustness, dependence, and cost protocols; separate
  domain evaluation; verification, analysis, reproducibility, and timeline.
- Appendix A: generic worked example.
- Appendix B: preliminary software worked calculation.
- Appendix C: preliminary electrical worked calculation.
- Appendix D: selected preliminary evidence, including unfavorable hydraulic
  agreement and known dependence limitations.

## Completed work versus planned work

The core mathematical equations and retained preliminary numerical results are
unchanged. The revised proposal adds planned structural comparison, separated
runtime and memory measurement, explicit cutoff-tie reporting, and reviewed
input-validation conventions. These additions are proposed methods, not newly
executed tests. See **docs/PROPOSAL_REVISION_NOTES.md** for decisions and
remaining confirmations.

The schedule is provisional. W1 is anchored to October 12, 2026; official
proposal/final defense, submission, data-access, and dissemination dates remain
to be confirmed. Independent outcome evaluation remains conditional on suitable
agency or event-aligned records.

## Historical research record

**archive/full-study/main_preconsultation.pdf** and the original six chapter
sources preserve the previous full-study manuscript. Archived chapter sources
are reference copies, not the main compilation target. Prior study briefings and
old revision notes are historical context, not the current proposal plan.
Existing experiment scripts and generated tables preserve earlier reproducibility
assets; running them does not execute the newly proposed protocols automatically.

## Evidence boundaries

GBBRPM is a bounded, non-probabilistic comparative index. Cross-domain
instantiation does not make domain scores equivalent, establish a calibrated
failure probability, or validate hydraulic, exploitation, or electrical-event
prediction. The real software topology and measured electrical loading remain
real inputs; the associated experiments are preliminary and partly controlled.

## Requirements

### Windows

- [MiKTeX](https://miktex.org/download)
- [Strawberry Perl](https://strawberryperl.com/) for `latexmk`
- [VS Code](https://code.visualstudio.com/)
- [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)
- Python 3 with `matplotlib` and `pandas` only when regenerating historical plots

After installation, restart VS Code and verify the toolchain in PowerShell:

```powershell
perl --version
pdflatex --version
latexmk --version
```

## Build the manuscript

Open the project directory in VS Code and build `main.tex` with LaTeX Workshop, or run:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The generated document is `main.pdf`. `main.tex` is the root file.

Clean auxiliary build files with:

```powershell
latexmk -c
```

To verify reproducibility, clone the repository into a new directory and build it again without copying files from the original working directory.

## Project layout

```text
.
├── main.tex
├── ADVISER_BRIEFING_COMPONENT2.md  # Component 2 defense rationale and Q&A
├── archive/                  # Prior full-study PDF, chapter sources, and briefings
├── references.tex
├── chapters/                 # Proposal Chapters I–III
├── appendices/               # Worked calculations and preliminary evidence
├── figures/                  # Manuscript figures
│   └── paper/                # Cross-domain generated figures
├── tables/                   # Literature and manuscript tables
│   └── paper/                # Presentation-adjusted cross-domain tables
├── data/                     # Inputs used by included plotting scripts
├── results/
│   └── paper/                # Preserved generator outputs and manifest
├── scripts/                  # Included figure-regeneration scripts
└── REVISION_NOTES.md         # Revision scope and remaining limitations
```

## Regenerate historical figures

Install the plotting dependencies:

```powershell
python -m pip install matplotlib pandas
```

Regenerate the former Figures 4.2–4.5 from `data/core_scenarios.csv`:

```powershell
python scripts/generate_chapter4_figures.py
```

Regenerate the scalability figure:

```powershell
python scripts/generate_figure4_8.py
```

The cross-domain files under `figures/paper`, `tables/paper`, and `results/paper` are preserved outputs from separate reproducibility workflows. The Component 2 manuscript figures are derived from an authorized dataset extract; raw measurements and credentials are intentionally not included. Do not claim these files are regenerated by this manuscript package unless the corresponding authorized source datasets and generators are available.

## References and formatting

- In-text sources use LaTeX author–date citation commands through `natbib`.
- The reference list is organized alphabetically in APA-style presentation.
- `main.tex` applies the available CITC body requirements, including A4 paper, the binding margin, paragraph indentation, single spacing, chapter headings, caption placement, equation labels, and page-number positioning.
- Palatino is used as the closest installed TeX-compatible substitute for Book Antiqua. Confirm whether the exact proprietary font is required for final submission.
- Preliminary pages are intentionally incomplete because their official template and required approval information were not provided with the body-formatting guideline.

## Use with Overleaf

1. Download or create a ZIP containing the complete project directory.
2. In Overleaf, choose **New Project → Upload Project**.
3. Upload the ZIP.
4. Confirm that `main.tex` is selected as the main document.
5. Compile with pdfLaTeX.

Overleaf is optional; the Git repository remains the reproducible source of truth.

## Git guidance

Commit manuscript sources, scripts, input data required for regeneration, and final approved figures or tables. Do not commit LaTeX auxiliary files such as `.aux`, `.log`, `.fls`, `.fdb_latexmk`, `.out`, or `.synctex.gz`.

Before pushing a manuscript revision:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
git status
git add .
git commit -m "Update thesis manuscript"
git push
```

This workflow keeps equations native to LaTeX, makes chapter and section numbering automatic, preserves traceable cross-references and citations, and allows each manuscript revision to be reproduced from version-controlled sources.
