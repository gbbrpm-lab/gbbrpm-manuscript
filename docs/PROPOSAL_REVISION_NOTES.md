# Proposal revision notes — October 13, 2026

This source revision implements the October 12 consultation and the additional
requests to name the software an **evaluation engine** and retain the
cross-domain emphasis in the title.

## Working title

Design and Evaluation of GBBRPM: A Graph-Based Bounded Risk Propagation Model
for Comparative Prioritization on Directed Acyclic Graphs Across Network Domains

GBBRPM names the mathematical model proposed by the study. The GBBRPM
evaluation engine names its executable implementation. “Across network domains”
describes separate instantiation studies; it does not claim that all directed
networks are DAGs or that domain scores have a common calibration.

## Feedback resolution

| Point | Implemented change |
| --- | --- |
| Model identity | First introduction and terms distinguish the named model, broader research area, constituent mechanisms, and software engine. |
| Title and DAG restriction | Title retains cross-domain focus and explicitly states directed acyclic graphs. DAG restriction is repeated in the objective, scope, framework, and engine contract. |
| Lightweight | Added operational definition, dedicated question/objective, propagation versus sorting complexity, timing/memory boundaries, input inventory, and a qualified high-fidelity comparison plan. |
| Local/structural comparison | Retained local-only and uniform conditions; specified a planned normalized in-degree descriptor to test different information dependence, without claiming superior outcome accuracy. |
| Objectives | Replaced literature-synthesis and pooled-evidence objectives with six aligned formulation, implementation, comparison, behavior, resource, and instantiation objectives. |
| Significance | Explicit theoretical and practical subsections, with practical benefits conditional on outcome evidence. |
| Scope and limitations | Explicit subsections; included work separated from model, data, and interpretation restrictions. |
| Chapter 2 flow | Regrouped existing literature into eight main subsections, retaining citation commands and source-based content. Improved the model-family table's column layout. |
| Chapter 3 flow | Design and detailed formulation precede implementation, data preparation, experiments, evaluation, analysis, and schedule. Research phases are distinguished from a per-scenario engine algorithm. |
| Formulation detail | Added notation/input roles, aggregation-choice rationale, initialization, recursive-state handling, analytical properties, identifiability, dependence, and numerical/input requirements. |
| Cross-domain evaluation | Separate mapping and within-domain analyses; no pooling of scores or equivalent-outcome claims. |
| Proposal stage | Main compilation includes only Chapters I–III, references, and Appendices A–D. Final-study chapters are archived. |
| Preliminary work | Selected evidence retained in Appendix D, including negative SWMM associations. Software and electrical worked calculations explicitly labeled preliminary. |
| Future-heavy methodology | Planned activities use future tense; mathematical statements remain present-tense and preliminary work remains past-tense. |
| Timeline | Provisional 24-week schedule includes prior-work documentation, proposal presentation, both revision buffers, acquisition checkpoint, implementation, evaluation, final defense/submission, and conditional dissemination. |
| Figure 3.2 concern from earlier discussions | The controlled-network figure now clearly states it is schematic and does not show all fixture nodes. Its new proposal number is Figure 3.3. |
| Engine name | GBBRPM evaluation engine used in definitions, methodology, prototype architecture, and documentation. |

## Scientific boundaries retained

The core equations Q_ij = S_ij tau_ij R_i and
R_j = 1 - (1 - B_j) product(1 - Q_ij) are unchanged.
Bounded aggregation is not dependence correction. S and tau remain conceptually
distinct but are not separately identified by risk outputs. The mean-of-snapshot
apparent-power construction in Appendix C remains intact.

Numerical results in the preliminary summaries were transferred from the
uploaded source record, not regenerated as new findings. The original six-chapter
PDF and chapter sources are preserved in archive/full-study. Prior briefings are
in archive/prior-briefings and should be treated as pre-consultation material.

## Proposed methods added or made explicit

The revised study plan specifies normalized directed in-degree comparison;
separated validation/order, propagation, sorting, and total timings; peak-memory
measurement; a denser DAG series; a bounded relative-uniform susceptibility
perturbation protocol; and cutoff-tie inclusion with absolute tolerance 1e-12.

These are prospective protocol choices. The original 136-run, 43-run, and
historical robustness outputs do not establish that every new choice has already
been tested or that all rerun outputs will be identical. Code/schema compatibility
must be implemented and checked as part of the proposed work. Existing
experiment scripts were preserved and were not changed to execute the new plan.

## Items still to confirm

- Official proposal-defense, final-defense, submission, and presentation dates.
  The current W1 anchor is October 12, 2026; later milestones are provisional.
- Agency drainage-data adequacy and acquisition timing.
- Availability of independent, event-aligned electrical outcomes.
- Final agreement on the prospective comparator, numerical, and perturbation
  conventions before confirmatory evaluation.
- Primary-source support for novelty and broad comparative claims, beyond the
  supplied manuscript's existing citations.
- Official final-submission front matter, which remains outside this pass.

## Verification scope

The LaTeX proposal was compiled with pdfLaTeX through latexmk; citations and
cross-references were resolved. Rendered title, tables, definitions, equations,
diagrams, timeline, and appendix pages were inspected. This validates the edited
document's compilation and presentation, not implementation of newly proposed
experiments or academic approval.
