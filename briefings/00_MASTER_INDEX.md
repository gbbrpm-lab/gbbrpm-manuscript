# GBBRPM Defense Briefing Pack

This pack follows the thesis from motivation to recommendations. Each file can be reviewed independently, but the numbering gives the recommended study order.

## Recommended order

1. [Study Overview and Problem](01_STUDY_OVERVIEW_AND_PROBLEM.md)
2. [Literature Gap and Contribution](02_LITERATURE_GAP_AND_CONTRIBUTION.md)
3. [Model Formulation and Equations](03_MODEL_FORMULATION_AND_EQUATIONS.md)
4. [Methodology and Experiment Design](04_METHODOLOGY_AND_EXPERIMENT_DESIGN.md)
5. [Architecture Results, Robustness, and Scalability](05_ARCHITECTURE_RESULTS_AND_ROBUSTNESS.md)
6. [Drainage and SWMM Case](06_DRAINAGE_AND_SWMM_CASE.md)
7. [Software-Dependency Case](07_SOFTWARE_DEPENDENCY_CASE.md)
8. [Electrical-Network Case](08_ELECTRICAL_NETWORK_CASE.md)
9. [Conclusions, Limitations, and Recommendations](09_CONCLUSIONS_LIMITATIONS_RECOMMENDATIONS.md)
10. [Rapid-Fire Examiner Questions](10_RAPID_FIRE_EXAMINER_QA.md)
11. [Suggested Defense Presentation Flow](11_PRESENTATION_FLOW.md)

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

## Three statements to repeat consistently

1. The output is a comparative risk index, not a calibrated probability.
2. Cross-domain instantiability does not mean universal predictive validity.
3. Controlled sensitivity evidence does not equal independent event validation.

