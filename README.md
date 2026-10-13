# GBBRPM Three-Chapter Research Proposal

This project incorporates the October 12, 2026 consultation and the additional
request to distinguish the **GBBRPM evaluation engine** from the mathematical
model. The title retains cross-domain emphasis and explicitly limits the proposed
core to **directed acyclic graphs**.

Build **main.tex**. Its main chapter sequence is Chapters I–III, followed by
references and Appendices A–E. **main.pdf** is the compiled proposal.

## Integrated member additions

The preliminary pages, updated prototype passages, and provisional timeline
chart have been merged into the latest research draft. See
**docs/MEMBER_INTEGRATION_REVIEW.md** for corrections and evidence boundaries.
The current proposal includes a pending approval-sheet layout and an
acknowledgement placeholder, with the abstract still pending final results.
The approval page does not assert acceptance or supply invented signatures.
Prototype revision reports were supplied
by the team, not independently executed during this manuscript pass; the reported
positive-infinity validation defect and manual browser inspection remain open.
The 24-week core calendar is provisional, with conditional dissemination shown
separately beyond the core period.

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
- Appendix E: supporting prototype trace/replay contract and planned functional
  verification, separate from completed preliminary evidence.

## Latest full-paper review

The preliminary pages use compact contents/list spacing based on the supplied
proposal examples. The full chapter heading hierarchy remains visible; no body
sections were deleted to shorten the contents. The earlier preliminary
adjustment replaced the abstract with a placeholder and added a small gap
between contents entries. The approval sheet and acknowledgement have since
been restored; see **docs/PRELIM_RESTORATION_NOTES.md**. Appendix labels in
the contents are shortened; full titles remain in the appendices.
Chapter III retains a concise prototype description and verification summary;
implementation-level replay details appear in Appendix E. The timeline uses the
manuscript's navy/gray style and explicitly marks the W8 data review and protocol
freeze. See **docs/FULL_PAPER_PASS_NOTES.md** for the review scope and changes.

## Completed work versus planned work

The core mathematical equations and retained preliminary numerical results are
unchanged. The prior-art pass explicitly credits the established
probabilistic-sum t-conorm and compares close leaky noisy-OR and RIPA
precedents. The revised proposal adds planned bounded-aggregation and structural comparison, separated
runtime and memory measurement, explicit cutoff-tie reporting, and reviewed
input-validation conventions. These additions are proposed methods, not newly
executed tests. See **docs/PROPOSAL_REVISION_NOTES.md** for decisions and
remaining confirmations. See **docs/PRIOR_ART_REVISION_NOTES.md** for
the narrowed research question, verified sources, and planned aggregator
comparison. The new aggregation variants have not been executed by this pass.

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

### Preliminary PDF form and `pdflscape.sty`

The current proposal includes a draft approval page and loads `pdfpages` so
an official first-page PDF at `preliminary/FM-USTP-ACAD-11.pdf` can replace
the draft layout. It does not load `pdflscape` or require landscape pages.
Use only the updated approved institutional form once it is supplied; do
not treat the draft layout as signed approval.

After replacing an older merged source, clean its local build cache and rebuild:

```powershell
latexmk -c main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Build from the extracted project folder. Do not merge generated `.aux`, `.fls`,
`.fdb_latexmk`, or `.log` files from someone else's machine into the source.

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

## Focused reference-evaluation revision

The proposal now makes receiving-state reference accuracy, shared-origin dependence,
and accuracy--cost tradeoffs the primary controlled research questions. The new
`chapters/reference_benchmark.tex` specifies exact and Monte Carlo reference solvers,
560 matched branch scenarios, 3600 generated-DAG scenarios across three families,
and 12 prospective Express-topology scenarios, task-matched aggregation
and recursion comparisons, a prospective ancestry-aware diagnostic, and exactly-k
selection metrics. All are planned work; the full benchmark and diagnostic have not
been implemented or executed in this revision. See
`docs/SCIENTIFIC_FOCUS_REVISION.md` for the contribution argument and execution order.
Core equations, preliminary results, and the timeline are preserved.

## Benchmark bound and expanded protocol

`chapters/benchmark_bound.tex` proves the conditional nodewise bracket
recursive maximum <= restricted-tree reference <= cascade marginal <= GBBRPM
<= recursive clipped sum.
It is grounded in established positive association and aggregation arguments,
not claimed as a first result. `chapters/cascade_prior_art.tex` distinguishes
Abbe--Kulkarni--Lee bounds, MIA, LDAG, and the ancestry-overlap diagnostic.
The model remains a domain comparative index; only the separately specified
synthetic benchmark assigns probabilistic meanings to the supplied numbers.

The expanded protocol uses low weights, 20 evaluation graphs plus five development
graphs per family/size, a restricted-tree comparator, and 48 preselected precision
audits. Express raw topology files are absent from this manuscript package;
their recovery or reacquisition is an explicit prerequisite for the conditional
Express case, not an executed result. If the snapshot and provenance checks
are incomplete at the week-8 freeze, that case leaves the frozen inventory
without delaying the controlled graph benchmark.
See `docs/BOUND_AND_PROTOCOL_REVISION.md` for changes and current experiment counts.
The full benchmark is still planned; only algebraic and small-graph proof checks
were performed during authoring.

## Tree bracket and prototype focus refinement

The restricted tree preserves a maximum-weight path from every positive-path
ancestor without thresholding. This gives the tighter conditional certificate
`0 <= R - pi <= R - T <= R - M` when the target-specific tree is computed;
constructing those trees incurs extra cost. Planned ranking analysis now
reports strict reversals, Monte Carlo interval-resolved reversals and the
number of unresolved pairs. Clipped addition remains a measured comparator:
a looser score bound does not determine ranking quality. Section 3.4.2 and
Appendix E have been shortened to keep replay and animation supporting the
scientific benchmark. See `docs/TREE_BRACKET_REFINEMENT_NOTES.md`. These are
proposal refinements; no new benchmark outcomes or prototype tests are claimed.

## Computational and literature follow-up

The prospective protocol now specifies a development-only compute pilot and
records 75.6 billion potential edge-trial checks for the 3600 generated-DAG
references under direct edge-by-edge execution, plus 10.08 billion for the
48 extra precision solves. It adds a separate 144-scenario heterogeneous
weight subset paired with existing uniform-0.20 graphs. This subset adds
3.024 billion potential checks and has 24 development and 120 evaluation
scenarios. No measured runtime or new study outcome is claimed. The 2020
JMLR extension by Abbe, Kulkarni, and Lee is now cited and compared at the
nodewise-equation and DAG lower-bound levels. Its published DAG lower
recursion is also specified as a planned matched comparator after an
auxiliary-source transformation; uniqueness of the bracket is not claimed.
Appendix E prioritizes finite-number validation and a
demonstration check ahead of replay polish. See
`docs/REVIEW_PROTOCOL_FOLLOWUP.md` for exact conditions and work status.

## Chapter 1 opening and alignment revision

Chapter 1 now starts with general network-state assessment, mechanism choices,
and shared ancestry. It introduces GBBRPM and its controlled evaluation before
placing drainage as the original motivation and a supporting instantiation.
The problem statement leads directly with the mechanism-selection question,
and practical significance describes the three cases without making drainage
the main research subject. Research questions, objectives, equations, title,
Chapter 3 protocols, historical evidence, and the provisional timeline are retained.
Chapter 2 has a short bridge explaining its existing domain-first review order.
See `docs/CHAPTER1_REFOCUS_NOTES.md`.
