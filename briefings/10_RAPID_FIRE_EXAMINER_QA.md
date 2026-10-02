# Briefing 10: Rapid-Fire Examiner Questions

## Prototype questions

### Why build a prototype if the thesis contribution is the model?

The prototype tests implementation feasibility and makes the model's inputs, validation rules, parameter changes, graph state, and rankings inspectable. It supports the model contribution without replacing its computational evaluation.

### Is the prototype production-ready?

No. Its core functions and production frontend build were verified, but it has not undergone formal usability, accessibility, security, concurrency, or deployment evaluation.

### Why is operational mode inactive?

Because no provenance-complete agency dataset has been mapped and independently verified. The inactive state prevents controlled fixtures from being presented as operational evidence.

## Model identity

### What is GBBRPM?

A deterministic bounded recursive architecture for comparative node-risk prioritization on directed acyclic graphs.

### Is `R` a probability?

No. It is a normalized non-probabilistic comparative index.

### What does “bounded” mean?

Every declared state and modifier lies in `[0,1]`, and the aggregation rule guarantees final node risk also lies in `[0,1]`.

### What is propagated?

The current accumulated upstream state `R_i`, modified by edge susceptibility and optional transmission.

### Can a source have local disturbance?

Yes. With no predecessors, the empty product equals one, so source risk equals its local disturbance.

### What happens when risks tie?

They retain equal standing. No unsupported tie-breaker is applied.

## Design choices

### Why a DAG?

It guarantees a deterministic topological order and one-pass computation. Cycles require a separately defined iterative or temporal mechanism.

### Why multiplicative-complement aggregation?

It is bounded, monotone, saturating, and can combine local and multiple incoming terms without post-hoc clipping.

### Is it noisy-OR?

It is algebraically related, but not interpreted probabilistically.

### Why separate susceptibility and transmission?

Susceptibility describes response under the evaluated condition; transmission describes how strongly influence transfers. Keeping them separate prevents conceptually different mechanisms from being hidden in one coefficient.

### Why is baseline tau equal to one?

Neutral transmission avoids inventing unsupported heterogeneous coefficients. Non-neutral uniform sweeps are sensitivity tests, not calibration.

### Why `S = min(1, L/C)`?

It is bounded, monotone, parameter-light, and traceable. It is a domain instantiation, not a universal susceptibility law.

## Experiment questions

### Why five synthetic networks?

They isolate linear propagation, branching, independent convergence, reconvergence, and mixed behavior.

### Why 136 scenarios?

That count comes from the declared architecture scenario families: 20 severity, 25 load stress, 36 location, 10 multi-source, and 45 intermediate-disturbance runs.

### Are there 179 total runs after Component 2?

Arithmetically, yes, but reporting one total would blur two protocols. The 136 runs test the generic architecture; the separate 43 runs test Component 2.

### Why 600 trials?

They provide repeated randomized checks under fixed-seed reproducibility. The study treats them as sampled computational evidence, not exhaustive proof.

### Why use Spearman and Jaccard?

Spearman measures overall rank agreement; Jaccard measures overlap among the highest-priority sets. They capture different stability questions.

### Why can Spearman stay high while Jaccard falls?

Most of the ordering may remain similar even when a few nodes cross the cutoff defining the top-priority set.

### Where can the complete step-by-step calculations be inspected?

Appendix A traces the generic architecture, Appendix B reproduces the Express software result at `tau = 0.50`, and Appendix C derives Component 2 susceptibility and reproduces the electrical risk sum of `1.186`. An operational drainage calculation remains pending real, provenance-complete inputs.

## Interpretation questions

### Why does downstream risk still increase after some S values reach one?

Clipping happens per edge. Other edges may remain below one and continue increasing, and their changed contributions propagate recursively downstream.

### Why can equal local disturbances produce different final risk?

Topology, upstream state, edge susceptibility, downstream reach, and convergence differ by location.

### Does high risk identify the cause of failure?

Not necessarily. It identifies high comparative modeled risk under the scenario. Causal attribution requires additional evidence.

### Does cross-domain testing prove generalizability?

No. It demonstrates instantiability in three selected cases. Broader generalization requires additional datasets and independent outcomes.

## Drainage questions

### Why did GBBRPM disagree with SWMM?

GBBRPM is downstream-only and does not model backwater, surcharge, ponding, or flow redistribution.

### Does disagreement invalidate the model?

It invalidates hydraulic-prediction interpretation, not the narrower comparative graph-risk role.

### Can it replace SWMM?

No.

## Software questions

### Does Express risk 0.9975 mean 99.75% exploit probability?

No. It is a saturated comparative index created by local and dependency contributions.

### Was tau calibrated from incidents?

No. The sweep tests attenuation sensitivity.

## Electrical questions

### Why Component 2?

It met pre-result feasibility criteria: authorized topology, synchronized source and terminal measurements, observable branches, useful structure, auditable exclusions, and DAG compatibility.

### Why only 12 modeled nodes from 13?

One branch lacked a supported downstream meter path. Excluding it was more honest than inventing loading or treating missing observation as zero.

### Why only 24 snapshots?

They support a short synchronized descriptive baseline, not temporal or event generalization.

### Why not allocate the 9.129 kW residual?

No evidence showed where it belonged. Allocation would add an unsupported spatial assumption.

### Why B equals zero initially?

The measurements represent normal operation without verified event labels. Controlled scenarios inject disturbance explicitly.

### Does Component 2 validate event prediction?

No. It validates controlled mechanism response on real topology and measured loading.

## Contribution questions

### What is novel?

The explicit integrative architecture, state semantics, separation of roles, controlled validation, dependence diagnostic, and evidence-aware cross-domain instantiation.

### What is not novel?

Graphs, recursion, susceptibility, multiplication, bounded aggregation, and ranking individually.

### What is the thesis's safest contribution statement?

GBBRPM provides a traceable bounded comparative-risk architecture whose intended computational behavior is supported on controlled DAGs and whose core roles can be instantiated coherently in three tested domains within explicitly different evidence limits.
