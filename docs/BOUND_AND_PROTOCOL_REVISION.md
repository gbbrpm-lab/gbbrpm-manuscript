# Current Conditional Bracket and Benchmark Protocol

Synchronized 15 October 2026 to `chapters/benchmark_bound.tex` and `chapters/reference_benchmark.tex`. **Benchmark execution remains planned.** The earlier revision record is preserved in `../archive/documentation-before-2026-10-15/docs/BOUND_AND_PROTOCOL_REVISION.md`.

## Guarantee and scope

For the finite DAG independent-primitive activation process, recursive maximum M, specified restricted-tree T, full-process marginal pi, ordinary recursion R, and recursive clipped addition H satisfy:

`M<=T<=pi<=R<=H`, hence `0<=R-pi<=R-T<=R-M` when T is available.

The tree retains consistent maximum-weight paths from every positive-path ancestor to each target, original B/weights, and no positive-path threshold. T is exact on that restricted process, not the full graph. Target construction has additional cost. Positive association and aggregation are established arguments. No domain probability calibration, arbitrary-pruning guarantee, diagnostic upper bound, or first-ever theorem claim follows.

`T_a>R_b` (or the cheaper sufficient `M_a>R_b`) certifies reference order. Overlap is inconclusive. Tighter pointwise bounds do not imply better selection. Actual slack and ranking outcomes remain empirical questions.

## Current inventory

| Block | Count | Status |
|---|---:|---|
| Matched branches | 560 | Planned; exact receiver closed forms |
| Uniform generated DAGs | 300 topologies; 3,600 scenarios | Planned; 720 development / 2,880 evaluation |
| Heterogeneous subset | 144 additional scenarios | Planned; 24 development / 120 evaluation; existing topologies |
| Express topology | 12 scenarios | Planned; original inputs included and verified |
| Precision audits | 48 additional reference solves | Planned; existing scenarios, N=1,000,000 |

Generated families are forward-edge, adjacent-layer, and preferential attachment with 2V edges and V={20,50,100,250}. Development seeds are 41–45; evaluation seeds 1001–1020. Uniform weights are {0.05,0.10,0.20,0.25,0.50,0.75}; initial settings are B=0.5 or 1 on the first ceil(0.10V) nodes in recorded order. Branch controls additionally use weight 1 and their own source grid. The secondary subset uses seed 41 and 1001–1005, mean-preserving hashed weights {0.10,0.20,0.30}, and separate summaries.

## References, methods, and metrics

Use exact enumeration at at most 16 non-degenerate primitives and branch closed forms beyond that cap. General Monte Carlo uses N=100,000, fixed scenario seeds, batches, and simultaneous Hoeffding node intervals for one scenario only. Audit selection is seed 1001, each family/size, weights 0.05/0.10, both initial settings. Keep both estimates; unresolved values remain unresolved.

Compare local-only, M, H, R, local-upstream ablation, T, the published 2020 DAG lower recurrence after the auxiliary-source transformation, and the specified lineage diagnostic. No ordering relative to M/T is assumed for the published lower comparator. Its full upper counterpart is discussed rather than required on the full grid.

Exclude positive-B nodes from the common ranking candidate set but retain unreachable nodes. Select exactly k at 10/20/30% budgets with 100 shared outcome-independent permutations and the anchored 1e-12 tie policy. Report capture/regret, association, strict and interval-resolved reversals, resolved fractions, bracket/slack metrics, saturation, and uncertainty. Expanded descriptive Jaccard cutoffs remain separate. Graph is the replication unit; repeated conditions are paired, not independent graphs.

A development pilot must assess the 75.6-billion primary, 10.08-billion audit, and 3.024-billion heterogeneous potential edge-trial checks under literal execution, together with comparator/tree costs. These are not timing measurements. Freeze any feasibility reduction before evaluation outcomes and record revised counts and precision.

See [current status](CURRENT_PROPOSAL_STATUS.md), [review follow-up](REVIEW_PROTOCOL_FOLLOWUP.md), and [next work](NEXT_STEPS.md). Prior authoring checks and historical exploratory results do not establish completion of these protocols.
