# Briefing 08A: Research Prototype

## Why the prototype exists

The prototype demonstrates that the frozen GBBRPM workflow can be used through an inspectable interface without rewriting the propagation rule. It is a research implementation artifact, not a claim of production deployment.

## Architecture

1. **React/Vite frontend:** dataset selection, graph visualization, parameter editing, execution, and ranking display.
2. **FastAPI service:** dataset retrieval, schema validation, and evaluation requests.
3. **Pinned `gbbrpm` v0.1.0 engine:** the same versioned evaluator used by the computational workflow.
4. **Cytoscape graph view:** directed topology, risk coloring, and component selection.

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
- edit edge load `L`, capacity `C`, and transmission `tau`;
- execute the model explicitly;
- inspect a risk-colored directed graph;
- view ranked node risks and outlet summaries; and
- retain edge-contribution terms for traceability.

## Functional verification

| Verification | Result |
|---|---|
| N1--N5 inventory and N5 node count | Passed |
| N5 outlet `R_N20 = 0.7086404493`; top node `N13` | Passed |
| Imported `A -> B -> C` case returns `R_C = 0.28` | Passed |
| Unknown endpoints and directed cycles rejected | Passed |
| Frontend production compilation | Passed with bundle-size warning |

## What the prototype establishes

- implementation feasibility;
- reuse of the versioned model engine;
- common-schema validation;
- interactive parameter and graph inspection; and
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

No. The frontend sends the validated dataset to the service, which invokes the pinned `gbbrpm` v0.1.0 evaluator. This avoids a second implementation of the equation in the interface.

### “Why is operational mode disabled?”

No provenance-complete agency drainage dataset is currently mapped to the common schema. Keeping the mode inactive prevents a demonstration fixture from being mistaken for operational evidence.

### “Does passing functional tests mean the system is ready for deployment?”

No. The checks establish core functional consistency only. Deployment would require user testing, authentication, persistence, security hardening, monitoring, and independently validated operational inputs.

### “What is the strongest prototype claim?”

The frozen model can be exposed through a validated, interactive, and traceable research workflow while preserving its declared evidence boundaries.
