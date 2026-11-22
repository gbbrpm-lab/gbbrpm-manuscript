# GBBRPM Three-Chapter Research Proposal

This uploaded manuscript is the authoritative proposal version. **Chapters I–III define the proposed study; the benchmark experiments are planned, not completed.** Updated documentation: 15 October 2026.

**Current title:** Design and Evaluation of GBBRPM: A Graph-Based Bounded Risk Propagation Model for Comparative Prioritization on Directed Acyclic Graphs Across Network Domains.

GBBRPM currently expands to **Graph-Based Bounded Risk Propagation Model**. The model, its executable **GBBRPM evaluation engine**, and its supporting interactive prototype have distinct roles.

## Start here

- [Current scope, evidence status, and source map](docs/CURRENT_PROPOSAL_STATUS.md)
- [Proposal briefing pack](briefings/00_MASTER_INDEX.md)
- [Proposal adviser briefing](ADVISER_BRIEFING_PROPOSAL.md)
- [Next-work checklist](docs/NEXT_STEPS.md)
- [Documentation index and historical notes](docs/README.md)
- [Documentation changes and verification scope](docs/DOCUMENTATION_ALIGNMENT_2026-10-15.md)

## Scientific focus

The planned controlled study asks when complement-product recursion gives useful **receiving-state** rankings under an explicitly specified stochastic reference, how shared origins affect agreement, and what accuracy–cost tradeoffs alternative mechanisms provide. Receiving-state priority differs from source influence and intervention benefit.

The domain core is a bounded comparative index:

```text
w_ij = S_ij * tau_ij
Q_ij = w_ij * R_i
R_j = 1 - (1 - B_j) * product_i(1 - Q_ij)
```

It uses current accumulated upstream R, not original B. A predecessor-free node has R=B. Domain outputs are not calibrated event probabilities. Only the separately defined benchmark gives B and w Bernoulli-probability meanings; its conditional edge probability is w, not Q.

Under that benchmark's independent primitive events on a finite DAG, Chapter 3 states:

```text
recursive maximum M <= restricted-tree T <= exact marginal pi
                    <= GBBRPM R <= recursive clipped sum H
```

The specified unthresholded target-specific tree gives `0 <= R-pi <= R-T <= R-M`. These are conditional mathematical guarantees grounded in existing bounding arguments, not domain calibration or a verified first-ever theorem. Actual tightness, rankings, selection quality, and costs require the planned experiments.

## Prospective benchmark inventory

| Block | Planned quantity | Status |
|---|---:|---|
| Matched shared/independent branch family | 560 scenarios | Exact closed-form receiver references specified |
| Uniform generated DAGs | 300 topologies; 3,600 scenarios | 720 development; 2,880 evaluation |
| Secondary heterogeneous subset | 144 additional scenarios on existing topologies | 24 development; 120 evaluation; separate summaries |
| Verified Express topology | 12 scenarios | Original inputs included; new benchmark not executed |
| Precision audits | 48 additional million-trial solves | Revisit preselected scenarios; not new scenarios |

The four scenario blocks total 4,316 before any pre-evaluation feasibility amendment. Counts do not imply execution or pooled inference. Generated references use N=100,000 with per-solve simultaneous node uncertainty intervals; audit solves use a separate N=1,000,000 estimate. A development-only compute pilot will determine feasibility before held-out outcomes.

Comparators include local-only, recursive maximum, clipped addition, GBBRPM, the local-upstream recursion ablation, restricted in-arborescences, the published Abbe et al. (2020) DAG lower recursion, and a specified ancestry-grouping diagnostic. Each recursive method computes its own states. The published full upper algorithm is discussed, not required as a full-grid implementation.

Fixed-budget selection uses exactly k candidates at 10%, 20%, and 30%, excluding positive-B nodes and retaining unreachable zero-B nodes. Capture, regret, rank association, resolved reversals, bracket tightness, runtime, and memory will be reported. Expanded cutoff-tie Jaccard is a separate descriptive measure.

## Build target and evidence structure

Build **main.tex**; its main body is Chapters I–III, references, and Appendices A–E. `main.pdf` is supplied from the uploaded package; this documentation-only update does not rebuild or replace it.

