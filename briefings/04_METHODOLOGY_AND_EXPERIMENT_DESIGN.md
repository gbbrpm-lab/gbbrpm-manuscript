# Briefing 04: Planned Methods and Experiment Inventory

**All benchmark rows below are prospective. Historical exploratory runs are separate.**

## Sequence

Specify the model and reference; implement and validate solvers/comparators; pilot development costs; finalize and freeze the protocol before held-out evaluation; then analyze selection, bound tightness, resources, and separate domain cases. The final feasibility decision precedes evaluation outcomes. Any later redesign needs unused cases for a confirmatory claim.

## Planned reference inventory

| Block | Inventory | Development/evaluation distinction |
|---|---:|---|
| Matched shared/independent branch controls | 560 scenarios | Analytically specified mechanism controls with exact receiver reference |
| Uniform-weight generated DAGs | 300 topologies; 3,600 scenarios | 720 development; 2,880 evaluation |
| Secondary heterogeneous weights | 144 additional scenarios on 72 existing topologies | 24 development; 120 evaluation; summarize separately |
| Express topology | 12 scenarios on the verified 71-node, 128-edge snapshot | Separate real-topology stochastic experiment |
| Low-weight precision audits | 48 additional million-trial reference solves | Existing generated scenarios; not 48 new scenarios |

The four scenario blocks total **4,316 planned scenarios**, before any feasibility amendment. The 48 audit solves are additional precision work. This sum is a documentation convenience, not a pooled analysis or a completed-run count.

## Branch family

Use branch counts {1,2,4,8}, path lengths {2,4}, edge probabilities {0.05,0.10,0.20,0.25,0.50,0.75,1}, source probabilities {0.10,0.25,0.50,0.75,1}, and both origin conditions: `4*2*7*5*2=560`. Match graph, edge weights, and branch-start marginals; change the joint origin construction. Closed forms supply exact receiver probabilities even beyond the enumeration cap.

## Generated DAGs

Use forward-edge, adjacent-layer, and preferential-attachment families at {20,50,100,250} nodes, each with exactly 2V unique edges. Check layer capacity; do not silently replace an infeasible generator. Preferential attachment starts with all ten forward edges among five nodes and adds two incoming edges per later node. A scale-free law is not presumed.

For every family/size use seeds 41–45 for development and 1001–1020 for evaluation. Each topology receives six uniform weights {0.05,0.10,0.20,0.25,0.50,0.75} and two initial settings: the first ceil(0.10V) nodes in its ordering receive B=0.5 or B=1. Other B values are zero. Initial-origin nodes need not have in-degree zero.

The secondary subset uses development seed 41 and evaluation seeds 1001–1005, both initial settings, and a stable SHA-256 ordering of edges. One quarter receive w=0.10, one half 0.20, and one quarter 0.30, preserving mean 0.20. Pair with existing uniform-0.20 conditions. Use S=w, tau=1. Copy the exact hash-string construction from Chapter 3; do not improvise it.

## Reference solvers

Enumerate configurations with at most 16 non-degenerate primitive variables, fixing probability-zero/one variables. Check total mass and isolated, chain, independent-convergence, and diamond identities. Validate Monte Carlo against enumeration.

General graphs use N=100,000 independent trials in memory-bounded batches and recorded per-scenario seeds. Per-solve simultaneous node intervals use `h=sqrt(log(2V/0.05)/(2N))`, clipped to [0,1]. This is Monte Carlo sampling uncertainty for one scenario, not a model error guarantee or joint coverage across all experiments.

The 48 audits use evaluation seed 1001, all three families and four sizes, weights {0.05,0.10}, and both source settings. Add a separate N=1,000,000 solve and retain both estimates. Unobserved rare activations do not imply zero true probability.

## Matched methods

Local-only; recursive maximum M; recursive clipped sum H; ordinary GBBRPM R; local-upstream complement-product ablation using B_i instead of R_i; target-specific restricted-tree T; the published Abbe et al. (2020) DAG lower recurrence; and the specified ancestry-aware diagnostic. Every recursive variant computes its own states on the same primitive inputs.

The published lower comparator uses an auxiliary certainly active source with edges of probabilities B. It has no assumed ordering relative to M or T. The full published upper algorithm is not a required full-grid implementation. In-degree is descriptive; seed-spread and intervention measures are different tasks.

## Historical suites

The N1–N5 136-run inventory and electrical 43-scenario suite are preliminary evidence, with reviewed reruns planned. They are not part of the new stochastic inventory. Original earlier N1–N5 inputs are unavailable for direct file comparison; reconstructed fixtures must retain that provenance. Express originals are included and verified, a separate fact.

Sources: `chapters/chapter3.tex`; `chapters/reference_benchmark.tex`; Appendix D.
