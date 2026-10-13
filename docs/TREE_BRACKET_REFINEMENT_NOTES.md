# Tree bracket and supporting-prototype refinement

This remains the same GBBRPM proposal. Its non-probabilistic domain index,
separate independent-primitive stochastic benchmark, title, three supporting
domain cases, research questions, equations, prospective experiment counts,
preliminary evidence, and 24-week provisional timeline are retained. Nothing
in this revision reports completed benchmark outcomes.

## Mathematical certificate

For each target, the proposed restricted in-arborescence retains one
consistently chosen maximum-weight next edge for every ancestor with a
positive-weight path to the target. It retains the original local inputs and
weights and applies no path threshold. The resulting tree probability `T`
preserves every ancestor's best single path, so recursive maximum `M <= T`.
Deleting edges from the original coupled independent cascade gives `T <= pi`.
Together with the already established upper bound, the conditional bracket is
`M <= T <= pi <= R <= H`. Thus `0 <= R - pi <= R - T <= R - M`.

The tree probability is exact only for its restricted stochastic process.
The proof does not make domain scores probabilities or make arbitrary pruning
a lower bound tighter than `M`. Computing a restricted tree separately for
each requested target takes additional work; reporting the tighter bracket
reuses it only where the tree comparator has already been run. The manuscript
credits related association bounds and MIA-inspired restrictions without
claiming the whole bracket as a first theorem.

## Proposed ranking analysis

The benchmark will count strict pairs whose GBBRPM order is opposite the
reference order. For sampled references, a reversal is called resolved only
when the relevant confidence intervals, intersected with the analytical
bracket when nonempty, establish the opposite order at the stated per-solve
coverage. Counts, denominators, the resolved fraction, and unresolved pairs
will accompany the rate. The analysis relates ranking changes to ancestry
overlap and selection regret without presuming that overlap causes every
discrepancy. Clipped-additive `H` stays as a baseline: being a looser nodewise
upper bound does not imply worse rankings.

## Scope and schedule

Section 3.4.2 now describes the engine-computed trace, optional replay, and
the distinction between scalar evaluation and display costs briefly.
Appendix E has been reduced to about 325 source words, preserving its
verification contract and recording the unresolved positive-infinity
validation issue and pending browser check. Those checks are proposals or
team reports, not new independent test results. Animation polish is secondary
to reference simulation, matched mechanism comparisons, and error analysis.

The prospective Express snapshot is targeted for acquisition and provenance
checking before the week-8 freeze. A newly acquired snapshot must be
distinguished from the missing historical raw data. If eligibility, source
identity, or DAG checks are incomplete, the conditional Express cases will be
omitted from the frozen main inventory and recorded as a limitation. The
generated graph benchmark will proceed. Preliminary pages still omit the
approval sheet and acknowledgments and retain an abstract placeholder.
