# Briefing 08A: Research Prototype

## Why the prototype exists

The prototype demonstrates that the frozen GBBRPM workflow can be used through an inspectable interface without rewriting the propagation rule. It is a research implementation artifact, not a claim of production deployment.

## Architecture

1. **React/Vite frontend:** dataset selection, graph visualization, parameter editing, execution, and ranking display.
2. **FastAPI service:** dataset retrieval, schema validation, and evaluation requests.
3. **Pinned `gbbrpm` v0.1.0 engine:** the same versioned evaluator used by the computational workflow.
4. **Cytoscape graph view:** directed topology, risk coloring, and component selection.
5. **Evaluation response contract:** topological order computed by the evaluation service, plus an ordered trace (`source`, `transfer`, `aggregate`) assembled from engine-computed values.

## Data modes

- **Synthetic:** frozen N1--N5 fixtures.
- **Imported:** user-supplied JSON following the common node-and-edge schema.
- **Operational:** inactive placeholder until a provenance-complete agency dataset and adapter exist.

The inactive operational mode is deliberate. It prevents synthetic or imported fixtures from being described as operational evidence.

## Inputs and safeguards

Nodes require:

- unique identifier;
- local disturbance `B` in `[0,1]`; and
- optional outlet and display metadata.

Edges require:

- declared source and target nodes;
- `tau` in `[0,1]`; and
- either explicit `S`, or both `L` and `C`.

Validation rejects duplicate nodes or edges, unknown endpoints, partial `L/C` input, invalid bounds, and cycles.

## Interface functions

- select N1--N5 or import a JSON network;
- edit node disturbance `B`;
- edit edge load `L`, capacity `C`, transmission `tau`, or explicit susceptibility `S`;
- execute the model explicitly;
- inspect a risk-colored directed graph;
- view ranked node risks and outlet summaries;
- retain edge-contribution terms for traceability; and
- optionally replay the stored evaluation trace to inspect intermediate states.

## Evaluation trace and trace presentation

The evaluation response carries the topological order computed by the evaluation service and an ordered trace. Each step records its type (source, transfer, or aggregate), the receiving node, that node's `B` and computed state, and, for a transfer, the corresponding edge contribution. Steps are assembled from values the engine has already computed; the service does not re-evaluate the propagation rule to build them, so the trace is a record of one evaluation rather than a second evaluation.

Trace presentation is optional and disabled by default:

- a node becomes active when its first predecessor settles and begins transmitting, and its displayed state converges and is revealed only after every incoming contribution has landed, so independent branches proceed concurrently on a single clock;
- each contribution begins traversing its edge only after its source has settled, and the schedule is derived from the service's topological evaluation order;
- the displayed contribution and aggregation terms converge on the values returned by the engine;
- the ranking list is withheld until the replay completes or is skipped, and is released if playback is terminated by a parameter edit, a dataset change, or disabling presentation (comparison and export views are unaffected);
- replay issues no additional evaluation request, and modifying a parameter or changing the dataset discards it;
- a reduced-motion environment initializes in a paused state with continuous motion suppressed while the same schedule and values remain available; and
- presentation timing is display order only, never physical propagation speed.

## Functional verification

| Verification | Result |
|---|---|
| N1--N5 inventory and N5 node count | Passed |
| N5 outlet `R_N20 = 0.7086404493`; top node `N13` | Passed |
| Imported `A -> B -> C` case returns `R_C = 0.28` | Passed |
| Unknown endpoints and directed cycles rejected | Passed |
| Trace covers every node and edge once; step values equal reported results (N1--N5) | Passed |
| Replay schedule settlement causality, ordered event boundaries, input non-mutation | Passed |
| Displayed contribution and node-risk values equal engine values once the corresponding contributions have arrived (controlled trace) | Passed |
| Frontend production compilation | Passed with bundle-size warning |
| Graph motion, selection correspondence, responsive layout | Not yet verified; manual browser inspection required |

## What the prototype establishes

- implementation feasibility;
- reuse of the versioned model engine;
- common-schema validation;
- interactive parameter and graph inspection;
- agreement between displayed and reported quantities once settled; and
- traceable comparative outputs.

## What it does not establish

- user acceptance or usability;
- accessibility compliance;
- production security or reliability;
- multi-user behavior;
- operational data integration; or
- predictive validity in any domain.

## Likely examiner questions

### “Did you rewrite the model in the frontend?”

No. The frontend sends the validated dataset to the service, which invokes the pinned `gbbrpm` v0.1.0 evaluator. This avoids a second implementation of the equation in the interface. The trace shown during replay is assembled from values that evaluator already computed, so it is a record of one evaluation rather than a second implementation. The live readout interpolates between those stored values for display and converges on them; it issues no request and computes no new result.

### “Does the replay animation represent physical propagation?”

No. The schedule is derived from the service's topological evaluation order: every contribution begins only after its source has settled, and a node's state is revealed only after all of its incoming contributions have landed. Independent branches run concurrently, so display order is not a strict sequence. The schedule exists to expose intermediate calculation states. Timing, playback rate, and display mode are presentational and cannot change any computed value; a topological order is a dependency order, not a timeline.

### “Why is operational mode disabled?”

No provenance-complete agency drainage dataset is currently mapped to the common schema. Keeping the mode inactive prevents a demonstration fixture from being mistaken for operational evidence.

### “Does passing functional tests mean the system is ready for deployment?”

No. The checks establish core functional consistency only. Deployment would require user testing, authentication, persistence, security hardening, monitoring, and independently validated operational inputs.

### “What is the strongest prototype claim?”

The frozen model can be exposed through a validated, interactive, and traceable research workflow while preserving its declared evidence boundaries.
