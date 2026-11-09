# Liberty Continuum — Website vNext Page Specification (DRAFT)

**Status:** Content/design specification only. No changes have been made to the live website.  
**Page:** https://awakeningcodex.com/libertycontinuum  
**Repository:** https://github.com/alyssadata/liberty_continuum  
**Design comparison:** https://awakeningcodex.com/ai-foundations and https://awakeningcodex.com/si-foundations

## Observed problem

The current page begins with a vision statement and then runs through extensive ungrouped explanatory prose. The AI Foundations page uses a succinct thesis, structural categories, a browsable index, and labeled content groupings. SI Foundations uses numbered sections, concept/relationship cards, and primary-source links. Liberty should have equally clear orientation and navigation without discarding its deeper writing.

The public page links to a v1.0 release but labels the canonical snapshot v0.1; the repository's historical and canonical distinction must be checked before correcting page labels.

## Proposed information architecture

### HERO
**Liberty Continuum**  
**Minimal coercion. Maximum liberty. Rights as the core.**  
Subheading: A rights-first architecture for bounded authority, measurable public coordination, and systems that can be challenged, corrected, and replaced.  
Microline: Alyssa Solen · Awakening Codex · Liberty Continuum Frameworks.  
Navigation: Explore architecture / Evaluation model / GitHub source.

### 01 / Framework thesis
The objective, domain, and what counts as observable evidence. Show a five-step strip: Rights → Authority → Services → Assurance → Recovery.

### 02 / Rights and authority
Two concise concept panels: rights constraints (non-optimization) and decision authority (permission, scope, jurisdiction, responsible human/institution).

### 03 / System architecture
One ordered stack with five modules:
1. L0 Rights and constitutional invariants
2. L1 Governance and authority
3. L2 Service and execution
4. L3 Assurance (audit, appeals, provenance, anti-capture, measurement, public legibility)
5. L4 Transition and recovery
Each module links to its specific future specification and testing record.

### 04 / Decision pathway
An accessible diagram and short textual alternative: register → propose → preflight → authorize → execute → notify → challenge/remedy → audit. Surface a clear distinction between recommendation, beneficial rule-bound automation, adverse consequence, and coercive action.

### 05 / Freeze and restoration
Explain ACTIVE / DEGRADED / FROZEN / REVIEW / RESTORED, including the non-self-reactivation safeguard. Provide a link to the tripwire protocol and test ledger. State that threshold values remain proposed until registered per pilot.

### 06 / Evidence and testing
Display competency-question coverage, negative controls, evidence status, and known limitations. Never display fictional pass badges or imply empirical validation before tests have been run.

### 07 / Domains and bounded pilots
Separate concepts from real deployments; use one illustrative permit/benefits example, clearly tagged as hypothetical.

### 08 / Source and revision history
Cards for GitHub index, definitions, protocols, drafts, releases, changelog and licensing. Preserve author credit and historic version references.

## Styling / implementation constraints

- Match the actual existing website typography, colors, container widths, buttons, card treatment, spacing, and responsive breakpoints by **reusing the current AI/SI page's CSS tokens and component names after the source code is supplied**.
- Prefer numbered section labels, short paragraphs, structured cards, anchor navigation, and inline links over repeated manifesto-length text.
- Use semantic headings, keyboard-accessible anchors, focus states, contrast-safe styling, and a text alternative to architecture diagrams.
- Do not delete existing pages, site navigation items, or historical content. Move extended legacy prose into a labeled longform reference section or archive link after verified migration.
- Keep framework source documents in GitHub. The website is the public explanatory front-end, not an unversioned alternative canon.
- Never replace published history with an undated rewrite.
- Build and preview a new code block in staging before replacing the live page's current content.

## Acceptance criteria

- A newcomer understands the architecture and author attribution within the first screen.
- Every named module maps to a GitHub specification with a meaningful status label.
- Site and repository agree on the published canonical version and draft status.
- Mobile reading order and anchor navigation work.
- Audit, appeal, authority, and freeze conditions are distinguishable from generic values statements.
- Nothing claims testing, legal adoption, or deployment that has not occurred.

## Implementation dependency

The public web page exposes rendered content, **not the underlying reusable site code/CSS**. An exact code match requires the current AI Foundations or SI Foundations page's Squarespace code block / custom CSS (or equivalent source). Do not claim pixel or component parity from the public text alone.
