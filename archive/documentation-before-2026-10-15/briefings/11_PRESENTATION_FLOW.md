# Briefing 11: Suggested Defense Presentation Flow

This sequence is designed for a roughly 13--16 minute technical presentation. Adjust timing to the panel's instructions.

## Slide 1: Title and one-sentence contribution — 30 seconds

Say:

> This study designs and evaluates GBBRPM, a bounded recursive architecture that combines local disturbance with directed network context to support comparative node-risk prioritization on DAGs.

Avoid beginning with equations.

## Slide 2: Practical motivation — 1 minute

Explain the difference between:

- local monitoring: how disturbed is this component?; and
- network-context prioritization: how should it rank after connectivity and operating conditions are considered?

Use one simple example: two nodes have the same local disturbance but different downstream reach.

## Slide 3: Research problem and gap — 1 minute

State that propagation models already exist. The gap is architectural integration under one bounded comparative-risk semantics—not lack of graphs or diffusion models.

## Slide 4: Model architecture — 1.5 minutes

Introduce:

- `Q_ij = S_ij * tau_ij * R_i`
- `R_j = 1 - (1 - B_j) product(1 - Q_ij)`

Define each symbol in plain language. Emphasize that `R_i` is the current accumulated state and `R` is not a probability.

## Slide 5: Why the rule is bounded — 45 seconds

Explain complement multiplication. Mention source behavior through the empty product and retain ties explicitly.

## Slide 6: Evaluation design — 1 minute

Show the two layers:

- architecture validation; and
- cross-domain evaluation.

Keep the 136 architecture runs separate from the 43 Component 2 runs.

## Slide 7: Controlled networks and scenario families — 1 minute

Show N1--N5 and their purposes. Summarize the five scenario families rather than listing every run.

## Slide 8: Main architecture findings — 1.5 minutes

Highlight:

- all declared bounds and property tests passed;
- equal local severity produced different outlet risks;
- local-only and heterogeneous rankings differed;
- robustness was high at modest perturbation but top-set overlap declined; and
- runtime reached approximately 16.65 ms at 1000 nodes.

## Slide 9: Reconvergence limitation — 1 minute

Show N3 versus N4/N5. Explain independent convergence versus shared-origin reconvergence. State clearly that the path-pruned output is diagnostic, not ground truth.

## Slide 10: Drainage and SWMM boundary — 1 minute

Report:

- maximum-depth Spearman: `-0.416`;
- flooding Spearman: `-0.485`;
- low top-set overlap; and
- substantial outside-scope hydraulic worsening.

Say that GBBRPM is not a hydraulic simulator.

## Slide 11: Software case — 45 seconds

Report 71 packages, 128 edges, seven affected versions, and Express risk increasing from `0.5000` to `0.9975` across the controlled transmission sweep. State the exploit-prediction boundary.

## Slide 12: Electrical case — 1.5 minutes

Split the explanation:

1. full-network preprocessing: 187 buses, 177 active connections, 269 files, and 98.31% coverage;
2. Component 2: 12 observable nodes, 11 edges, measured loading, and 43 controlled runs.

Explain why Component 2 was selected and why this remains controlled sensitivity rather than event validation.

## Slide 13: Research prototype — 1 minute

Show the prototype architecture or a live interface view. Explain validated synthetic/imported inputs, editable model parameters, graph safeguards, and traceable rankings. State that operational mode remains inactive and that the prototype is not production-ready.

## Slide 14: Cross-domain evidence comparison — 1 minute

Use a table:

- drainage: behavioral plus hydraulic boundary;
- software: structural plus sensitivity;
- electrical: preprocessing plus controlled measured-loading sensitivity.

State that these are unequal evidence roles.

## Slide 15: Conclusions — 1 minute

Give only three conclusions:

1. the architecture behaves consistently with its bounded semantics;
2. network context materially changes prioritization; and
3. the frozen rule is instantiable across the tested domains, without proving universal prediction.

## Slide 16: Limitations and next work — 45 seconds

Prioritize:

- shared-origin dependence;
- DAG-only scope;
- lack of independent operational outcomes; and
- need for domain calibration and repeated external studies.

## Backup slides and calculation evidence

Keep these outside the timed main presentation unless the panel asks:

- **Appendix A:** generic bounded-recursion example, including source behavior, convergence, ranking, and ties;
- **Appendix B:** Express software calculation yielding `R = 0.9118` at `tau = 0.50`;
- **Appendix C:** Component 2 susceptibility derivation and 12-node trace yielding risk sum `1.186`; and
- **Component 2 adviser briefing:** selection rationale, exclusions, parameter policies, and the separate 43-run design.

Do not present an operational drainage calculation until defensible real inputs are available.

## Final sentence

> GBBRPM is best understood as a lightweight, traceable comparative-prioritization architecture whose mechanisms are computationally supported, while predictive validity remains a separate domain-specific requirement.

## Presentation habits

- Say “comparative risk index,” not “probability.”
- Say “supports,” not “proves,” unless referring to the analytical boundedness argument.
- Say “controlled sensitivity,” not “event validation,” for Component 2.
- Do not combine unlike evidence into one accuracy score.
- When challenged, return to the exact question each experiment was designed to answer.
