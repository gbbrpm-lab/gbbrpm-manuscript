# Briefing 08: Electrical Instantiation

**Role: preliminary real-topology, measured-loading case plus planned reviewed evaluation; not electrical-event prediction.**

## Evidence layers

| Layer | Existing record | Boundary |
|---|---|---|
| Full-network import | 187 bus records and 177 active connections | Import counts do not prove physical acyclicity or fault accuracy |
| Complete Component 2 | 13 nodes and 12 elements | Observability limits coverage |
| Observable Component 2 | 12 nodes, 11 edges; arborescence | Supports branching, not downstream reconvergence |
| Loading baseline | 24 synchronized normal-operation phasor snapshots | Disturbances are injected, not observed faults |
| Controlled suite | Historical 43-scenario exploratory configuration | Reviewed reruns are planned; not the new stochastic benchmark |
| Independent event outcomes | Not supplied in aligned form | Switching/outage/event prediction remains unvalidated |

Component 2 is purposively selected for authorized topology, source/terminal observability, traceable mapping, useful branching, and DAG compatibility. It is not a representative random sample of electrical networks.

## Parameter construction

Aggregate downstream real/reactive powers **within each aligned snapshot**, then compute apparent magnitude and average it:

`L_ij = mean_t(sqrt(P_ij,t^2 + Q_ij,t^2))`.

Do not substitute the magnitude of mean P and Q. Use the documented transformer nameplate rule and three-phase line capacity `3*V_phase*I_rated/1000` kVA. Then `S=min(1,L/C)`. This is a bounded loading index, not a physical failure probability.

The unsupported `line_407` branch is excluded rather than assigned an invented load or zero. Source/terminal meter mappings, neighboring-feeder exclusion, unusable measurements, and unallocated residuals must remain explicit. Restricted raw measurements and credentials are not packaged here.

## Historical protocol proposed for reviewed reruns

One zero-disturbance baseline, four root severities, 12 disturbance locations, five load scales, five transmission levels, 15 internal-node pairs, and one all-internal case total 43. These scenarios remain separate from the historical 136-run N1–N5 configuration and the prospective reference inventory.

The baseline B=0 avoids inventing observed disturbances from normal-operation records. Controlled B injections and uniform tau changes test mechanism response. The historical root-severity trace at B=0.75 gives risk sum approximately 1.186; Appendix C explains it. A risk sum is not a failure probability or conserved power.

## Next evidence needs

Review adapter completeness and authorized source availability, rerun the frozen controlled configuration, and seek independent outcomes aligned with event windows. If those outcomes are unavailable, report the restriction. A domain case becomes primary operational validation only after its independent target, mapping, coverage, and evaluation separation are defensible; no domain is selected automatically.

For detailed meter and residual policies, see [the Component 2 adviser briefing](../ADVISER_BRIEFING_COMPONENT2.md).

Sources: Chapter 3 electrical/domain sections; Appendices C–D.
