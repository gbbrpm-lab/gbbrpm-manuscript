# Review resolution

This pass uses the unchanged uploaded manuscript and applies supported
clarifications from the supplied Review.pdf. It does not change the
model, scenario inputs, or computed risk results.

| Review point | Decision and evidence |
| --- | --- |
| Figure 4.1 x-axis | No change. Visual inspection confirms N1, N2, N3, N4, N5. |
| Appendix C apparent-power arithmetic | Correct the displayed averaging formula, retain 1153.8297 kVA. The previously supplied Component 2 meter summary reports source mean apparent power 1153.8296825976352 kVA across 24 snapshots; snapshot data reproduce the average of per-snapshot magnitudes. The magnitude of the mean P/Q pair is about 1153.8285 kVA. |
| Top-three versus top-20% robustness | Retain both distinct conventions and add the top-20% column to the robustness table (label tab:robustness). Values: 0.776000, 0.604873, 0.440823. The supplied N5_robustness_summary.csv has SHA-256 0dfb11934c7a6d2fa45c18776f1236fd284811b9118425d5c0e034d228bdca7e, matching the manuscript output manifest. Nominal top-20% size is four. |
| SWMM interpretation | Clarify that mismatch does not isolate physical causes or validate inspection/maintenance utility. Retain the reported comparison results. |
| Software reconvergence | Explicitly discuss shared qs and send paths in Chapter IV, Chapter V, and Appendix B. Root-state inflation is possible but its magnitude is not quantified by this case. Ranking stability does not prove unbiased risk magnitudes. |
| Susceptibility versus transmission | Preserve conceptual roles, explain that the update depends on their product and does not identify the factors separately from risk outputs. |
| Saturation | Distinguish clipping of susceptibility from saturation of receiving-node risk. |
| RRL citations | No changes; retain the user's guideline-compliant citation convention. |
| Front matter | Deferred as instructed. |

Evidence from earlier experiment archives was checked locally. Private
Component 2 measurement files are not added to this manuscript package.
