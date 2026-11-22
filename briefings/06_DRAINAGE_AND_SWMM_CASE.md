# Briefing 06: Drainage and SWMM

**Role: supporting instantiation; operational usefulness remains conditional.**

Drainage supplied the original motivation. It is now one of three supporting cases rather than the primary scientific benchmark. Nodes/edges must define permitted downstream influence and form a defensible DAG. The domain adapter uses compatible nonnegative load L and positive capacity C:

`S_ij=min(1,L_ij/C_ij)`.

B is a declared disturbance or documented condition mapping. Tau defaults to the neutral value only where justified. Clipping S bounds the adapter input; it neither produces a failure probability nor forces downstream R to one. Other edges can still change after one edge reaches S=1.

## Preliminary hydraulic evidence

Appendix D retains an earlier 12-scenario SWMM comparison:

| Simulated outcome | Mean Spearman | Top-20% Jaccard | Positive worsening outside downstream scope |
|---|---:|---:|---:|
| Maximum depth | -0.416 | 0.119 | 71.2% |
| Flooding volume | -0.485 | 0.000 | 40.5% |

These are historical exploratory findings, not new results from the proposal benchmark. They do not support hydraulic ranking equivalence or validate maintenance/inspection utility. The mismatch is consistent with omitted hydraulic behavior but does not isolate the causal mechanism in each scenario.

## Planned evaluation and eligibility

Align graph, intervention, entity mapping, and SWMM scenarios. Compare priority changes with maximum-depth and flooding changes; report association, priority-set overlap, and positive worsening outside the downstream region. Simulations remain distinct from field observations.

Operational evaluation requires provenance-complete topology and flow direction, specifications, loading/capacity, condition/maintenance records, and independent outcomes. An outcome used to construct inputs is not an independent validation label. Missing records cannot be replaced by invented observations. W8 is a data/mapping/eligibility review, not a promised date of successful field validation.

The DAG core omits backwater, surcharge, ponding, redistribution, and feedback. Any quantitative SWMM speed comparison requires a separate paired protocol with explicit solver settings, scenarios, hardware, and timing boundaries. Existing scalar timings alone do not establish it.

## Concise answer

“We retain drainage to examine a documented mapping and its limits. Historical SWMM disagreement restricts the claims; the primary planned mechanism evaluation uses the separately specified stochastic reference.”

Sources: Chapter 3 drainage/domain/cost sections; Appendix D.
