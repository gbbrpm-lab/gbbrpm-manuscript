# Adviser Briefing: Caltech Component 2

## One-minute explanation

Component 2 was selected as a purposive, fit-for-purpose electrical case because it provided the combination needed to instantiate GBBRPM without inventing unsupported inputs: an authorized topology, synchronized phasors at a traceable component source and five terminal loads, a nontrivial branching network, and an observable directed subgraph compatible with the model's DAG assumption. The choice was made from feasibility and evidence-quality criteria, not because Component 2 produced favorable risk results. After excluding one edge without a supported downstream meter path, the observable model contained 12 nodes and 11 edges. It is therefore evidence that the frozen GBBRPM mechanism can be instantiated and tested on real topology and measured loading, but it is not claimed to represent the entire SoCal 28-Bus system or to validate event prediction.

## Why Component 2 specifically?

Component 2 met six practical selection criteria:

1. **Authorized and traceable inputs.** Its topology and phasor measurements were available through the authorized Caltech dataset workflow.
2. **Observable source boundary.** `egauge_21` supplied a defensible component-source measurement.
3. **Multiple observable terminal loads.** `egauge_3`, `egauge_7`, `egauge_9`, `egauge_11`, and `egauge_13` supported downstream loading calculations across several branches.
4. **Useful structural complexity.** The component contains depth, branching, internal nodes, and multiple terminal nodes, allowing severity, location, loading, and multi-source experiments without becoming opaque.
5. **Compatibility with GBBRPM v1.** The observable network is an arborescence and therefore a DAG, so it can be evaluated without changing the frozen one-pass update rule.
6. **Auditable exclusions and reconciliation.** Unsupported elements and meters could be identified explicitly rather than silently estimated.

This is **purposive case selection**, not random sampling and not a claim that Component 2 is the “best” or most representative Caltech component. The defensible claim is that it met the declared requirements of this mechanism-and-sensitivity study.

## Why 13 complete nodes but only 12 model nodes?

The complete component contains 13 nodes and 12 directed elements. `line_407` did not have a supported downstream meter path for the selected extract. Including it would require either inventing a load or assigning zero loading. Zero would incorrectly mean “observed no load,” whereas the actual status was “not sufficiently observed.” The study therefore excluded that element and its unsupported branch, producing a 12-node, 11-edge observable model.

This improves evidentiary honesty at the cost of reduced topology coverage. The excluded edge is reported as a limitation rather than hidden.

## Why these meters?

| Meter | Role | Decision |
|---|---|---|
| `egauge_21` | Component source | Included as the source-boundary meter |
| `egauge_3`, `7`, `9`, `11`, `13` | Terminal loads | Included for downstream real and reactive power aggregation |
| `egauge_19` | Neighboring feeder | Excluded because it does not represent Component 2 load |
| `egauge_15` | Redundant or auxiliary measurement | Excluded because complete usable phasors were unavailable |

## Why use 24 phasor snapshots?

The 24 aligned snapshots provide a short, internally synchronized normal-operation window for constructing a deterministic descriptive baseline. Their purpose is to estimate mean loading for this controlled instantiation—not to characterize seasonal behavior, train a forecasting model, or establish statistical generalizability.

If challenged on sample size: **24 is adequate for the stated descriptive mechanism test, but insufficient for temporal or event-response validation.** The manuscript states that limitation explicitly.

## Why use mean phasor-derived power?

Mean phasor-derived real and reactive power provides one traceable operating point while reducing snapshot-to-snapshot noise. Phasors were used as the model input because the declared unit of the `Mains_Power` register was inconsistent with its numerical scale. That register was retained only as a reasonableness cross-check.

The model is static and comparative, so this mean operating point is consistent with the one-pass formulation. A time-varying extension would require a separate temporal model and experiment.

## Why was the residual not allocated?

The mean source real power was 985.957 kW, while the five metered terminal loads summed to 976.828 kW. The real-power residual was therefore 9.129 kW, or approximately 0.926% of source real power. The reactive residual was 135.398 kvar.

The residual was reported separately because no evidence justified assigning it to a particular internal node or branch. Allocating it proportionally or placing it at one node would introduce an unverified modeling assumption. This policy preserves traceability, although it means the case is not a complete power-flow reconstruction.

## Why define susceptibility as S = min(1, L/C)?

The mapping is bounded, monotone, parameter-light, and consistent with the generic role of susceptibility in GBBRPM:

- higher loading relative to capacity cannot reduce susceptibility;
- values remain within `[0,1]`;
- clipping prevents overload ratios from violating the model's bounded inputs; and
- the calculation is interpretable from documented measurements and ratings.

It is a normalized loading-to-capacity susceptibility, **not a probability of electrical failure**.

