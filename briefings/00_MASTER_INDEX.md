# GBBRPM Proposal Briefing Pack

Updated 15 October 2026 against the uploaded proposal source. Chapters I–III are authoritative; the benchmark experiments are **planned, not completed**. These briefings replace the earlier six-chapter defense narrative. Filenames are retained so existing links continue to work; files 05 and 09 now concern evaluation plans and expected outputs.

## Study in one sentence

GBBRPM is a bounded receiving-state index on DAGs whose proposed evaluation will examine ranking quality, shared-origin dependence, and accuracy–cost tradeoffs against an explicitly defined stochastic reference, with three separate supporting domain instantiations.

The current expansion is **Graph-Based Bounded Risk Propagation Model**. “Blockage” describes the project's earlier drainage framing, not the current model name.

## Read in this order

1. [Study overview and problem](01_STUDY_OVERVIEW_AND_PROBLEM.md)
2. [Literature, gap, and contribution](02_LITERATURE_GAP_AND_CONTRIBUTION.md)
3. [Model and conditional benchmark bracket](03_MODEL_FORMULATION_AND_EQUATIONS.md)
4. [Methods and prospective inventory](04_METHODOLOGY_AND_EXPERIMENT_DESIGN.md)
5. [Planned accuracy, robustness, and cost evaluation](05_ARCHITECTURE_RESULTS_AND_ROBUSTNESS.md)
6. [Drainage and SWMM boundaries](06_DRAINAGE_AND_SWMM_CASE.md)
7. [Software inputs and planned topology benchmark](07_SOFTWARE_DEPENDENCY_CASE.md)
8. [Electrical instantiation](08_ELECTRICAL_NETWORK_CASE.md)
9. [Supporting engine and prototype](08A_RESEARCH_PROTOTYPE.md)
10. [Expected outputs, limitations, and next work](09_CONCLUSIONS_LIMITATIONS_RECOMMENDATIONS.md)
11. [Proposal examiner Q&A](10_RAPID_FIRE_EXAMINER_QA.md)
12. [Proposal presentation flow](11_PRESENTATION_FLOW.md)

For consultation use [the proposal adviser briefing](../ADVISER_BRIEFING_PROPOSAL.md). For electrical detail use [the Component 2 briefing](../ADVISER_BRIEFING_COMPONENT2.md).

## Evidence and status map

| Material | Current status | Permitted interpretation |
|---|---|---|
| Core formulation and conditional bracket | Specified in Chapters 1 and 3 | Mathematical statements under their declared assumptions |
| Appendix A | Generic worked calculation | Explanation of the recursion |
| Appendices B–C | Preliminary software/electrical calculations | Traceable case calculations, not independent outcome validation |
| Appendix D | Selected completed exploratory evidence | Feasibility and limitations; not results of the planned benchmark |
| Express original files | Included; verification procedure supplied | Input identity/integrity, not benchmark execution |
| Branch, generated-DAG, heterogeneous, and Express benchmarks | Planned | No empirical performance findings yet |
| Appendix E | Prototype contract and planned verification | Team-reported prior work and outstanding checks distinguished |

## Source priority

1. Current `main.tex` inclusion tree and Chapters I–III, including their input files.
2. Current appendices, source snapshots, and manifests for their specific evidence roles.
3. These briefings and [current status](../docs/CURRENT_PROPOSAL_STATUS.md), as navigation aids.
4. Earlier revision notes, archived chapters, and earlier chats as history.

A supporting doc must be corrected when it conflicts with the source. Historical 136-run and 43-scenario suites do not stand in for the new benchmark. Domain-index values are not probabilities; receiving-state priority is not intervention benefit; coherent domain mappings do not establish predictive utility.
