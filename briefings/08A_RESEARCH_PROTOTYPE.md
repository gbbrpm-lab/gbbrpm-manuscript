# Briefing 08A: Evaluation Engine and Supporting Prototype

**Status: existing preliminary implementation and team reports; planned verification is not a completed test report.**

GBBRPM is the model. Its versioned evaluation engine validates inputs and performs the deterministic DAG calculation. The React/Vite interface, FastAPI service, and graph visualization support inspection of that calculation. Additional presentation work is secondary to the mechanism evaluation.

## Planned input contract

Require unique node identifiers, valid edge endpoints, finite bounded B/S/tau, and a valid DAG. Reject self-loops, duplicate edges, cycles, and non-finite values. An explicit zero is different from missing data. Require direct S or a complete compatible L/C pair, with C>0 and L>=0; reject supplying both representations for one edge. Clip only through a declared adapter, not to hide malformed input.

Synthetic and user-imported inputs use the same contract. Operational mode remains inactive until provenance-complete data are available. Record the engine/package and application revisions used; do not assume an old pinned version implements the new benchmark methods.

## Trace and replay

Return engine-computed B, Q, R, and topological order, with one source-or-aggregate settlement record per node and one transfer record per edge. A receiver may appear in multiple transfer records.

Replay presents stored results without another propagation evaluation. Trace assembly, scheduling, storage, and rendering still have costs. Independent branches may display concurrently; a receiver settles after required incoming contributions. Interpolated readouts are presentation values; settled quantities must agree with the engine. Display timing is not physical propagation speed and must not alter inputs, final states, or ranks.

## Evidence status

Appendix D preserves prior fixture/import/build checks as preliminary feasibility evidence. Prototype revision `eafec4d` and related replay checks are team-reported; matching application source/logs were not independently reproduced in this manuscript package. Manual browser inspection remains reported as pending.

Earlier supporting records report positive infinity in loading/capacity reaching HTTP 500. The active Chapter 3 contract requires controlled rejection of non-finite inputs; do not claim the defect is fixed without matching-source reproduction and regression evidence. Appendix E supplies the current verification plan, not a new application test report.

## Verification still required

Compare N1–N5 states against the versioned engine at declared tolerance; verify trace coverage, receiving-state reconstruction, valid imports and controlled invalid-input rejection; exercise NaN and both infinity signs; check predecessor settlement, concurrent branches, input non-mutation, cancellation/reduced-motion behavior, and display-mode invariance. Retain source revisions, fixtures, expected values, and logs. Complete browser checks and production build on the tested revision.

Functional consistency does not establish usability, operational utility, production security, or deployment readiness. Animation is not scientific propagation evidence.

Sources: Chapter 3 engine/verification sections; Appendices D–E; historical member integration record.
