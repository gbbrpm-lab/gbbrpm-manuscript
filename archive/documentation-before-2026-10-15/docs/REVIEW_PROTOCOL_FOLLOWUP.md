# Follow-up to the compute, prior-art, heterogeneity, and prototype review

These are proposal specifications. The benchmark and the proposed prototype
regressions were not executed by this manuscript edit.

## Computational pilot

The primary inventory remains 560 exact branch scenarios and 3600 generated
DAG scenarios, with 48 additional million-trial reference solves. Since the
generated graphs have `2|V|` edges, a literal edge-by-edge reference pass
has `3 * 25 * 6 * 2 * 100000 * 2 * (20+50+100+250) = 75.6 billion`
possible edge-trial checks. The audit adds `10.08 billion`. This is a scale
estimate, not a forecast of running time. Chapter 3 specifies a
development-only staged pilot across family, size, attenuation, local input,
and heterogeneity; records throughput, memory, and solver/tree costs; and
requires a revised grid and interval widths to be frozen before held-out
results if the original compute allocation is insufficient. An optimized
implementation must preserve the same independent-primitive semantics.

## Existing bounds and novelty

Abbe, Kulkarni, and Lee (2020), *JMLR* 21(31), 1--36, extends their 2017
nonbacktracking bounds paper. Section 3.1 defines a nodewise upper bound
from length-indexed, complement-product messages before summing it into
expected influence. Section 4.1 defines a nodewise lower recursion on a
directed acyclic subnetwork and states linear complexity for that lower
algorithm. The manuscript now acknowledges both; describing the earlier
work solely as aggregate influence would miss its nodewise constructions.
The fixed-seed input can also represent independently random local starts
via one always-active auxiliary source and independent edges. Different
input terminology alone is not a novelty argument. No relative tightness
or runtime ordering between the published bounds and the proposed bracket
is asserted without a matched implementation and cost boundary. Chapter 3
now plans to run the journal's directed-acyclic-subnetwork lower recurrence
on that auxiliary-source graph as a published nodewise comparator. Its
formula and subnetwork deletion are to be checked against exact fixtures,
and its cost reported separately. The journal's length-indexed upper
algorithm is discussed at equation level and is not a mandatory full-grid
baseline for this proposal.

Primary source: https://jmlr.org/papers/v21/18-112.html

## Controlled heterogeneity

The additional synthetic subset fixes the same graph and sources as paired
uniform `w=0.20` conditions. It uses development seed 41 and five
prespecified evaluation seeds per family/size, both local-source settings,
and a mean-preserving edge allocation: one quarter 0.10, one half 0.20,
one quarter 0.30. The assignment is defined before outcomes by a stable
hash of graph and edge identifiers. Counts are `3 * 4 * 6 * 2 = 144`:
24 development and 120 evaluation. At 100,000 trials, the added reference
stage represents 3.024 billion possible edge-trial checks. Five evaluation
graphs per family/size limit inference. This benchmark tests synthetic
effective-weight heterogeneity; separate N1--N5 cases still address how
domain information is constructed. Neither test identifies `S` and `tau`
from outputs or calibrates domain probabilities.

## Prototype boundary

Appendix E retains the team-reported positive-infinity to HTTP-500 issue as
unresolved until reproduced and corrected in matching application source.
Finite-number checks for load and capacity, expected client validation
responses, and regression fixtures for NaN and both infinity signs precede
a demonstration. Additional replay effects have no role in the mechanism
comparison. No new application fix or browser verification is claimed here.
