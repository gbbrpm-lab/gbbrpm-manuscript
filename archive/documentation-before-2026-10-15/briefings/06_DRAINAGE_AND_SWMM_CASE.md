# Briefing 06: Drainage and SWMM Case

## Role of the drainage case

Drainage provides the most complete behavioral case because it includes:

- the N1--N5 controlled networks;
- drainage-motivated `L/C` susceptibility;
- 136 controlled scenarios;
- robustness and dependence diagnostics; and
- a 12-scenario SWMM external-reference comparison.

## Drainage parameter meaning

- nodes: junctions or modeled locations;
- edges: directed downstream relations;
- `B`: local blockage or disturbance severity;
- `L`: edge load;
- `C`: effective capacity;
- `S = min(1, L/C)`: operating susceptibility; and
- `R`: bounded comparative node-risk index.

These meanings instantiate the generic roles; they are not universal definitions for every domain.

## SWMM comparison protocol

For blocked conduit area loss `a`, effective capacity becomes:

`C'_ij = (1 - a) * C_ij`

GBBRPM positive risk changes are compared with positive SWMM changes in:

- node maximum depth; and
- node flooding volume.

Metrics:

- mean scenario-level Spearman rank correlation;
- top-20% Jaccard overlap; and
- hydraulic worsening outside the target-and-descendant region modeled by downstream-only GBBRPM.

## SWMM results

| Hydraulic outcome | Mean Spearman | Top-20% Jaccard | Outside-scope share |
|---|---:|---:|---:|
| Maximum depth | -0.416 | 0.119 | 71.2% |
| Flooding volume | -0.485 | 0.000 | 40.5% |

## Interpretation

The negative correlations and low overlap mean the nodes prioritized by GBBRPM generally differed from those with the largest SWMM hydraulic worsening.

This does not mean the experiment is useless. It establishes a crucial boundary:

- GBBRPM represents directed downstream comparative propagation;
- SWMM represents hydraulic mechanisms such as backwater, surcharge, ponding, and flow redistribution.

Large outside-scope shares confirm that important hydraulic consequences can occur outside the strictly downstream region used by GBBRPM.

## The correct conclusion

> GBBRPM should not be used as a substitute for hydraulic simulation. It is better positioned as a lightweight screening and prioritization layer that can indicate where further inspection or higher-fidelity analysis may be warranted.

## What drainage evidence supports

- controlled mechanism behavior;
- susceptibility and location sensitivity;
- bounded multi-source response;
- robustness and ranking analysis;
- reconvergence limitation diagnosis; and
- a documented boundary against hydraulic outcomes.

## What it does not support

- field-validated flood prediction;
- calibrated hydraulic state estimation;
- replacement of SWMM;
- modeling of backwater or bidirectional effects; or
- universal drainage parameter calibration.

## Likely examiner questions

### “Does negative correlation mean GBBRPM failed?”

It failed only if the intended claim were hydraulic prediction, which the thesis explicitly rejects. The comparison successfully identifies the boundary between graph-based prioritization and hydraulic state reproduction.

### “Why compare with SWMM if the outputs are different?”

The comparison tests whether their prioritizations align and prevents unsupported hydraulic claims. It is a scope-validation exercise rather than numerical equivalence testing.

### “Could GBBRPM still be useful in drainage?”

Yes, as a lightweight downstream screening and comparative prioritization layer, especially when full hydraulic modeling is unavailable or reserved for shortlisted locations.

### “What evidence is still missing?”

Provenance-complete operational drainage observations and independent field outcomes are still needed.

