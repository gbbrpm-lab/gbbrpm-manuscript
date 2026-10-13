# Conditional benchmark bracket and expanded evaluation

## Meaning and contribution

GBBRPM remains a domain comparative index. Under the separately specified
synthetic process with independent initial-activation and edge-transmission
primitives, the same recursion is a nodewise upper bound on activation
marginals. The conditional result is not a calibration of domain inputs.
Deterministic evaluation itself does not distinguish probability from index
semantics; the interpretation and assumptions do.

The added proof establishes

    recursive maximum <= exact cascade marginal <= GBBRPM <= recursive clipped sum.

It uses established positive association and bounded aggregation. The statement
is presented as a benchmark proposition with explicit assumptions, not as an
unprecedented theorem. The nearest literature comparison now includes
Abbe, Kulkarni, and Lee (2017), MIA (Chen, Wang, and Wang, 2010), and LDAG
(Chen, Yuan, and Zhang, 2010). Their primary papers were inspected for the
association argument, length-indexed bounds, restricted-tree recurrence,
and Linear Threshold semantics, respectively.

## What the bound changes

- GBBRPM's benchmark slack is nonnegative. Its sign need not be inferred
  from experiments, though numerical failures still need investigation.
- Width R-M is a computable error certificate under the benchmark.
- Clipped sum cannot be a tighter nodewise upper bound than GBBRPM under
  these assumptions. It can still have different ranking quality.
- A lower bound for node a exceeding the upper bound for node b certifies
  that a has greater benchmark activation probability. Overlap is inconclusive.
- The ancestry-overlap diagnostic does not inherit an upper-bound guarantee.

Ranking and fixed-budget selection are the primary benchmark outcomes;
score metrics describe tightness. The stochastic reference remains a proxy
task. Agreement with it does not establish inspection or intervention utility.

## Current inventory

| Experiment | Count | Status |
|---|---:|---|
| Matched shared/independent branch family | 560 scenarios | Planned; exact closed-form receiver reference |
| Generated DAGs | 300 topologies, 3600 scenarios | Planned |
| Generated development subset | 60 topologies, 720 scenarios | Seeds 41--45 |
| Generated evaluation subset | 240 topologies, 2880 scenarios | Seeds 1001--1020 |
| Express topology | 12 scenarios | Planned, requires verified raw snapshot |
| Low-weight precision audit | 48 additional reference solves | Preselected subset, not new scenarios |

Generated families are uniform forward-edge, adjacent-layer, and directed
preferential attachment. Each has 2V edges at V in {20,50,100,250}.
The preferential construction starts with ten edges among five nodes and
adds two incoming edges for each subsequent node, giving 10+2(V-5)=2V.
No scale-free law is claimed from the generator name.

Generated weights are {0.05,0.10,0.20,0.25,0.50,0.75}; branch controls also
include 1. Initial probabilities use the specified fixed source settings.
Graphs are the replication unit, rather than treating repeated weight/source
conditions as independent graph samples. Family and regime summaries remain
separate. Near-zero and saturated cases are retained and reported.

The default reference uses 100,000 trials. The 48 audit cases use a separate
1,000,000-trial estimate selected before outcomes: seed 1001, every family and
size, weights 0.05 and 0.10, and both initial settings. Each solve has its own
sampling interval; no joint confidence guarantee across all experiments is
claimed. Unresolved ranking differences remain unresolved.

Development timings and memory use will establish whether the inventory is
feasible. Any budget amendment must be recorded before evaluation outcomes,
including new counts. The 24-week schedule remains provisional and unchanged.

## Additional comparator

The new restricted-in-arborescence comparator retains consistent maximum
weighted paths to each target and evaluates all retained local inputs on
the resulting tree. This is an adaptation for fixed receiving queries, not
the complete MIA seed-selection algorithm. It preserves multiple local
origins, unlike globally retaining a single largest contribution. Its restricted
process gives a lower bound by edge deletion, with construction cost included.
LDAG is discussed as related literature under another cascade model.

## Express prerequisite

The preserved manifest records historical software node/edge hashes, but
the raw topology CSVs are absent from this manuscript package. Recover and
hash-check them, or acquire and freeze a new resolved-dependency snapshot.
Do not pretend a new snapshot is byte-identical to the historical case or
reconstruct the full network from its figure. Verify acyclicity and all seven
historical advisory-origin identities. Controlled initial probabilities of
0.5 or 1 will test the real topology; advisory severity is not calibrated
as activation probability. This is not real incident validation.

## Locations and work status

- `chapters/benchmark_bound.tex`: proposition, proof, interpretation, and limits.
- `chapters/cascade_prior_art.tex`: closest additional literature distinctions.
- `chapters/reference_benchmark.tex`: expanded inventory, comparators, metrics,
  and reference-precision protocol.
- Chapters 1--3, framework figure, references, README, and current focus notes
  are aligned with the extension.

The core equations and historical data, results, appendices, and timeline are
preserved. The full benchmark, restricted-tree comparator, and diagnostic have
not been implemented or executed here. Small exact calculations check the
mathematical arguments; they are not the proposed full-study results.

## Prior-art follow-up before stronger novelty claims

Compare the DAG specialization and random-initialization construction with
existing reliability, percolation, and cascade-approximation formulations.
Do not infer novelty from new notation, a model name, or a successful proof.
The contribution must identify what additional characterization or supported
application result the proposed experiments establish beyond those precedents.

## Authoring verification

The revised 72-page proposal was compiled and its affected pages inspected.
New citations and cross-references resolved without overfull or undefined errors.
Exact enumeration on 80 four-node configurations checked the bracket and the
restricted-tree comparator's exactness and lower-bound relation. Layer capacity
and preferential edge-count arithmetic were checked for every proposed size.
The 27 historical data/result/appendix files and the timeline matched the
previous source package byte for byte. These checks do not replace execution
of the planned experiment inventory.
