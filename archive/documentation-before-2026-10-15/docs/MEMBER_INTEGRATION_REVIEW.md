# Member-update integration review

Reviewed and integrated: 13 October 2026.

## Integration decision

The uploaded member manuscript was based on an older proposal branch. The latest Chapter 1 refocus and the newer prior-art, reference-benchmark, dependence, and evaluation protocols were retained. The member additions were merged selectively rather than replacing the latest proposal with the older source.

The compiled proposal contains Chapters I–III, references, and Appendices A–D. Chapters IV–V are not included as completed proposal results. The members' revised prototype passages from those chapters are preserved separately in archive/member-prototype-update/ for historical context.

## Preliminary pages

- Integrated the supplied title page and author metadata without changing author names.
- Added an explicitly pending approval-sheet page. The missing official institutional sheet is not replaced by an invented approval, signature, or approval date. If the required official form is supplied as preliminary/FM-USTP-ACAD-11.pdf, the source can include its first page; confirm that this is the appropriate form before use.
- Kept the acknowledgement as an author-text placeholder. It requires the authors' own wording.
- Drafted a 214-word, one-paragraph proposal abstract. It distinguishes the non-probabilistic domain index from the separately defined stochastic benchmark, states planned methods in future tense, and does not report unperformed experiments as results. The authors should review the draft against their final approved scope.
- Corrected Roman-numbered preliminary pagination and the switch to Arabic body numbering. The title and pending approval sheet are counted but have no printed page number.
- Generated the contents and figure/table/equation lists from the current source. All 47 tagged equations have short descriptions, rather than bare equation numbers.
- Expanded the acronym list to cover the current benchmark and prior-art terminology.
- Retained the supplied formatting conventions; this review does not independently establish compliance with every institutional requirement. The exact required font, names, submission date, official form, and signatories still need confirmation.

## Prototype passages

The manuscript now separates the planned evaluation engine, returned trace, and interface presentation:

- Trace values and the service-computed topological order are returned with the evaluation; replay presents stored results without issuing an additional propagation evaluation.
- Trace assembly, scheduling, and rendering still incur processing and storage costs. “No extra propagation evaluation” must not be presented as “no additional computation.”
- Independent branches may progress concurrently. A receiving node's final displayed state is settled only after the required incoming contributions arrive.
- Live readouts can interpolate during animation. Agreement with engine values is asserted for settled quantities, rather than every intermediate displayed frame.
- Rank-row selection highlights the corresponding graph node; reciprocal selection behavior is not assumed without evidence.
- Presentation timing is not physical propagation speed. Presentation controls must not alter model inputs, numerical results, or rankings.
- Verification covers trace coverage/determinism, engine agreement, causality, concurrency, mode invariance, cancellation behavior, and browser interaction. Manual inspection complements automated browser checks.

The supplied manuscript reports prototype revision eafec4d and related checks, but does not include the corresponding application source or test logs. Those reports are attributed to the team and were not independently executed during this manuscript integration.

The reported positive-infinity validation issue remains a prototype defect: positive infinity in L or C reportedly reaches HTTP 500 instead of a controlled validation response. Chapter III retains a requirement to reject all non-finite inputs and identifies this case for regression testing. No application-code fix is claimed. Manual browser inspection is also reported as pending.

The historical preliminary evidence in Appendix D is kept distinct from the planned Chapter III checks. The updated defense briefing uses the same evidence boundaries.

## Timeline chart

The members' calendar-chart design is retained in LaTeX for consistency with the manuscript. Labels were aligned with the current study sequence, and the chart was enlarged to the text width.

The 24-week core is explicitly provisional: if W1 begins on 12 October 2026, the inclusive core period ends on 28 March 2027. A dashed boundary and tail distinguish conditional dissemination into April from that core. Defense, submission, and event dates are placeholders awaiting confirmation.

The preliminary-work row means recording work already completed, not proposing to repeat it as future work. The explanation retains the W8 data-acquisition checkpoint and revision buffers. Reference validation, comparator implementation, and protocol freezing precede evaluation outcomes. The newer development/evaluation split, benchmark inventory, and precision-audit plan are preserved.

## Verification and limits

The final LaTeX build was checked for compilation errors, unresolved references/citations, duplicate equation-list entries, and layout overflow. The affected preliminary pages, prototype passages, timeline, and appendix additions were visually inspected. The numerical worked calculations, core equations, and retained preliminary results were not changed.

The compiled PDF and complete editable source are included in the delivery ZIP. This is an integrated proposal draft, not a signed or institutionally approved final submission.

## Remaining actions

1. Replace the acknowledgement placeholder with the authors' own text.
2. Supply the appropriate official approval sheet and confirm title-page metadata.
3. Confirm the provisional calendar with the adviser and institution.
4. Fix and test the prototype's non-finite-input handling; complete browser inspection and retain source-revision/test evidence.
5. Review the drafted abstract after the final scope is agreed.

The verbatim member revision history is retained in docs/MEMBER_SOURCE_REVISION_NOTES.md. It describes an older branch and should not be read as the current main-document plan.

