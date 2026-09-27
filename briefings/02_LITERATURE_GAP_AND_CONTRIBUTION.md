# Briefing 02: Literature Gap and Contribution

## Literature progression

The review moves through three evidence streams:

1. **Local condition assessment** — blockage, debris, vulnerability, or component-level evidence.
2. **Graph-based prioritization** — centrality, critical paths, weakest links, capacity, and functional importance.
3. **Propagation-model families** — influence diffusion, epidemics, cascading failure, attack graphs, cyber risk, and infrastructure contagion.

These streams contain mechanisms relevant to GBBRPM, but they answer different questions and propagate different states.

## Why existing model families are not direct substitutes

| Family | Typical propagated meaning | Why it is not directly interchangeable with GBBRPM |
|---|---|---|
| Independent Cascade / Linear Threshold | Activation | Usually binary or threshold-based rather than a continuous comparative risk state |
| SIR / SEIR | Epidemiological compartment | Includes domain-specific transition and recovery semantics |
| Cascading failure | Load, overload, or failure | Often relies on redistribution, failure thresholds, or physical conservation |
| Attack graphs | Reachable compromise or probability | Uses security-path and conditional-compromise semantics |
| Centrality | Structural importance | Does not recursively update a current disturbance state |
| Hydraulic simulation | Physical hydraulic state | Models backwater, surcharge, ponding, and redistribution beyond a downstream graph index |

The thesis therefore compares these models conceptually, not by treating their numerical outputs as equivalent labels.

## The research gap

The gap is not that no propagation model exists. The gap is that, within the reviewed literature, no clearly established lightweight formulation combines all of the following under one explicit comparative-risk semantics:

- bounded continuous non-probabilistic node state;
- current-state recursive propagation;
- directed reachability;
- explicit separation of susceptibility and optional transmission;
- local disturbance at receiving nodes;
- bounded aggregation of converging contributions; and
- explicit recognition that shared paths create dependence limitations.

## Novelty statement to use

> The study does not claim that its individual mathematical mechanisms are independently novel. Its contribution is their explicit integration into a traceable bounded comparative-risk architecture, together with controlled evaluation and cross-domain evidence separation.

## Why the multiplicative complement is appropriate

The operator is suitable because it:

- remains bounded in `[0,1]`;
- is monotone in every genuine contribution;
- allows local and incoming terms to coexist;
- supports multiple simultaneous inputs; and
- saturates instead of growing without limit.

Its algebra resembles noisy-OR, but the thesis does not assign probabilistic semantics because the inputs are normalized risk contributions rather than calibrated probabilities.

## “More interpretable than hydraulic simulation?”

Avoid making this an absolute superiority claim. The defensible statement is:

> GBBRPM is directly traceable at the level of its declared terms—local disturbance, upstream state, susceptibility, transmission, and aggregation—while hydraulic simulation represents richer physical behavior. The two models answer different questions.

Hydraulic models may also be interpretable, but their state variables and mechanisms are more physically detailed. GBBRPM's advantage is lightweight traceability for comparative prioritization, not universal interpretability superiority.

## Likely examiner questions

### “Is this just noisy-OR?”

The aggregation form is related algebraically, but the thesis contribution is the complete architecture and its non-probabilistic state semantics. The study also explicitly analyzes shared-origin dependence, which prevents treating the terms as independent probabilities.

### “Why not just use centrality?”

Centrality is structural and usually scenario-independent. GBBRPM combines structure with current local disturbance and heterogeneous relation conditions, so rankings may change between scenarios.

### “Why not use a graph neural network?”

A GNN would answer a learned prediction question and require labels, training data, and generalization assessment. GBBRPM targets a deterministic, transparent comparative index when such labeled data may be unavailable.

### “What is genuinely new?”

The explicit combination and separation of roles, bounded current-state recursion, controlled validation protocol, dependence diagnostic, and evidence-aware cross-domain instantiation—not the isolated invention of multiplication, graphs, or ranking.

