# Briefing 04: Methodology and Experiment Design

## Research design

The thesis uses a quantitative model-design, computational-validation, and cross-domain evaluation design.

## Two evidence layers

### Layer 1: Architecture validation

Question: Does the frozen formulation behave mathematically and computationally as intended?

Evidence:

- five controlled DAGs;
- 136 controlled scenario runs;
- diagnostic comparators;
- robustness trials;
- randomized property tests;
- reconvergence diagnostics; and
- scalability measurements.

### Layer 2: Cross-domain evaluation

Question: Can the same roles and update rule be instantiated coherently in different directed-network domains?

Evidence:

- drainage and SWMM;
- Express software dependencies; and
- full-network electrical preprocessing plus Component 2.

These layers are not pooled as if they were equivalent predictive validation.

## Controlled network set

| Network | Structure | Diagnostic role |
|---|---|---|
| N1 | Linear | Depth and attenuation |
| N2 | Branching | Divergence and path differences |
| N3 | Converging | Independent multi-source aggregation |
| N4 | Diamond / reconverging | Shared-origin overlap and dependence stress |
| N5 | Mixed | Multiple sources, branching, convergence, intermediate disturbance, heterogeneous susceptibility |

## Why synthetic networks are necessary

Synthetic graphs isolate mechanisms transparently. A real network combines many effects, making it difficult to determine whether a result came from depth, branching, convergence, local disturbance, or heterogeneous edges.

They are mechanism-isolation inputs, not representations of one physical drainage system.

## Provenance of the historical configuration

The exact lost original edge-by-edge table was not recovered. The study uses historical reconstructed node and edge inputs that were computationally verified against preserved baseline and comparator behavior. They are labeled **historical reconstructed validation inputs**, not original field data and not newly invented fixtures.

## The 136-run architecture protocol

| Family | Runs | Purpose |
|---|---:|---|
| Source severity | 20 | Four severity levels across N1--N5 |
| `L/C` stress | 25 | Five load scales across N1--N5 |
| Disturbance location | 36 | Fixed severity at selected locations |
| Multi-source configuration | 10 | Source subsets in N3 and N5 |
| Intermediate disturbance | 45 | Three nodes x three severities x five networks |
| **Total** | **136** | Generic architecture protocol |

The 43 Component 2 experiments form a separate domain-specific protocol.

## Diagnostic comparators

1. **Local only:** `R_j = B_j`
2. **Uniform susceptibility:** recursive architecture with the same `S` on every edge
3. **Heterogeneous GBBRPM:** relation-specific susceptibility

These are mechanism comparators, not ground truth.

## Robustness protocol

- susceptibility perturbations: `+/-5%`, `+/-10%`, and `+/-20%`;
- 600 trials at each perturbation level;
- fixed seed: `41`;
- metrics: Spearman rank correlation and top-set Jaccard overlap.

## Mathematical property tests

Six hundred randomized trials test:

- boundedness;
- monotonicity in local disturbance;
- `B = 1` implies `R = 1`; and
- `S = 0` gates the edge contribution.

## Reconvergence diagnostic

Ordinary GBBRPM is compared with an ancestry-aware path-pruned counterfactual. Incoming terms with overlapping ancestry are grouped, retaining only the largest contribution per group. The counterfactual is diagnostic—not a replacement model or ground truth.

## Scalability protocol

- sparse DAGs with approximately three edges per node;
- sizes from 20 to 1000 nodes;
- five warm-up evaluations;
- 30 timed repetitions;
- median and IQR are primary due to timing outliers.

## Reproducibility safeguards

- versioned input tables;
- fixed seeds;
- generated manifests and hashes;
- explicit data-source selection;
- scenario-level exports;
- separate workflows for core cross-domain and Component 2 results; and
- credentials and restricted raw data excluded from the manuscript package.

## Likely examiner questions

### “Why 136 runs?”

The count follows the declared factorial scenario families. It is not an arbitrary performance target; each family isolates a different mechanism.

### “Why not combine 136 and 43 as 179?”

They can be arithmetically summed, but should not be reported as one protocol. The 136 runs validate the generic architecture, while the 43 runs evaluate one electrical instantiation using different inputs and claims.

### “Why use reconstructed inputs?”

They restore a historically used configuration and reproduce preserved behavior. Their provenance limitation is disclosed, and claims are restricted to computational validation rather than field representativeness.

### “Why use a DAG?”

It guarantees a deterministic one-pass order and prevents unresolved cyclic feedback. Cycles require an explicit iterative or temporal extension, which v1 does not silently assume.

