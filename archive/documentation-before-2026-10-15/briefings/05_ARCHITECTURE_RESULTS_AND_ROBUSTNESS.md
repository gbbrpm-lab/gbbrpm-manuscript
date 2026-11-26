# Briefing 05: Architecture Results, Robustness, and Scalability

## Baseline behavior

| Network | Maximum risk | Mean risk | Outlet risk | Main interpretation |
|---|---:|---:|---:|---|
| N1 | 0.800000 | 0.249493 | 0.053760 | Strong attenuation along a chain |
| N2 | 0.800000 | 0.465250 | 0.408000 | High-susceptibility branches retain downstream risk |
| N3 | 0.700000 | 0.420205 | 0.106814 | Bounded convergence from independent sources |
| N4 | 0.800000 | 0.579719 | 0.351372 | Reconvergence increases downstream state |
| N5 | 0.816448 | 0.632660 | 0.708640 | Mixed mechanisms elevate internal nodes |

In the N5 baseline, the top three are `N13 > N19 > N16`, showing that neither the source nor the outlet must rank highest.

## Source-severity response

All networks showed monotone outlet response as selected source severity increased from `0.25` to `1.00`.

Ranking was not always fixed:

- N1 and N2 retained their top-three ordering;
- N3, N4, and N5 changed ordering; and
- N5 outlet change was relatively small because other active disturbances already contributed to its baseline state.

Interpretation: monotonicity of values does not imply invariance of rankings.

## `L/C` stress response

Scaling edge loads and recomputing clipped susceptibility changed risk magnitude and ranking. When one edge reaches `S = 1`, it saturates individually, but other unsaturated edges can still change. Recursive downstream states can therefore continue increasing after some edges have clipped.

## Location sensitivity

Equal local severity `B = 0.75` produced wide outlet-risk ranges:

| Network | Lowest outlet risk | Highest outlet risk | Range |
|---|---:|---:|---:|
| N1 | 0.050400 | 0.600000 | 0.549600 |
| N2 | 0.000000 | 0.750000 | 0.750000 |
| N3 | 0.000000 | 0.487500 | 0.487500 |
| N4 | 0.000000 | 0.562500 | 0.562500 |
| N5 | 0.058820 | 0.619410 | 0.560590 |

This directly supports the claim that local severity alone is insufficient for network-level prioritization.

## Multi-source response

In N3, the outlet risks were:

- source A only: `0.056306`;
- source B only: `0.073734`; and
- sources A+B: `0.106814`.

In N5, all three sources produced outlet risk `0.708640`. The bounded aggregator allowed contributions to coexist without exceeding one, but this does not establish probabilistic independence.

## Intermediate disturbance

The largest tested outlet responses included:

- N1: `0.613440` for `E = 0.75`;
- N2: `0.852000` for `H = 0.75`; and
- N5: `0.852160` for `N19 = 0.75`.

This family demonstrates that a node can combine inherited risk with a newly introduced local disturbance.

## Comparator evidence

N5 agreement with heterogeneous GBBRPM:

| Comparator | Spearman | Top-three Jaccard |
|---|---:|---:|
| Local only | 0.108627 | 0.0 |
| Uniform `S = 0.25` | -0.042105 | 0.0 |
| Uniform `S = 0.50` | 0.150376 | 0.0 |
| Uniform `S = 0.75` | 0.696241 | 0.5 |

Low local-only agreement shows that propagation changes prioritization. Varying agreement across uniform conditions shows that heterogeneous edge patterns also matter.

## Robustness

| Perturbation | Mean Spearman | Mean top-three Jaccard |
|---|---:|---:|
| `+/-5%` | 0.979190 | 0.744500 |
| `+/-10%` | 0.938267 | 0.546667 |
| `+/-20%` | 0.845552 | 0.388833 |

Broad ordering remains comparatively stable, but membership among the highest-priority nodes is more sensitive. Do not summarize robustness using Spearman alone.

## Mathematical property tests

All 600 randomized trials passed each declared property:

- boundedness;
- monotonicity;
- full local disturbance; and
- zero-susceptibility gating.

These tests support implementation consistency over sampled cases, not a proof of correctness for every possible future extension.

## Reconvergence and dependence

| Network | Maximum overlap inflation | Outlet GBBRPM | Outlet path-pruned |
|---|---:|---:|---:|
| N3 | 0.000000 | 0.106814 | 0.106814 |
| N4 | 0.189280 | 0.351372 | 0.252000 |
| N5 | 0.439353 | 0.708640 | 0.386003 |

N3 convergence comes from independent source branches. N4 and N5 contain shared-origin reconvergence, where ordinary local aggregation may count related ancestry through multiple paths.

## Scalability

Median runtime increased from approximately:

- `1.63 ms` at 20 nodes and 60 edges; to
- `16.65 ms` at 1000 nodes and 3000 edges.

The observed trend is consistent with one-pass `O(|V| + |E|)` evaluation on sparse DAGs. Runtime values remain environment-dependent.

## Strongest architecture conclusion

GBBRPM behaves consistently with its declared bounded and monotone semantics, responds materially to topology and heterogeneous conditions, remains broadly rank-stable under modest perturbation, exposes a clear reconvergence limitation, and is computationally lightweight on the tested sparse DAGs.

