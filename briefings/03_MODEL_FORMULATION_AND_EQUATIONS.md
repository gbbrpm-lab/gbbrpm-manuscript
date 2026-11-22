# Briefing 03: Formulation and Conditional Benchmark Bracket

**Status: specified mathematics; full empirical benchmark remains planned.**

## Domain-index core

For a DAG `G=(V,E)`, let `P(j)` be the predecessors of j. All supplied B, S, and tau values are finite and in [0,1].

`w_ij = S_ij * tau_ij`

`Q_ij = w_ij * R_i`

`R_j = 1 - (1 - B_j) * product[i in P(j)](1 - Q_ij)`

B is local disturbance; S is relation-specific susceptibility; tau is optional transmission (neutral baseline 1 where permitted). R_i is the **current accumulated** upstream state. S and tau have different intended roles, but outputs identify only their product unless independent information distinguishes them.

Evaluate once in topological order. This order expresses computational dependence, not physical time. R is a dimensionless comparative index in domain cases, not a calibrated probability. Branching does not conserve a physical quantity that must be divided among outgoing edges.

For a source or isolated node, the empty product is 1, hence `R_j=B_j`, not automatically 1. A node may have both local and incoming disturbance. Every Q and R remains in [0,1], and increasing an independent primitive input on a fixed graph cannot decrease node states. Rankings can nevertheless change.

The update is the established probabilistic-sum t-conorm. Boundedness does not correct shared-origin dependence. `S=1` does not imply `R=1`; it only removes susceptibility attenuation on that edge.

## Small core calculation

With source states 0.60 and 0.30, susceptibilities 0.50 and 0.40, tau=1, and receiver local input 0.10:

`R_receiver = 1 - 0.90 * 0.70 * 0.88 = 0.4456`.

A later edge with S=0.75, tau=1, and no receiver local input gives `R_next=0.3342`. Appendix A supplies the complete trace. These are worked arithmetic, not benchmark findings.

## Separate stochastic reference

Only in this benchmark, B specifies initial Bernoulli probabilities and w specifies conditional Bernoulli edge-transmission probabilities:

`Z_j ~ Bernoulli(B_j)`; `E_ij ~ Bernoulli(w_ij)`.

`X_j = Z_j OR any_i(X_i AND E_ij)`; `pi_j = Pr(X_j=1)`.

All primitive Z and E draws are mutually independent. Derived node events may be dependent. Each primitive is drawn once per trial and reused through all of its consequences. Conditional transmission uses **w, not Q**; sampling X_i and then transmitting with w*R_i would count the upstream marginal twice.

## Conditional bracket

| Symbol | Meaning |
|---|---|
| M | Recursive maximum: `max(B_j, max_i(w_ij*M_i))` |
| T | Exact target marginal on the specified restricted in-arborescence |
| pi | Exact activation marginal in the full declared process |
| R | Ordinary complement-product recursion |
| H | Recursive clipped addition: `min(1, B_j + sum_i(w_ij*H_i))` |

Under the finite-DAG and independent-primitive assumptions:

`M_j <= T_j <= pi_j <= R_j <= H_j`.

The restricted tree must preserve one consistently chosen maximum-weight path from every positive-path ancestor, the original local terms and weights, and the target, with no positive-path threshold. Arbitrary pruning does not inherit `T>=M`. Edge deletion gives `T<=pi`; disjoint incoming primitive subtrees make tree evaluation exact. The R upper bound follows established positive association and topological induction.

Consequently `0 <= R-pi <= R-T <= R-M` when T is computed. Target-specific trees have additional construction/evaluation cost. `T_a>R_b` certifies `pi_a>pi_b`; `M_a>R_b` is a cheaper sufficient certificate. Overlapping brackets are inconclusive. Pointwise bound ordering does not guarantee ranking superiority.

These guarantees do not apply to domain probabilities, dependent primitives, cycles, arbitrary cascade mechanisms, or the ancestry-grouping diagnostic. The manuscript credits established bounding arguments rather than claiming a first theorem.

## Shared-origin control

For m edge-disjoint branches, each with path product `u=p^ell`, shared source probability b gives `pi_shared=b*(1-(1-u)^m)`. Independent origins with matching branch-start marginals give `pi_independent=1-(1-b*u)^m`. GBBRPM gives the second expression in both cases.

For two branches the shared-origin slack is `b*(1-b)*u^2`. At b=0.5 and u=1, pi=0.5 and R=0.75. At b=1 and u=0.25, both equal 0.4375, whereas retaining one strongest branch gives 0.25. Shared ancestry alone therefore does not force positive slack, and pruning is not automatically a correction.

Sources: Chapter 3 formulation; `chapters/benchmark_bound.tex`; `chapters/reference_benchmark.tex`.
