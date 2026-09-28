# Briefing 03: Model Formulation and Equations

## Graph assumption

GBBRPM v1 operates on a directed acyclic graph:

`G = (V, E)`

- `V`: nodes or entities
- `E`: directed relations
- DAG restriction: allows one-pass topological evaluation
- topological order: computational order, not physical time

## Edge contribution

For edge `i -> j`:

`Q_ij = S_ij * tau_ij * R_i`

where:

- `R_i` is the **current accumulated upstream risk**, not merely the original disturbance;
- `S_ij` is relation-specific susceptibility;
- `tau_ij` is optional transmission or influence; and
- `Q_ij` is the incoming contribution reaching node `j`.

## Receiving-node update

`R_j = 1 - (1 - B_j) * product over i in P(j) of (1 - Q_ij)`

where:

- `B_j` is local disturbance at `j`;
- `P(j)` is the predecessor set; and
- `R_j` becomes the current state used for later downstream propagation.

## Source-node behavior

For a source with no predecessors, the product over an empty set equals `1`:

`R_j = 1 - (1 - B_j)(1) = B_j`

Therefore, a source node can have local disturbance. It does not need a special propagation equation.

## Why risk stays bounded

If `B`, `S`, `tau`, and upstream `R` are all in `[0,1]`, then every `Q` lies in `[0,1]`. Every complement term also lies in `[0,1]`. Their product lies in `[0,1]`, so subtracting from one keeps `R_j` in `[0,1]`.

## Why it is monotone

Increasing a valid local disturbance or incoming contribution cannot decrease final risk because the update reduces the remaining complement. However, the size of the increase may diminish near saturation.

## Bounded multi-source aggregation

For two incoming contributions and no local disturbance:

`R = 1 - (1 - Q1)(1 - Q2)`

This is greater than either contribution alone but cannot exceed `1`.

It does not prove the contributions are probabilistically independent. Shared ancestry is diagnosed separately.

## Worked miniature example

Suppose:

- source `N1`: `B1 = 0.60`, so `R1 = 0.60`;
- source `N4`: `B4 = 0.30`, so `R4 = 0.30`;
- `S_12 = 0.50`, giving `Q_12 = 0.30`;
- `S_42 = 0.40`, giving `Q_42 = 0.12`;
- receiving node `N2`: `B2 = 0.10`.

Then:

`R2 = 1 - (1 - 0.10)(1 - 0.30)(1 - 0.12)`

`R2 = 1 - (0.90)(0.70)(0.88) = 0.4456`

If `S_23 = 0.75`, `tau_23 = 1`, and `B3 = 0`:

`Q_23 = 0.75 * 1 * 0.4456 = 0.3342`

`R3 = 0.3342`

This demonstrates current-state recursion: `N3` receives the accumulated `R2`, not only an original source score.

## Susceptibility mapping used in drainage and Component 2

`S_ij = min(1, L_ij / C_ij)`

This mapping is:

- bounded;
- monotone;
- simple to audit; and
- domain-specific rather than universal.

Clipping at one prevents the bounded model input from exceeding its declared range. After an edge reaches `S = 1`, it is saturated, but other edges may still increase when a global load scale changes; therefore, downstream risk can continue to change.

## Neutral transmission baseline

The baseline uses `tau = 1` so unsupported heterogeneous transmission is not invented. Uniform non-neutral sweeps test sensitivity only and are not calibration.

## Ranking and ties

Nodes are ordered by descending final `R`. Equal values retain equal standing. The model does not introduce arbitrary tie-breaking unless an external decision rule is explicitly added.

## Likely examiner questions

### “Why multiply S, tau, and R?”

The product makes each factor a gate on the incoming contribution. If susceptibility or transmission is zero, no contribution passes. If both are one, the full current upstream state passes.

### “Can local disturbance and incoming risk coexist?”

Yes. The local complement `(1 - B_j)` is multiplied with the incoming complements, so the node can contain both inherited and locally introduced risk.

### “Why not add contributions?”

Simple addition can exceed one and requires clipping after aggregation. The multiplicative complement is intrinsically bounded and saturating.

### “Is R time-dependent?”

Not in v1. “Current state” means the state already computed earlier in topological order for the evaluated scenario, not a time-series state.

