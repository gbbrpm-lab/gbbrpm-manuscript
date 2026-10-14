# Preserved Express 4.18.2 inputs

This directory contains the original files supplied from the experiment repository:

- `nodes.csv`: 71 package/version nodes, advisory-based local disturbances,
  and source indices.
- `edges.csv`: 128 dependency-to-dependent relations with baseline S and tau.
- `deps_dev_dependencies.json`: the preserved resolved-dependency response.
- `osv_snapshot.json`: the preserved advisory query results and advisory records.
- `manifest.json`: source hashes, mappings, and case metadata.

The original file bytes are unchanged. Both CSV hashes match
`results/paper/paper_outputs_manifest.json`; both JSON source hashes match
the case manifest. `input_verification.json` records additional integrity checks.

From the manuscript root, run `python3 scripts/verify_express_inputs.py`.

The baseline B values are comparative index inputs derived from categorical
advisory severity, not calibrated activation probabilities. The planned
stochastic benchmark will supply its declared controlled initial probabilities
and edge weights separately. These verified inputs do not imply that the
new benchmark experiments have been completed or that incident outcomes
have been independently validated.
