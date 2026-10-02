# Briefing 07: Software-Dependency Case

## Purpose

The software case tests whether the frozen GBBRPM roles can be instantiated on a real non-physical directed dependency graph without changing the update rule.

## Dataset and graph

- target package: Express 4.18.2;
- nodes: 71 packages;
- edges: 128 directed dependency-to-dependent relations;
- evidence-backed affected versions: 7 packages.

## Local disturbance mapping

Advisory severity is mapped to bounded `B` values:

| Package | Severity | B |
|---|---|---:|
| body-parser | High | 0.75 |
| path-to-regexp | High | 0.75 |
| express | Moderate | 0.50 |
| qs | Moderate | 0.50 |
| cookie | Low | 0.25 |
| send | Low | 0.25 |
| serve-static | Low | 0.25 |

This mapping is a transparent controlled severity encoding, not exploit probability.

## Transmission sweep

Uniform `tau` values: `0`, `0.25`, `0.50`, `0.75`, and `1.00`.

| tau | Express risk | Express rank | Maximum network risk |
|---:|---:|---:|---:|
| 0.00 | 0.5000 | 3 | 0.7500 |
| 0.25 | 0.7673 | 2 | 0.7812 |
| 0.50 | 0.9118 | 1 | 0.9118 |
| 0.75 | 0.9766 | 1 | 0.9766 |
| 1.00 | 0.9975 | 1 | 0.9975 |

Express reaches rank one by `tau = 0.50`. Ranking agreement with the `tau = 1` reference remains extremely high, and top-20% Jaccard remains `1.0` throughout.

**Worked-calculation reference:** Appendix B independently traces the nonzero dependency contributions, intermediate-node recursion, and bounded aggregation that reproduce `R_Express = 0.9118` at `tau = 0.50`.

## Interpretation

As transmission increases, more dependency risk reaches packages that depend on the affected packages. Express accumulates several incoming dependency contributions and approaches saturation.

The sweep demonstrates expected attenuation sensitivity. It does not calibrate the true probability that a dependency vulnerability will be exploited or compromise Express.

## What the software case supports

- coherent mapping of the frozen architecture to a real dependency topology;
- evidence-backed local disturbance inputs;
- controlled transmission sensitivity;
- traceable accumulation at a dependent package; and
- cross-domain structural instantiability.

## What it does not support

- future exploit prediction;
- compromise probability;
- incident forecasting;
- empirical calibration of `tau`; or
- causal proof that a dependency advisory compromises Express.

## Likely examiner questions

### “Why direct edges from dependency to dependent?”

That direction represents the modeled influence pathway: evidence at a dependency may affect the package that relies on it. Direction must follow the risk-transfer interpretation, not merely package-manager display conventions.

### “Why is Express locally disturbed if it also receives propagated risk?”

Express has its own evidence-backed advisories, so it legitimately has local `B = 0.50` while also receiving contributions from vulnerable dependencies. The architecture was designed to combine both.

### “Why does Express approach one?”

Several nonzero contributions combine with its local disturbance through the saturating multiplicative complement. The value is a high comparative index, not near-certain exploitation.

### “Why is ranking already similar at tau = 0?”

The same seven local disturbances already determine much of the ordering. Increasing transmission changes accumulated magnitudes and elevates Express while leaving much of the broader ordering stable.
