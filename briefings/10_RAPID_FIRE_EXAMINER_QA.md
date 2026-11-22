# Briefing 10: Proposal Examiner Q&A

**Answers follow Chapters I–III; benchmark experiments remain planned.**

### What is GBBRPM now?

Graph-Based Bounded Risk Propagation Model: the proposed bounded receiving-state index on DAGs. The earlier blockage framing was its drainage origin.

### What is the principal research question?

When the recursion gives accurate receiving-state rankings under a declared reference, how shared origins affect that agreement, and what accuracy–cost tradeoffs alternatives provide.

### What is complete?

The formulation, manuscript proposition, worked calculations, selected exploratory evidence, and verified Express input record exist. The proposed full benchmark and new comparator evaluation are not complete.

### Does the model produce probabilities?

Domain outputs are indices. Only the separate benchmark assigns probabilistic meanings to B and w and evaluates R against pi under explicit assumptions.

### Why sample edges using w rather than Q?

The trial already samples upstream activation. Conditional transmission is w=S*tau; multiplying by R again would count upstream activation twice.

### What does the bracket say?

Under mutually independent local/edge primitives on a DAG, M<=T<=pi<=R<=H. R is an upper bound, T is a restricted-process lower bound, and R-T is a tighter certificate than R-M when the specified tree is computed.

### Is that bracket a new theorem?

The manuscript presents a DAG specialization using established association and aggregation arguments, with explicit MIA and Abbe et al. precedents. A first-ever claim has not been established.

### Is the restricted tree just the strongest incoming edge?

No. It retains consistent maximum-weight paths from every positive-path ancestor to one target, preserves local terms and weights, and uses no positive-path threshold. It aggregates retained independent subtrees exactly. It needs a tree per target.

### Is it the same as MIA or LDAG?

It adapts MIA's tree restriction for receiving queries, not the full seed-selection algorithm. LDAG uses Linear Threshold semantics and a different recurrence.

### Which published-bound implementation is required?

The Abbe et al. (2020) DAG lower recurrence after encoding local starts via an auxiliary certain seed. No ordering relative to M or T is assumed. Their full upper algorithm is discussed but not required on the full grid.

### Does a tighter upper bound rank nodes better?

Not necessarily. Unequal slack can reverse ordering. Fixed-budget capture, regret, and resolved reversals will test the ordering effects.

### Is shared ancestry always an error?

No. In the matched family a certain common source can still produce exact complement-product results through independent branch edges. Source uncertainty and attenuation matter.

### Will ancestry grouping fix the model?

That is unproven. It may discard valid edge opportunities or merge partially overlapping lineages. It will be evaluated as a diagnostic with its own states and measured cost.

### Why exclude positive-B nodes from benchmark ranking candidates?

To prevent supplied local disturbances from trivially dominating the receiving-state selection task. Unreachable zero-B nodes remain candidates.

### How do ties work at a fixed budget?

Select exactly k and average over 100 shared outcome-independent seeded permutations. Expanded cutoff-tie sets are used only for separately labeled descriptive overlap.

### What does a zero Monte Carlo count mean?

No activation was observed in that sample, not proof of zero true probability. Report intervals and retain unresolved differences.

### How many planned scenarios are there?

560 branch controls, 3,600 uniform generated-DAG scenarios, 144 secondary heterogeneous scenarios, and 12 Express scenarios: 4,316 before feasibility amendments. The 48 extra precision solves revisit existing scenarios.

### Are the 136 and 43 counts included?

No. They describe separate historical exploratory configurations proposed for reviewed reruns, not the new reference inventory.

### Why development and evaluation graphs?

Development validates and refines implementation; held-out graphs assess the frozen protocol. A redesigned method requires unused cases for a confirmatory claim.

### Has the full workload been shown feasible?

No. A staged development-only pilot will measure throughput and memory. The billion-scale edge-trial counts are estimates of work, not measured runtime. Amendments must be frozen before held-out outcomes.

### Are the original Express inputs missing?

No. They are included and hash-verified. Earlier N1–N5 fixture inputs remain a separate reconstruction-provenance issue.

### Does real topology make the Express benchmark incident validation?

No. It uses controlled B and w on real topology. Advisory severities are index inputs, not calibrated exploit probabilities or independent incident labels.

### What does Component 2 show?

A preliminary controlled instantiation on real topology and measured normal-operation loading. Its arborescence does not test reconvergence and its injected disturbances do not validate event prediction.

### What does the unfavorable SWMM comparison imply?

It does not support hydraulic ranking equivalence in that exploratory protocol. It neither isolates every hydraulic cause nor validates maintenance utility.

### Is GBBRPM lightweight?

Its prepared-input scalar DAG pass is O(V+E); full sorting adds O(V log V). Measure resource, adapter, tree/diagnostic, and reference costs separately before stronger efficiency claims.

### Can the prototype be called fully verified?

No. Earlier checks and revision eafec4d are preliminary/team-reported. Matching-source regressions and browser inspection remain required, including reported non-finite-input handling.

### What if operational domain data never arrive?

Complete the independently specified controlled benchmark and supporting mappings, and limit practical claims accordingly. Missing observations cannot be replaced with invented field data.

### What would count as a useful final result?

A reproducible account of bound tightness, selection quality, dependence regimes, costs, and failures beyond what the prior methods already establish. A positive performance claim is not required for an honest result.
