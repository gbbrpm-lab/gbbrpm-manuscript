# Briefing 07: Software Inputs and Planned Express Benchmark

**Verified inputs and historical calculations exist; the 12 new stochastic scenarios are planned.**

The original Express 4.18.2 case contains 71 package/version nodes and 128 edges. Direction is **dependency to dependent**, so influence reaches consuming packages. The preserved dependency response uses the source convention; the CSV direction is checked against it.

## Included originals

`data/software/express_4.18.2/` contains nodes/edges CSVs, dependency JSON, OSV snapshot, case manifest, and input-verification record. The original CSV hashes match the historical paper-output manifest. The source records support seven advisory-origin identities, including Express itself.

From the manuscript root run:

```bash
python3 scripts/verify_express_inputs.py
```

This checks input identity, endpoints, direction, acyclicity, and advisory-origin consistency. It does not execute a stochastic benchmark, validate current incident outcomes, or authenticate the separate reconstructed N1–N5 fixtures. Reacquiring Express originals is no longer an outstanding task.

## Two distinct uses of this topology

| Use | Inputs and status | Interpretation |
|---|---|---|
| Preliminary index calculation | Advisory severity mapped to B; S=1; historical tau sweep {0,0.25,0.50,0.75,1} | Comparative index response, not exploit probability |
| Planned stochastic topology benchmark | Seven verified advisory identities receive controlled B=0.5 or 1; other nodes B=0; six declared uniform weights | 12 future scenarios against the independent-primitive process on real topology |

Do not treat advisory severities as Bernoulli probabilities. The planned experiment uses advisory identities to locate controlled initial terms, including the root where applicable. It does not import severity values as calibrated probabilities.

Appendix B traces the historical tau=0.50 index calculation, giving Express R approximately 0.9118. Appendix D retains the historical root range 0.5000 to 0.9975 across the transmission sweep. These values are preliminary index calculations, not results of the 12 planned benchmark scenarios.

Shared `qs` and `send` paths reconverge. Stable root rank does not quantify dependence slack. The controlled stochastic reference will support that evaluation under its own assumptions.

W8 will confirm selected hashes, mappings, and scenario eligibility before protocol freezing. Express results remain separate from generated-graph averages. Cyclic dependency input is rejected; component condensation would require separately defined node semantics. Independent incident prediction is not established.

Sources: Chapter 3 software and reference sections; Appendix B; Appendix D; `docs/INPUT_PROVENANCE_UPDATE.md`.
