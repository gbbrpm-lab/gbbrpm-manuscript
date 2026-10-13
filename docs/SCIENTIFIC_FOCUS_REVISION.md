# GBBRPM: focused research contribution and proposal changes

## What the study will establish

The proposed core output is a receiving-state index: accumulated local and
inherited disturbance. Its established complement-product operator, DAG
traversal, name, and prototype are not sufficient novelty claims.

The strengthened question is:

> When does complement-product recursion give accurate receiving-state
> rankings under a declared reference process, how do shared origins limit
> agreement, and what accuracy and resource tradeoffs accompany simpler
> aggregation and ancestry-aware alternatives?

This is a proposed investigation, not a completed discovery. Its contribution
will depend on the evidence and on comparison with relevant prior approximation
and dependence literature. No first-ever claim or universal error bound is made.

## Three evidence levels

| Evidence | What it can establish | What it cannot establish alone |
|---|---|---|
| Algebra and implementation checks | Correct execution, sufficient independence controls, constructed counterexamples | Operational usefulness |
| Specified stochastic benchmark | Receiving-activation approximation error, selection quality, and cost under its assumptions | Calibration of drainage, advisory, or electrical indices |
| Independent domain outcomes | Case-specific usefulness for a declared target | Universal applicability or intervention benefit from receiving-state rankings |

The model remains a non-probabilistic domain index. Only the separate controlled
benchmark interprets numerical B as initial activation probabilities and S*tau
as conditional edge probabilities. It does not use Q=S*tau*R as a conditional
transmission probability after upstream activation is sampled.

## Main manuscript changes

- Chapter 1 now names receiving-state accuracy and dependence as the central
  scientific problem, with aligned questions and objectives. A residual
  architectural/integrative problem statement was removed.
- Chapter 2 closes with the reference-based evaluation question and credits
  adopted operators and cascade mechanisms.
- Chapter 3 adds Sections 3.6.2--3.6.6 through
  `chapters/reference_benchmark.tex`, including reference semantics, exact
  enumeration, Monte Carlo uncertainty, matched dependence controls,
  comparators, and fixed-budget ranking metrics.
- Section 3.7 defines the prospective ancestry-aware grouping algorithm and
  evaluates its errors and costs. It is a diagnostic, not an assumed solution.
- Sections 3.8--3.11 align cost measurements, outcome requirements, tie handling,
  and development/evaluation separation with the revised study.

## Concrete experiment inventory

The 560 branch-family scenarios hold graph and branch-start activation
marginals fixed while changing shared versus independent initial origins.
They vary branch count, path length, attenuation, and source uncertainty.
Their receiver probabilities have a closed form, so Monte Carlo is unnecessary
for the family reference even when enumeration would be expensive.

The current protocol uses 3600 generated-DAG scenarios from three graph families,
four sizes, 25 graph seeds, six weight settings, and two initial-activation
settings. Seeds 41--45 are development cases; 1001--1020 supply 20 evaluation
graphs per family/size after freezing. The 100,000-trial references have explicit
sampling uncertainty; 48 preselected low-weight cases receive separate
1,000,000-trial precision audits. Another 12 Express scenarios require verified
raw topology inputs, which are absent from this package. See
`BOUND_AND_PROTOCOL_REVISION.md` for the bound, comparator, and inventory update.

Methods are local-only, recursive maximum, recursive clipped sum, ordinary
GBBRPM, the local-upstream recursion ablation, the restricted-in-arborescence comparator, and the ancestry-aware diagnostic.
Recursive maximum already gives the strongest local-origin weighted path, so
adding that as a separate comparator would duplicate a method. In-degree remains
descriptive; seed influence and receiving-state probability are different tasks.

Ranking and selection are the primary benchmark outcomes. Score reports
characterize bound width and upper/lower slack as well as mean and maximum
absolute error, terminal error, Spearman association, activation mass captured
at 10%, 20%, and 30% selection budgets, and selection regret. Ranking candidates
exclude positive-local-input nodes. Budgeted selections have exactly k nodes;
100 shared outcome-independent random permutations resolve boundary ties.
Descriptive cutoff-expanded Jaccard sets remain separate.

## Why pruning is not automatically a fix

On a diamond with source probability 0.5 and perfect edges, the exact receiver
probability is 0.5 while GBBRPM gives 0.75. With a certainly active source and
edge probability 0.5 on every edge, both give 0.4375, while retaining only one
complete branch gives 0.25. Shared ancestry can coexist with independent edge
opportunities. A grouping diagnostic may also combine partially overlapping
lineages and discard independent inputs. These cases must be reported.

## Work order after consultation

1. Review the narrowed question with the adviser and freeze the benchmark
   contract, graph manifest, methods, metrics, exclusions, and reporting rules.
2. Implement the Boolean reference independently of the deterministic model.
   Check exact enumeration against chain, independent-convergence, and diamond
   calculations before relying on Monte Carlo.
3. Implement separately versioned comparators and the specified diagnostic.
   Verify that each recursive method computes its own upstream states.
4. Run the closed-form branch controls and development DAGs. Record failures,
   reference uncertainty, and lineage-processing costs.
5. Freeze the implementation before examining evaluation DAG outcomes. Any
   subsequent redesign requires new unused cases for a confirmatory claim.
6. Evaluate a primary domain outcome only if independent labels and defensible
   mappings are available. Retain the other domains as supporting instantiations.

The current revision specifies these future experiments. It does not implement
the full simulator, execute the inventory, or report new empirical performance.
Three diamond calculations were checked by exact rational enumeration during
authoring: (B,p)=(0.5,1), (1,0.5), and (0.5,0.5). This verifies those examples;
it is not full simulator validation.

## Sources verified for this extension

- Kempe, Kleinberg, and Tardos (2003), *Maximizing the spread of influence
  through a social network*, SIGKDD, pp. 137--146. The author-hosted primary
  paper specifies conditional edge transmission and the equivalent live-edge
  interpretation: https://www.cs.cornell.edu/home/kleinber/kdd03-inf.pdf
- Hoeffding (1963), *Probability inequalities for sums of bounded random
  variables*, JASA 58(301), pp. 13--30.
  DOI: https://doi.org/10.1080/01621459.1963.10500830
  Primary article scan: https://www.cs.rpi.edu/academics/courses/spring06/random/hoefding.pdf
  The bounded-variable concentration inequality supplies the sampling bound;
  applying both tails and a union bound gives the stated per-scenario interval.

## Preserved scope

The title, core equations, historical data/results, preliminary appendices,
and member-owned timeline remain unchanged. The proposal still contains only
Chapters I--III, references, and appendices. New comparisons are planned work;
old exploratory results have not been relabeled confirmatory.