Transformer capacity used the minimum declared nameplate kVA when multiple values were present, providing a deterministic conservative rule. Line capacity used three times phase-to-ground nominal voltage times the declared current rating.

## Why initialize B = 0?

The selected phasors describe normal operation and do not provide verified event or fault labels. Assigning nonzero observed disturbance would therefore be unsupported. The reference model initializes every node at `B = 0`, producing the expected all-zero risk state. Controlled experiments then inject declared disturbances so mechanism response can be tested without mislabeling normal measurements as faults.

## Why initialize tau = 1, then sweep it?

`tau = 1` is the neutral baseline: it avoids inventing heterogeneous transmission coefficients. The uniform sweep over `0, 0.25, 0.50, 0.75, 1.00` is explicitly a sensitivity experiment showing how attenuation affects propagation. It is not calibration and does not claim that any swept value is the true electrical transmission coefficient.

## Why exactly 43 scenarios?

| Scenario family | Runs | Purpose |
|---|---:|---|
| Zero-disturbance reference | 1 | Verify the mathematical zero baseline |
| Root severity | 4 | Test monotonic response to `B = 0.25, 0.50, 0.75, 1.00` |
| Disturbance location | 12 | Inject the same severity at every observable node |
| Measured-load scaling | 5 | Test susceptibility response at `0.50x` through `1.50x` loading |
| Uniform transmission | 5 | Test controlled attenuation from `tau = 0` through `1` |
| Internal-source pairs | 15 | Test every pair among six non-root internal nodes: C(6,2) = 15 |
| All internal sources | 1 | Test simultaneous disturbance at all six internal nodes |
| **Total** | **43** | Separate Component 2 protocol |

The count is separate from the 136-run generic architecture protocol because the two suites answer different questions.

## Why use internal nodes for multi-source cases?

Terminal-node disturbances have no downstream edges and would often produce only their local risk, making many multi-source combinations structurally trivial. Six non-root internal nodes were used so pairwise cases exercise local-plus-incoming bounded aggregation or concurrent branch coverage.

Component 2 is an arborescence, so these scenarios do **not** test downstream reconvergence. Reconvergence and shared-origin double counting are evaluated separately in the N4 and N5 architecture cases.

## What does Component 2 establish?

It supports the following claims:

- the frozen GBBRPM rule can be instantiated on an observable real electrical topology;
- measured phasor loading and documented capacity can produce traceable heterogeneous susceptibility;
- node and edge outputs remain bounded;
- severity, load scale, transmission, and location produce coherent controlled sensitivity responses; and
- equal local disturbances can create different network-level risk because of topology and edge conditions.

## What does it not establish?

It does not establish:

- calibrated failure probabilities;
- prediction of switching events, outages, or equipment failure;
- temporal forecasting;
- complete power-flow reconstruction;
- statistical representativeness of the full SoCal 28-Bus dataset;
- behavior on cyclic or bidirectional electrical models; or
- reconvergent multi-path dependence behavior.

## Likely examiner questions and concise answers

### “Did you choose Component 2 because it produced good results?”

No. It was selected using pre-result feasibility criteria: topology availability, synchronized source and terminal measurements, observable downstream loading, useful branching structure, traceable exclusions, and DAG compatibility. The resulting rankings were not a selection criterion.

### “Is this cherry-picking?”

It is purposive case selection, which limits generalizability but is appropriate for a mechanism-instantiation study. The thesis does not claim random sampling or grid-wide representativeness. Repeating the protocol on additional components is identified as future work.

### “Why not force the missing branch into the model?”

Doing so would require an invented load or an unjustified zero. Excluding and reporting the unsupported branch preserves evidence traceability.

### “Is 24 snapshots really enough?”

Enough for a short descriptive operating-point instantiation and deterministic sensitivity study; not enough for temporal, seasonal, or event-response claims. Those stronger claims are explicitly withheld.

### “Why call this real-data evaluation if the disturbances are injected?”

The topology, loading, and capacity basis are real or documented; the disturbances are controlled. The correct description is a controlled real-topology, measured-loading mechanism and sensitivity study—not observed event validation.

### “Why did you not distribute the residual?”

No measurement identified where it belonged. Reporting it separately avoids adding an unsupported spatial allocation assumption.

### “Does the tau sweep validate electrical transmission?”

No. It validates the model's controlled attenuation response. Empirical transmission calibration would require independent electrical evidence.

### “Can you generalize the results to the full Caltech grid?”

No statistical generalization is claimed. Component 2 demonstrates coherent instantiation within one observable case. Wider generalization requires repetition across additional components, operating periods, and event-aligned outcomes.

## Safest final defense statement

> Component 2 provides controlled mechanism and sensitivity evidence on real topology and measured normal-operation loading. It strengthens the cross-domain instantiation claim, but it does not convert GBBRPM into an electrical-event predictor.
