# Input provenance update — 14 October 2026

## Verified original Express inputs

The supplied `express_4.18.2.zip` contains the original software inputs.
The files were included without changing their bytes under
`data/software/express_4.18.2/` in this manuscript package.

| File | Historical SHA-256 | Result |
|---|---|---|
| `nodes.csv` | `854ddc4f2a4b803d983cb713145524589fdf6425d91e70867d90bd8aa182f31b` | Exact match; 71 nodes |
| `edges.csv` | `11dfe4c2b82b30e836eda0bb31b8690edceb316134ee16fa8a6ffe22cd7cfab0` | Exact match; 128 edges |

The dependency JSON and OSV snapshot also match the hashes in the supplied
case manifest. Package/version identities, edge endpoints, reversal from
deps.dev dependency direction, and all seven advisory-origin identities
agree with the preserved source records. Topological sorting confirms a DAG.

Reproduce these checks from the manuscript root:

```bash
python3 scripts/verify_express_inputs.py
```

The recorded check output is `data/software/express_4.18.2/input_verification.json`.
The historical paper-output manifest and five original case files were preserved.

## Manuscript corrections

- Chapter 2 describes the scientific criteria for the model-family comparison
  without referring to consultation history.
- Section 3.6.4 uses the verified original Express topology for the planned
  12 benchmark scenarios. Recovery/reacquisition is no longer an outstanding task.
- Section 3.11.2 records verified Express input availability and keeps N1–N5
  reconstruction provenance separate.
- The timeline description makes W8 a review of mappings, input selection,
  and scenario eligibility. The existing chart's generic data/mapping row
  remains appropriate; the calendar is still provisional.
- Appendix D, README, and supporting method/protocol notes use consistent status.
- The manuscript no longer describes the earlier N1–N5 synthetic fixtures as
  a “lost original raw dataset.” It still identifies their reconstructed inputs
  and does not claim identity with unavailable earlier fixture files.

## Study status

Input verification is completed. The proposed stochastic benchmark remains
planned. The software case remains a real-topology mechanism experiment;
OSV supplies input evidence rather than independent incident outcomes.
Historical exploratory results and numerical values were not changed.
Express input recovery does not establish recovery of the earlier N1–N5 inputs.
