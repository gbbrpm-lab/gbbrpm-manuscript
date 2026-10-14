# Full-paper consistency and layout pass

Reviewed on 13 October 2026.

## Result

The revised proposal compiles to 83 pages without final-pass warnings,
undefined references/citations, or overfull boxes. It contains Chapters I–III,
references, and Appendices A–E. The contents is now three pages instead of six;
the preliminary pages occupy 12 pages instead of 17. The editable source and
compiled main.pdf are included.

The review used the current build-repaired proposal, the two supplied NeuralCTM
PDFs as layout examples, and the member-reported prototype revision record.
The samples are examples, not an independently verified institutional rubric.

## Preliminary pages

The compact layout removes a full blank line between contents entries,
retains single spacing, and uses a small gap between major groups. The page
column was narrowed to reduce unnecessary wrapping. All heading levels remain:
chapter, numbered section, numbered subsection, and appendix topics. No body
section was removed to shorten the contents.

The table and equation lists also use compact spacing. All 47 tagged equations
retain their descriptions. Their PDF links now point to the actual equation
tags rather than inheriting a preceding section anchor; each destination was
checked against its listed page.

The supplied examples contain the same preliminary components already present
here: title, approval, acknowledgement, contents, tables, figures, equations,
acronyms, and abstract. The approval page now has an editable draft structure
for the adviser, panel chair/members, dean, and defense date. It expressly
states that approval, examination outcome, and acceptance are pending. A sample
page's “approved” or “PASSED” wording was not asserted for this proposal.

The acknowledgement still needs author-written text. The proposal abstract is
retained as a draft describing planned work without inventing final findings.
Names, credentials, required approval wording/form, and final submission date
remain for author/institution confirmation. The optional official-PDF insertion
route is preserved, together with the previous missing-package repair.

## Prototype scope

Chapter III now gives approximately 189 words for prototype integration and
visualization (previously 377) and 140 words for functional verification
(previously 294), excluding the diagram and using a simple word-count
convention. Its emphasis is the prototype's role in inspecting the model.

Appendix E holds the supporting trace contract, replay behavior, verification
checklist, and outstanding evidence. This is explicitly a future design and
verification plan. Appendix D remains the record of selected preliminary
evidence, keeping completed exploratory work separate from planned evaluation.

The shortened main text retains the earlier decisions:
- The model and its evaluation engine are distinct from the interface.
- Replay presents stored engine results; it does not issue another propagation
  evaluation. Trace preparation, scheduling, and rendering still cost resources.
- Independent branches may display concurrently. Receiving states settle only
  after their incoming contributions arrive.
- Interpolated readouts are presentation values; settled readouts are checked
  against returned quantities.
- Display mode and speed do not change numerical results and do not represent
  physical-time propagation.
- The prototype supports traceability; its UI features are not presented as the
  principal scientific contribution.

The manuscript does not claim a prototype code fix or newly passed application
tests. Revision eafec4d and its checks are team-reported; matching application
source/test logs were not in the manuscript package. Positive-infinity handling
in L/C and manual browser inspection remain open.

## Timeline and visual style

The chart now uses the manuscript's navy/gray colors, thin borders, and body
typeface. Activity labels and graphical distinctions remain readable in the
single-column PDF; conditional work also uses a dashed outline rather than
depending on color alone.

The schedule distinguishes:
1. Prior preliminary work, shown schematically rather than assigned invented
   original completion dates.
2. Current proposal revision, continuing literature review, and data follow-up.
3. Proposal presentation and adviser-driven scope revisions.
4. Final model/engine specification, reference validation, comparator development,
   computational feasibility pilot, and protocol freezing.
5. Held-out mechanism/dependence comparisons, cost measurements, and separate
   domain analyses.
6. Supporting prototype checks, final writing, adviser review, defense revisions,
   submission, and conditional dissemination.

The W8 data checkpoint and protocol-freeze point are explicitly marked.
If W1 begins 12 October 2026, W8 begins 30 November 2026 and the inclusive
24-week core ends 28 March 2027. Duration and event dates remain placeholders,
not newly agreed deadlines. The dashed dissemination extension is conditional.
Inadequate domain records narrow domain claims; they do not prevent the
independently specified controlled benchmark. A feasibility-driven reduction
must be recorded and frozen before evaluation outcomes.

## Scientific and cross-chapter checks

The problem, six research questions/objectives, alignment table, methods, and
evidence boundaries were checked together.

| Objective | Main method/evidence location | Interpretation retained |
|---|---|---|
| 1: Formulate | 3.2–3.3; Appendix A | Named architecture using established algebra |
| 2: Implement | 3.4, 3.10; Appendix E | Reproducibility and functional traceability |
| 3: Compare | 3.6 | Exact/uncertainty-qualified receiving references |
| 4: Dependence | 3.6.3–3.6.4, 3.7 | Conditional bracket; diagnostic may help or fail |
| 5: Cost | 3.8 | Matched boundaries, reference precision, adapter costs |
| 6: Instantiate | 3.5, 3.9 | Separate mappings and domain evidence limits |

The domain index remains non-probabilistic. The stochastic benchmark assigns
probability semantics only to its separately declared primitive process.
Conditional transmission remains w = S·tau, not Q after sampling upstream
activation. The bracket remains conditional on independent primitives and
DAG structure; it is not a domain calibration or a universal physical bound.

The primary benchmark remains separate from historical reruns and supporting
domain cases. A smaller score error is not assumed to produce a better ranking.
Receiving-state priority is not equated with source influence or intervention
benefit. Shared ancestry and identifiability limitations remain explicit.

A small Chapter I framework passage was reordered so that current-state
recursion leads directly into ranking, followed by the separate evaluation
interpretation. The rest of the formulation and benchmark protocol were
preserved.

## Numerical and reference checks

- Appendix A: R2 = 0.4456 and R3 = 0.3342 recomputed.
- Appendix B: Express R = 0.911767840385437 recomputed.
- Appendix C: all 11 displayed loading/capacity ratios checked within rounding;
  the 12-node trace gives risk sum approximately 1.186082.
- Inventory arithmetic checked: 560 branch scenarios; 3600 generated scenarios,
  including 720 development and 2880 evaluation scenarios; 48 precision audits.
  The additional 12 Express scenarios remain planned; the original snapshot
  has since been included and verified (see `INPUT_PROVENANCE_UPDATE.md`).
- All cited keys resolve. Four references not cited in the compiled proposal
  were removed from its current reference list; the previous full list is
  preserved in archive/references_before_full_pass.tex.
- This was a citation-key and manuscript-consistency audit, not a fresh
  independent verification of every primary publication or bibliography field.
- Historical results and worked numerical values were not changed. Restricted
  raw electrical data and the earlier N1--N5 fixture files were not authenticated
  by this manuscript review. The original Express snapshot was subsequently
  supplied and verified against the historical CSV hashes; see
  `INPUT_PROVENANCE_UPDATE.md` for the additional input checks.

The complete PDF was inspected through a layout overview; affected preliminary,
prototype, timeline, reference, and appendix pages were also checked at readable
resolution. Compilation and layout checks do not establish empirical validity
or institutional approval.

