# GBBRPM Defense Briefing Pack

This pack follows the thesis from motivation to recommendations. Each file can be reviewed independently, but the numbering gives the recommended study order.

## Current manuscript status

This briefing pack is aligned with the verified 86-page A4 consultation manuscript containing Chapters 1--6, the research-prototype sections, and Worked Appendices A--C. Operational drainage integration remains pending a provenance-complete real dataset.

## Recommended order

1. [Study Overview and Problem](01_STUDY_OVERVIEW_AND_PROBLEM.md)
2. [Literature Gap and Contribution](02_LITERATURE_GAP_AND_CONTRIBUTION.md)
3. [Model Formulation and Equations](03_MODEL_FORMULATION_AND_EQUATIONS.md)
4. [Methodology and Experiment Design](04_METHODOLOGY_AND_EXPERIMENT_DESIGN.md)
5. [Architecture Results, Robustness, and Scalability](05_ARCHITECTURE_RESULTS_AND_ROBUSTNESS.md)
6. [Drainage and SWMM Case](06_DRAINAGE_AND_SWMM_CASE.md)
7. [Software-Dependency Case](07_SOFTWARE_DEPENDENCY_CASE.md)
8. [Electrical-Network Case](08_ELECTRICAL_NETWORK_CASE.md)
9. [Research Prototype](08A_RESEARCH_PROTOTYPE.md)
10. [Conclusions, Limitations, and Recommendations](09_CONCLUSIONS_LIMITATIONS_RECOMMENDATIONS.md)
11. [Rapid-Fire Examiner Questions](10_RAPID_FIRE_EXAMINER_QA.md)
12. [Suggested Defense Presentation Flow](11_PRESENTATION_FLOW.md)

The detailed Component 2 briefing remains available at [ADVISER_BRIEFING_COMPONENT2.md](../ADVISER_BRIEFING_COMPONENT2.md).

## Thesis in one sentence

GBBRPM is a deterministic, bounded, non-probabilistic recursive architecture that combines local disturbance with directed network context to produce traceable comparative node-risk rankings on DAGs.

## Evidence map

| Evidence block | Main question answered | Strongest defensible claim |
|---|---|---|
| N1--N5 architecture suite | Does the formulation behave as designed? | Bounded, monotone, topology-sensitive behavior under controlled conditions |
| Robustness and scalability | Is prioritization stable and computationally tractable? | Broad ranking stability under modest perturbation and one-pass sparse-DAG scaling |
| SWMM comparison | Does graph risk reproduce hydraulic consequences? | No; disagreement defines a clear hydraulic scope boundary |
| Software case | Can the frozen roles map to a different real topology? | Structural instantiability and controlled transmission sensitivity |
| Electrical full-network import | Can real topology and baseline channels be processed? | Topology and baseline data-pipeline verification |
| Component 2 | Can measured loading parameterize a controlled electrical instantiation? | Real-topology, measured-loading mechanism and sensitivity evidence |
| Research prototype | Can the frozen evaluator support a validated interactive workflow? | Implementation feasibility, graph safeguards, and traceable outputs |

## Worked-appendix map

| Appendix | Purpose | Result to remember |
|---|---|---|
| Appendix A | Generic core calculation | Source initialization, current-state recursion, bounded aggregation, ranking, and ties |
| Appendix B | Software-dependency calculation | Express reaches `R = 0.9118` at the controlled `tau = 0.50` setting |
| Appendix C | Electrical Component 2 calculation | Phasor-derived susceptibility and complete trace reproduce risk sum `1.186` |

The operational drainage calculation is intentionally not fabricated; it will be added only when defensible real drainage inputs are available.

## Three statements to repeat consistently

1. The output is a comparative risk index, not a calibrated probability.
2. Cross-domain instantiability does not mean universal predictive validity.
3. Controlled sensitivity evidence does not equal independent event validation.
