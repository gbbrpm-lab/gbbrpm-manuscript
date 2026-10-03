# Briefing 09: Conclusions, Limitations, and Recommendations

## Answers to the research questions

### RQ1: Integration

The architecture integrates local disturbance, current upstream risk, susceptibility, optional transmission, directed reachability, and multiple incoming contributions using topological evaluation and multiplicative-complement aggregation.

### RQ2: Mathematical behavior

The model preserved bounds and monotonicity in controlled scenarios and all 600 randomized property trials. Ranking changed coherently when severity, susceptibility, and location changed.

### RQ3: Sensitivity, robustness, and scalability

The model responded materially to severity, susceptibility, topology, location, and multi-source configuration. Overall ranking remained comparatively stable under modest perturbation, while top-set membership was more sensitive. Runtime growth was consistent with one-pass sparse-DAG evaluation.

### RQ4: Cross-domain instantiation

The frozen update rule was instantiated without redefinition in drainage, software dependency, and electrical networks. Parameter meanings changed, but the roles of `B`, `S`, `tau`, `Q`, and `R` remained fixed.

### RQ5: Research prototype

The validated workflow was implemented through a common node-and-edge contract, graph validation, controlled parameter editing, the pinned model engine, network visualization, and comparative rankings. Functional checks reproduced preserved outputs and rejected invalid graphs.

### RQ6: Evidence boundaries

- drainage: controlled behavior and hydraulic-reference boundary;
- software: real-topology structural and transmission-sensitivity evidence;
- electrical: preprocessing verification and controlled real-topology, measured-loading sensitivity.

The cases do not provide equal predictive evidence.

## Main conclusions

1. GBBRPM is deterministic, bounded, and interpretable at the level of its declared terms.
2. Network context and heterogeneous relations can change prioritization beyond local scoring.
3. Broad ranking is robust under modest uncertainty, but top-priority membership becomes less stable as uncertainty grows.
4. The frozen rule is coherently instantiable in the tested domains.
5. SWMM disagreement demonstrates that GBBRPM should not replace hydraulic simulation.
6. Component 2 strengthens electrical mechanism evidence but does not complete event validation.
7. The prototype demonstrates implementation feasibility and traceability, not production readiness or operational validation.

## Limitations

### Model limitations

- DAG-only formulation;
- no cycles, feedback, or bidirectional influence;
- no explicit temporal dynamics;
- comparative index rather than calibrated probability;
- no common-cause or ancestry correction in the v1 aggregator; and
- domain mappings depend on evidence quality.

### Drainage limitations

- controlled and reconstructed inputs;
- SWMM rather than operational field outcomes;
- downstream-only formulation omits hydraulic redistribution.

### Software limitations

- advisory-based evidence rather than observed incidents;
- severity mapping and transmission sweep are not exploit calibration.

### Electrical limitations

- Component 2 selected purposively rather than randomly;
- only 24 aligned snapshots for the controlled baseline;
- one unobserved branch excluded;
- residual not spatially allocated;
- no event-aligned labels or independent outcomes; and
- no statistical generalization to the full grid.

### Prototype limitations

- no formal user or accessibility study;
- no authentication, persistent storage, or deployment hardening;
- no concurrent multi-user evaluation; and
- operational mode remains inactive until a documented dataset adapter is available.

## Recommendations linked to limitations

1. Obtain event-aligned electrical measurements and independent outcomes.
2. Test domain rankings against outcomes not used to construct model inputs.
3. Obtain operational drainage observations with complete provenance.
4. Develop ancestry-aware or dependence-aware aggregation.
5. Calibrate susceptibility and transmission separately by domain.
6. Design explicit cyclic, bidirectional, or temporal extensions.
7. Repeat cross-domain protocols on additional datasets and components.
8. Conduct prototype usability testing and production hardening before operational use.

## Safe final conclusion

> GBBRPM is supported as a bounded comparative-prioritization architecture with controlled behavioral evidence and cross-domain instantiability. It is not supported as a universal predictor, hydraulic simulator, exploit probability model, or completed electrical-event predictor.

## Likely examiner questions

### “What is the most serious limitation?”

The most structural limitation is dependence under shared-origin reconvergence, because local aggregation can combine related contributions as if they were separate paths. The most empirical limitation is the lack of independent operational outcomes for drainage and electrical event validation.

### “What should be done first after this thesis?”

Obtain outcome-aligned domain data and test whether the produced rankings correspond to independent observed consequences. Model extensions should remain separate from validation of v1.

### “Can this be deployed now?”

It can be used experimentally as a transparent comparative screening tool when inputs are defensible. Operational deployment would require domain calibration, outcome validation, governance thresholds, and monitoring of input quality.