| Location | Role |
|---|---|
| `chapters/chapter1.tex` | Problem, six questions/objectives, scope, framework, definitions |
| `chapters/chapter2.tex` and `chapters/cascade_prior_art.tex` | Literature and close approximation/bounding precedents |
| `chapters/chapter3.tex` | Formulation, implementation, evaluation, cases, reporting, schedule |
| `chapters/reference_benchmark.tex` | Planned process, inventory, controls, methods, uncertainty, metrics |
| `chapters/benchmark_bound.tex` | Conditional bracket, proof, certificates, and interpretation |
| `appendices/appendixA.tex` | Generic worked calculation |
| `appendices/appendixB.tex`, `appendixC.tex` | Preliminary software/electrical worked calculations |
| `appendices/appendixD.tex` | Selected completed exploratory evidence and limitations |
| `appendices/appendixE.tex` | Supporting prototype contract and planned verification |
| `briefings/` | Updated proposal study notes and Q&A |
| `docs/` | Current status/tasks plus labeled historical revision records |
| `archive/` and uncompiled Chapters IV–VI | Historical full-study context, not current proposal results |

## Historical evidence and domain boundaries

The 136-run N1–N5 and 43-scenario electrical configurations are historical exploratory suites, proposed for reviewed reruns. They are separate from the new benchmark. Earlier N1–N5 fixture files are unavailable for direct comparison; reconstructed inputs must retain their provenance. Agreement with historical outputs does not establish input-file identity.

Drainage, software dependencies, and electrical networks are supporting instantiations. Historical unfavorable SWMM agreement does not validate hydraulic ranking or maintenance utility. Real software topology/advisory inputs do not supply independent incident labels. Electrical topology and measured normal-operation loading plus injected disturbances do not validate event prediction. Independent domain outcomes are required for practical claims, and domain scores are not pooled on a common physical scale.

Original Express 4.18.2 files are included in `data/software/express_4.18.2/`. Verify hashes, direction, acyclicity, and advisory origins with:

```bash
python3 scripts/verify_express_inputs.py
```

Input verification does not run the stochastic benchmark. The manuscript package does not contain the full new benchmark runner. Existing plotting scripts do not implement the proposed protocol automatically. Restricted electrical measurements and credentials are not included.

Prototype revision eafec4d and prior tests are team-reported; matching application source/logs were not reproduced here. Manual browser inspection and reported non-finite loading/capacity handling remain evidence tasks. The scalar DAG core is O(V+E), sorting adds O(V log V), and adapter, tree, diagnostic, reference, and display costs are separate.

## Actual preliminary-page configuration

The active `preliminary/preliminary.tex` includes the title, contents, table/figure/equation lists, and acronyms, then resets body numbering to Arabic 1. It currently **does not include approval, acknowledgement, or abstract pages**, although their source files remain present. Earlier restoration/integration notes describe previous configurations. Confirm the intended submission configuration with the authors; this update changes documentation only.

`main.tex` currently loads `pdfpages` unconditionally. An earlier repair note describes a conditional-loading revision, which is not the uploaded active preamble. If the installed TeX distribution requests missing `pdflscape.sty` through `pdfpages`, install the dependency through the distribution or review the preamble deliberately. No LaTeX repair is claimed in this pass.

## Provisional schedule

W1 is anchored to 12 October 2026; W8 starts 30 November 2026; W24 ends 28 March 2027. These remain planning placeholders, not confirmed defense/submission deadlines. The W8 checkpoint reviews data, mappings, and scenario eligibility. Compute/protocol amendments must be frozen before held-out outcomes. Missing operational records narrow domain claims rather than prevent the controlled study.

## Build locally or in Overleaf

Windows requirements: MiKTeX, Strawberry Perl for latexmk, VS Code with LaTeX Workshop. Restart VS Code after installation and check:

```powershell
perl --version
pdflatex --version
latexmk --version
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

For stale build-cache problems, run `latexmk -c main.tex` and rebuild. In Overleaf, upload the full source ZIP, select `main.tex`, and compile with pdfLaTeX. Build from the project directory. Do not merge another machine's auxiliary files.

The source uses natbib author–date citations, an alphabetically presented APA-style bibliography, A4/CITC body settings, and Palatino as the available Book Antiqua substitute. Confirm final institutional font, metadata, front matter, and dates before submission; documentation alignment is not institutional approval.

## Regenerate historical plots only

```powershell
python -m pip install matplotlib pandas
python scripts/generate_chapter4_figures.py
python scripts/generate_figure4_8.py
```

These consume included historical summary CSVs. They do not recover earlier edge-level fixture identity or execute the new reference study. Cross-domain figures/tables/results preserve separate experiment outputs and require their corresponding generators and authorized sources for regeneration.

## Version-control practice

Review the diff and stage the intended sources/docs explicitly. Preserve existing uncommitted work. Exclude build caches and restricted data; record input hashes and engine revisions with experiment outputs. A manuscript source build and a completed benchmark are separate checks.
