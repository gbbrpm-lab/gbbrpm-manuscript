# Current Compute, Prior-Art, Heterogeneity, and Prototype Follow-up

Synchronized 15 October 2026 to Chapter 3. These are planned protocols, not executed benchmark or regression results. The earlier review record is preserved in `../archive/documentation-before-2026-10-15/docs/REVIEW_PROTOCOL_FOLLOWUP.md`.

## Computational pilot

The 3,600 generated scenarios at N=100,000 imply 75.6 billion potential edge-trial checks under literal execution; 48 extra million-trial audits add 10.08 billion and the heterogeneous subset adds 3.024 billion. This is workload arithmetic, not a runtime forecast.

Use development seed 41 at sizes 20/100/250 in every family, both local settings, weights 0.10/0.75 and the heterogeneous assignment, with staged 1,000/10,000 trials and at least one size-250 N=100,000 case if memory permits. Record generation, sampling, deterministic methods including the published lower comparator, target-tree work, storage, throughput, memory, hardware, and revisions. Try batching or validated equivalent implementation first; freeze any reduced allocation/count/precision before held-out outcomes.

## Published bounds

Chapter 2's `cascade_prior_art.tex` acknowledges both nodewise and aggregate roles of Abbe et al. (2017/2020). The planned matched published comparator is the 2020 DAG lower recurrence after adding one always-active auxiliary source with independent B-weight edges. It may delete original DAG edges and has no assumed ordering relative to M or T. Validate against exact fixtures and time its preparation and evaluation. The length-indexed upper construction is compared at equation level but is not a mandatory full-grid implementation. Independent local starts alone are not a novelty distinction.

This is a summary of the manuscript's cited comparisons, not a new independent source verification.

## Secondary heterogeneity

Use the existing family/size graphs for development seed 41 and evaluation seeds 1001–1005, with both initial settings. The fixed hash ordering assigns a quarter w=0.10, a half 0.20, and a quarter 0.30, paired to existing uniform-0.20 cases. There are 144 additional scenarios: 24 development and 120 evaluation. Copy the exact hash construction from `reference_benchmark.tex`. Report separately; five evaluation graphs per family/size limit inference. This tests effective-weight heterogeneity and does not identify S/tau separately or calibrate domain probabilities.

## Prototype evidence

The active contract requires finite-number validation and controlled invalid-input responses. Earlier team records report positive infinity in L/C reaching HTTP 500. Reproduce/correct that issue in matching application source and retain NaN and both infinity regressions; do not claim a fix from manuscript edits. Complete recorded browser and numerical/trace checks. Replay polish remains secondary.

See [current status](CURRENT_PROPOSAL_STATUS.md), [benchmark summary](BOUND_AND_PROTOCOL_REVISION.md), and [next work](NEXT_STEPS.md).
