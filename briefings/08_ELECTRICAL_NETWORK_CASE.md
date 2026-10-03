# Briefing 08: Electrical-Network Case

## Two-stage purpose

The electrical case has two distinct stages:

1. **Full-network import and baseline quality** — verifies topology construction, channel mapping, missingness handling, and coverage reporting.
2. **Component 2 controlled instantiation** — tests GBBRPM mechanisms on real topology and measured loading.

These stages should not be described as event-response validation.

## Full-network baseline evidence

- 187 bus records;
- 177 active directed connections;
- 10 weak components;
- 269 channel files;
- 231 populated and 38 empty files;
- 222 mapped files;
- 54 usable voltage channels;
- 98.31% overall timestamp coverage; and
- mean-voltage range of 0.9762 to 1.0431 p.u.

Empty files were recorded as data-quality outcomes rather than causing parser failure.

The available baseline covers November 14--15, 2024, while the requested switching groups occurred on November 13. Event-aligned inputs and independent outcomes were not available in the analyzed extract.

## Why Component 2?

Component 2 was selected purposively because it supplied:

- authorized and traceable topology;
- synchronized source and terminal-load phasors;
- useful branching structure;
- explicit meter roles and exclusions;
- an observable directed subgraph; and
- compatibility with the v1 DAG evaluator.

Selection was based on feasibility and evidence quality, not favorable results. It is not claimed to represent the full Caltech system statistically.

## Observable model

- complete topology: 13 nodes and 12 edges;
- observable model: 12 nodes and 11 edges;
- excluded element: `line_407` due to no supported downstream meter path;
- source meter: `egauge_21`;
- terminal meters: `egauge_3`, `7`, `9`, `11`, and `13`;
- excluded neighboring feeder: `egauge_19`;
- unavailable incomplete meter: `egauge_15`; and
- aligned snapshots: 24.

## Power reconciliation

- source mean real power: 985.957 kW;
- metered terminal-load real power: 976.828 kW;
- real residual: 9.129 kW or 0.926%;
- reactive residual: 135.398 kvar.

Residuals were reported separately because spatial allocation would require an unsupported assumption.

## Parameterization

- loading `L`: mean downstream apparent power from phasors;
- transformer capacity: minimum declared nameplate kVA when multiple values exist;
- line capacity: three times phase-to-ground nominal voltage times declared current rating;
- susceptibility: `S = min(1, L/C)`;
- reference disturbance: `B = 0`; and
- reference transmission: `tau = 1`.

`Mains_Power` was used only as a scale cross-check because its declared unit conflicted with its numerical scale. Phasor-derived power remained the input.

## The 43-run suite

| Family | Runs |
|---|---:|
| Zero reference | 1 |
| Root severity | 4 |
| Location | 12 |
| Measured-load scale | 5 |
| Uniform transmission | 5 |
| Internal-source pairs | 15 |
| All internal sources | 1 |
| **Total** | **43** |

## Key results

- all node risks and edge contributions remained in `[0,1]`;
- zero-disturbance reference produced zero risk;
- root severity from `0.25` to `1.00` increased risk sum from `0.395` to `1.581`;
- load scaling from `0.50x` to `1.50x` increased risk sum from `0.908` to `1.638`;
- at equal `B = 0.75`, `C2_N02` produced the highest location risk sum, `1.417`;
- `tau = 0` retained only root local risk, while `tau = 1` produced risk sum `1.186`;
- nested pair `C2_N02 + C2_N03` produced maximum node risk `0.599` and risk sum `1.582`; and
- all six internal sources affected 10 of 12 nodes with risk sum `3.754`.

**Worked-calculation reference:** Appendix C derives baseline electrical susceptibility from measured apparent loading and declared capacity, then traces the full 12-node root-disturbance scenario that reproduces risk sum `1.186`.

## Structural interpretation

`C2_N02` can produce greater network-wide risk than the root at equal disturbance because it bypasses attenuation through the initial transformer while retaining access to nearly every downstream branch.

Terminal disturbances often remain local because terminal nodes have no downstream edges.

Component 2 is an arborescence, so multi-source experiments test local-plus-incoming aggregation and concurrent branch coverage—not downstream reconvergence.

## Strongest defensible claim

> The electrical case verifies real-data preprocessing and demonstrates controlled bounded sensitivity on one observable real topology parameterized by measured normal-operation loading.

## Claim boundary

It does not establish failure probability, switching-event prediction, temporal forecasting, complete power-flow reconstruction, or system-wide generalizability.

For the detailed rationale and examiner answers, read [ADVISER_BRIEFING_COMPONENT2.md](../ADVISER_BRIEFING_COMPONENT2.md).
