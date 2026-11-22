# Current GBBRPM Proposal Status

**Authoritative snapshot: uploaded GBBRPM_Manuscript(1).zip, reviewed 15 October 2026.** This file summarizes the manuscript; it cannot override Chapters I–III or their included source files. The benchmark experiments are planned, not completed.

## Identity and research task

The title is **Design and Evaluation of GBBRPM: A Graph-Based Bounded Risk Propagation Model for Comparative Prioritization on Directed Acyclic Graphs Across Network Domains**. The earlier blockage name and completed full-study narrative are historical. The current model is a bounded domain index, the evaluation engine is its implementation, and the prototype supports inspection.

The primary task is receiving-state selection: accumulated local and inherited influence at candidate nodes. The proposal will examine reference agreement, uncertain shared ancestry, attenuation, and accuracy–cost tradeoffs. Source influence and intervention benefit are distinct tasks. Drainage, software dependencies, and electrical networks are separate supporting instantiations.

## Evidence ledger

| Item | Status in authoritative source | Evidence location / consequence |
|---|---|---|
| Core Q=S*tau*R and complement-product update | Specified | Chapters 1/3; current upstream state, not B-only recursion |
| Basic operator properties | Established/adopted mathematics | Credit probabilistic-sum precedent; no invention claim |
| M<=T<=pi<=R<=H | Conditional proposition supplied | `chapters/benchmark_bound.tex`; independent primitives and specified tree only |
| Full stochastic benchmark | Planned | `chapters/reference_benchmark.tex`; no completed error/selection comparison |
| Matched branch references | Closed forms specified | Algebraic controls, not new unseen discoveries |
| Exact/Monte Carlo solvers and comparators | Implementation/validation planned | Historical authoring checks do not certify full runners |
| N1–N5 136-run suite | Historical exploratory record; reviewed reruns proposed | Appendix D; reconstructed fixtures, earlier file identity unavailable |
| Express originals | Included with integrity-check procedure/record | Original CSV hashes match historical manifest; new 12-scenario benchmark unrun |
| Software worked example | Preliminary index calculation | Appendix B; no calibrated exploit probability |
| Electrical case | Real topology/loading; historical controlled injections | Appendices C/D; 43-scenario configuration distinct from new benchmark |
| SWMM comparison | Historical exploratory disagreement | Appendix D; no hydraulic-equivalence or maintenance-utility claim |
| Prototype checks | Preliminary/team-reported, further verification planned | Appendices D/E; matching-source evidence and browser inspection outstanding |
| Operational domain usefulness | Not established | Requires independent target, eligible mapping, adequate outcomes, frozen evaluation |

“Planned” does not mean no preliminary work exists. Conversely, existing exploratory results and input verification do not mean the new protocols have been executed.

## Numerical specifications declared in the proposal

| Block | Declared inventory |
|---|---|
| Matched branches | 560 = 4 branch counts * 2 lengths * 7 weights * 5 source probabilities * 2 origin conditions |
| Uniform generated DAGs | 3 families * 4 sizes * 25 seeds * 6 weights * 2 initial settings = 3,600 |
| Uniform split | 720 development (seeds 41–45); 2,880 evaluation (1001–1020) |
| Secondary heterogeneity | 144 = 3 families * 4 sizes * 6 existing seeds * 2 initial settings; 24 development / 120 evaluation |
| Express | 12 = 6 weights * 2 controlled initial settings on one verified topology |
| Additional precision | 48 million-trial solves revisiting existing evaluation scenarios |

Preserve these manuscript values while preparing implementation; final protocol freezing and feasibility amendments are still planned. The four scenario blocks sum to 4,316, not including extra audit solves or historical reruns. Summaries remain stratified rather than pooled.

Exact enumeration caps non-degenerate primitives at 16; branch closed forms provide exact receiver references beyond that cap. Default N=100,000; audits N=1,000,000. Per-solve Hoeffding half-width is `sqrt(log(2V/0.05)/(2N))`. It is sampling uncertainty for one scenario, not a universal GBBRPM error guarantee.

## Comparison and reporting contract

Compare local-only, recursive maximum, clipped addition, GBBRPM, local-upstream recursion ablation, specified unthresholded restricted trees, the published 2020 DAG lower method, and the ancestry-grouping diagnostic. Every recursive method computes its own states. No ordering is assumed between the published lower method and M or T; the full published upper implementation is not required.

The diagnostic uses connected components of incoming lineage-overlap sets and group maxima. It is not the target-specific restricted tree and may worsen results. It inherits no upper-bound guarantee.

Primary ranking candidates have B=0 and include unreachable nodes. Select exactly k at 10%, 20%, and 30%, using 100 shared outcome-independent tie permutations (seed 140), with anchored 1e-12 tie groups. Report capture/regret, association, strict and interval-resolved reversals, resolved fractions, ties, and unresolved pairs. Expanded cutoff-tie Jaccard is separately descriptive. Report graph-level replication, saturation, bracket widths and slack, and Monte Carlo uncertainty.

## Provenance and missing evidence

Original Express inputs are present under `data/software/express_4.18.2/`; the seven advisory-origin identities and dependency-to-dependent DAG can be checked by the included verifier. The original software files also exist in the experiment repository, but they are not absent from this manuscript package.

Reconstructed N1–N5 fixtures are a different provenance issue. Earlier fixture files are unavailable for direct comparison. Do not describe them as recovered originals or imply that a plotting summary restores edge-level inputs. The experiment repository owns the reviewed fixture/rerun workflow; this manuscript package preserves summaries and selected original software inputs. Do not claim current remote implementation status without inspecting that repository.

Restricted electrical measurements require authorized source access. Normal-operation measurements do not supply independent event labels. Operational drainage records and event-aligned electrical outcomes remain conditional evidence needs. An input-derived advisory label cannot validate the same input mapping independently.

## Current build and preliminaries

`main.tex` includes Chapters I–III, references, and Appendices A–E. Chapter 2 inputs `cascade_prior_art.tex`; Chapter 3 inputs `reference_benchmark.tex`, which inputs `benchmark_bound.tex`. Uncompiled Chapters IV–VI are historical even when their paths sit under `chapters/`.

The active `preliminary/preliminary.tex` includes title, contents, table/figure/equation lists, and acronyms, then body Arabic numbering. It does not include approval, acknowledgement, or abstract. Those source files exist but are inactive. `main.tex` loads `pdfpages` unconditionally, contrary to an earlier conditional-loading repair note. No source inclusion or preamble change is made by this documentation pass.

The uploaded `main.pdf` is preserved, not newly compiled here. No current page count, layout pass, new mathematical proof verification, prototype test success, or benchmark outcome is claimed by this update.

## Planning and historical context

W1: 12 October 2026; W8 begins 30 November 2026; W24 ends 28 March 2027. Dates and the 24-week duration are provisional. The computational pilot precedes full allocation; eligibility and protocol changes must be frozen before held-out outcomes. Missing operational data restrict practical claims rather than block the controlled benchmark.

The earlier trajectory moved from drainage/local condition motivation, to a reusable model with three-domain exploratory work, to the current reference-based proposal. This is orientation from the manuscript/archive and earlier project decisions, not a newly reconstructed meeting record. See [next work](NEXT_STEPS.md) and [documentation index](README.md).
