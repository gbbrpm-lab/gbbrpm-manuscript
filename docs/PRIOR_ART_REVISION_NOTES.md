# Prior-art revision notes — October 13, 2026

This pass follows the supplied prior-art assessment and the request to revise
the current proposal. It keeps the model equations, title/DAG scope, evaluation
engine distinction, preliminary results, and member-assigned timeline work.

## Sources checked

1. Klement, E. P., Mesiar, R., & Pap, E. (2004). Triangular norms. Position paper I:
   Basic analytical and algebraic properties. Fuzzy Sets and Systems, 143(1), 5–26.
   DOI: https://doi.org/10.1016/j.fss.2003.06.007
   Author-hosted full text:
   https://www.flll.jku.at/sites/default/files/44_2004_KMesPap_TNormsPosPaperI_FSSPrintedVersion.pdf
   Section 3, Definition 3.1 and Equations (14)–(16) support the established
   maximum, probabilistic-sum, and bounded-sum operators.

2. Fallet-Fidry, G., Weber, P., Simon, C., Iung, B., & Duval, C. (2012).
   Evidential network-based extension of Leaky Noisy-OR structure for supporting
   risks analyses. IFAC Proceedings Volumes, 45(20), 672–677.
   DOI: https://doi.org/10.3182/20120829-3-MX-2028.00183
   Publisher metadata was located; the publisher/HAL full-text routes were
   blocked. The full article uploaded by coauthor Philippe Weber was inspected:
   https://www.researchgate.net/publication/229476099_Evidential_network-based_extension_of_Leaky_Noisy-OR_structure_for_supporting_risks_analyses
   Sections 2.1–2.2 and the efficacy-parameter representation support the
   background-plus-parent conditional aggregation comparison. GBBRPM's B is
   an index input, not automatically a probabilistic leak.

3. Faraji, F., Mouratidis, H., & Al Zakwani, A. (2026). Risk impact pathway analysis
   (RIPA): A dynamic risk assessment framework for interdependent critical
   infrastructures. International Journal of Information Security, 25, Article 26.
   https://doi.org/10.1007/s10207-025-01201-1
   Publisher full text, Section 3.3, Equations (4)–(5), supports current-total-risk
   propagation through multiplicative modifiers and additive node aggregation.

This is a targeted primary-source check, not an exhaustive Scopus/Web of Science
search or a complete verification of every existing reference. Full papers are
not reproduced in this manuscript package.

## Changes by location

- Chapter 1: replaces the weak absence-of-combination framing with a testable
  design/evaluation question; explicitly credits the adopted operator; updates
  RQ3, Objective 3, significance, framework explanation, and aggregation definition.
- Chapter 2: adds t-conorm grounding, exact algebraic identification, conditional
  leaky noisy-OR and RIPA equations, and Table 2.2 comparing operator equivalence,
  architectural overlap, semantics, and evaluation needs.
- Chapter 2 closing gap: focuses on relation heterogeneity, accumulation,
  saturation, ranking, shared-origin sensitivity, and resource cost under matched
  inputs. It does not claim a first-of-its-kind model from a new name, DAG
  restriction, non-probabilistic label, prototype, or three-domain combination.
- Literature-gap figure: shows established mathematical/architectural precedents
  leading to the proposed evaluation question.
- Chapter 3: credits probabilistic-sum adoption and established properties;
  adds a matched bounded-aggregation protocol and updates objective alignment.
- References: adds the two verified aggregation/noisy-OR sources and the RIPA DOI.
  Existing citation style and entries are retained.
- README: identifies the new pass and its prospective experimental status.

## Planned aggregation protocol

The reference GBBRPM update remains the probabilistic-sum version.
Separately versioned maximum and bounded-sum conditions will be compared with it.

The operator-only analysis will use identical incoming vectors.
The end-to-end analysis will use identical graph, B, S, and tau, while each
variant recursively recomputes its own upstream states. The initial chain
control will contain a single source and no intermediate disturbance.
Independent convergence, local-plus-incoming terms, and reconvergence will
be examined separately.

Metrics will include paired node differences, terminal states, numerical
saturation fraction, Spearman agreement, and tie-aware top-k overlap.
These comparisons characterize behavior and tradeoffs; choosing an operator
for operational prioritization requires an independent reference outcome.
The new diagnostic runs will be counted outside the historical 136-run suite.

This editing pass does not implement or execute the new experiment runner.
The illustrative (0, 0.5, 0.5) values are direct algebraic examples, not results
from newly run domain experiments. The baseline equations and previously
reported numerical findings remain unchanged.

## Boundaries and follow-up

- Model naming remains permissible as identification of a specified model; it
  does not establish mathematical novelty.
- Separate S/tau labels do not create a different mechanism from their effective
  product without independent interpretation evidence.
- Negative SWMM agreement remains a scope limitation, not screening validation.
- Existing analytical properties are credited as inherited mathematics.
- Extend native-index searches and equation-level extraction before making any
  stronger novelty claim.
- The title, front-matter scope, three-chapter structure, archives, and timeline
  content remain as supplied. No Gantt chart was created.
- Final comparative protocol implementation, independent domain evidence, and
  institutional milestones remain work for the proposed study.

## Document verification

The updated source was compiled with pdfLaTeX/latexmk and checked for resolved
citations/references and overflow. The new equations, prior-art table, literature
figure, comparison protocol, and affected section pages were visually inspected.
Input/result files and preliminary appendix sources were checked against the
uploaded archive for unintended changes.
