# Briefing 05: Planned Accuracy, Robustness, and Cost Evaluation

**Proposal briefing: no completed benchmark results are asserted.** The legacy filename is retained for compatibility.

## Primary selection outcomes

Candidates are nodes with B=0, including unreachable nodes. Exclude positive-local-input nodes so supplied disturbances do not trivially dominate. For f in {0.10,0.20,0.30}, set `k=max(1,ceil(f*|C|))` and select exactly k candidates.

Average boundary-tie handling over 100 seeded random node-order permutations, shared by methods and independent of reference outcomes (seed 140). Numerical tie groups use absolute tolerance 1e-12 anchored to the highest score in each descending group.

| Measure | Interpretation |
|---|---|
| Capture | Sum of pi over selected nodes divided by sum of pi over candidates |
| Regret | Optimal k-node activation mass minus selected activation mass |
| Tie-aware Spearman | Association with reference receiving-state ordering |
| Strict reversals | Strict model order contradicted by strict reference order |
| Resolved-pair fraction | Shows how much ordering the reference precision actually resolves |

Capture is undefined when total candidate activation mass is zero. Report that case. Monte Carlo oracle membership and regret are estimates. A set-mass difference has conservative uncertainty bounded by h times the symmetric-difference size.

Descriptive top-three/top-20% Jaccard uses expanded cutoff ties and can exceed nominal k. It is a separate measure and must not be used to claim fixed-budget superiority. Constant-rank Spearman is undefined.

## Score tightness and uncertainty

Report R-M, R-T, actual upper slack R-pi, lower slacks pi-M and pi-T, mean/max absolute error, and terminal error. The bracket already guarantees the sign and pointwise ordering under the declared process. Measure tightness and ordering consequences; do not present the guaranteed inequality as an empirical discovery.

Intersect per-node Monte Carlo intervals with [T,R], or [M,R] for scalar-only certificates, when nonempty. An empty intersection is a sampling-coverage or implementation discrepancy to retain and investigate. A sampled reversal is resolved only when nonempty intersected intervals establish the opposite strict order at the stated per-solve coverage. Report counts, denominator, ties, and unresolved pairs together.

Also report near-saturation fractions (scores/reference estimates at least 0.95), numerical saturation at 1-1e-12, and distinct score groups. Retain near-zero and saturated cases. A tighter pointwise bound need not yield better rankings.

Graph is the replication unit. Average nodes within graph first; give graphs equal weight; keep development, evaluation, graph families, sizes, weights, source settings, heterogeneous cases, and Express summaries distinguishable. Repeated conditions on one graph are not independent graph replications.

## Prospective dependence diagnostic

Carry local-origin label sets. Form an overlap graph of positive incoming contributions; connected components, including transitive overlap, define groups. Keep the largest incoming contribution per group, combine group maxima and the local term by complement product, and propagate this variant's own states and union labels.

It may suppress independent edge opportunities or merge partially overlapping origins. It is not the restricted-tree comparator and inherits no stated upper-bound guarantee. Evaluate both failures and gains against the same reference. A straightforward implementation can need `O(K*sum_j d_j^2)` overlap work; record label sizes, checks, runtime, and memory.

## Robustness and cost plans

Planned robustness uses 600 trials at each delta in {0.05,0.10,0.20}, seed 41, and independently perturbed S clipped to [0,1]. Freeze topology, B, and tau. Historical robustness tables do not certify this exact revised implementation.

Validation/order and scalar propagation are O(V+E), full sorting adds O(V log V), and graph/contribution-trace storage is O(V+E). These bounds exclude adapters and extra diagnostic/tree work. Measure validation/order, propagation, ranking, total evaluation, and peak memory separately. Use five warm-ups and 30 deterministic repetitions; state hardware and instrumentation. Reference timings include trial count/precision, preparation, and sampling; per-target tree construction is included.

A development-only pilot precedes the full compute commitment. The primary generated references imply 75.6 billion potential edge-trial checks, audits another 10.08 billion, and heterogeneity another 3.024 billion under direct execution. These are workload estimates, not measured runtimes. Document any reduction before held-out outcomes.

## Preliminary context

Appendix D preserves historical 136-run behavior evidence, 600 randomized property trials, robustness summaries, counterfactual dependence differences, and sparse-DAG timings. These motivate the proposed evaluation but do not provide its reference errors, fixed-budget results, or matched memory/cost comparisons. Historical disagreement with GBBRPM measures information dependence, not accuracy against ground truth.

Sources: Chapter 3 properties/cost/reporting sections; `chapters/reference_benchmark.tex`; Appendix D.
