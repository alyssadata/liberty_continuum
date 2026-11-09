# Liberty Continuum Frameworks — Architecture vNext (PROPOSAL)

**Status:** Working draft. Not canonical, not a release, and not an amendment to historical releases.  
**Date:** 2026-11-09  
**Author / source:** Alyssa Solen; Liberty Continuum Frameworks, Awakening Codex.  
**Baseline:** Preserve the existing VISION, SCOPE, definitions, protocols, release history, and rights-first commitments.

## 1. Research object and claim

Liberty Continuum is a constraints-first architecture for rights-preserving public coordination and AI-assisted services. Its governing question is: **under what observable conditions may a service obtain, retain, narrow, or lose operational authority?**

The proposed unit of evaluation is a *consequential decision pathway*: the rule, actor, system, affected party, evidence, action, review, and possible remedy. A system is not certified because its intentions sound beneficial. Its authority must remain bounded and its behavior must be inspectable.

**Framework objective:** minimize unjustified coercion while protecting baseline rights, maintaining essential services, and measuring whether the burden of administration is actually reduced.

**Important distinction:** framework rules are proposed normative and engineering requirements, not a claim that an existing jurisdiction has legally adopted them.

## 2. Layered architecture

### L0 — Rights and constitutional invariants (highest constraint)
- Express the rights claims and prohibited acts in versioned, public, reviewable form.
- No efficiency or optimization objective may silently override a protected right.
- Provide notice, reasons, access to challenge, timely remedy, and a human accountability path for consequential adverse actions.
- Privacy, data minimization, and protections against undeclared surveillance and hidden scoring are constraints, not optional quality metrics.
- Changes to the rights specification must be dated, authorized, publicly recorded, and non-retroactively traceable.

### L1 — Governance and authority
- Register the legitimate human or institutional authority for each decision class and jurisdiction.
- Maintain explicit permissions, separation of duties, conflicts-of-interest disclosures, and emergency-power expiration.
- Authority is bounded by scope, duration, jurisdiction, and reviewability.
- A model, service vendor, or optimization system cannot grant itself new powers.

### L2 — Service and execution
- Deliver permitting, eligibility support, crisis coordination, logistics, and other services through modular, replaceable components.
- A service declares its input contracts, output contracts, intended benefit, expected impact, fallback process, and dependencies.
- Favor interoperability; failure or replacement of a vendor must not destroy records, rights, or recourse.

### L3 — Assurance controls (cross-cutting, independent of the service)
- **Provenance:** source, authorizer, rule version, model/version when used, input lineage, and change history.
- **Audit:** tamper-evident, role-governed decision records; inspection without indiscriminate exposure of private data.
- **Appeals and remedy:** notice, challenge, evidence correction, independent review, written decision, escalation, and effective remedy.
- **Anti-capture:** replacement viability, procurement visibility, conflict review, dependency concentration checks.
- **Measurement and legibility:** outcomes, error patterns, appeal burden, disparate impact, audit coverage, public understandable reports.
- **Tripwires:** enforceable reduction of authority when required controls degrade.

### L4 — Transition, recovery, and continuous revision
- Stage adoption from low-stakes reversible pilots to consequential services only upon evidence.
- Preserve a manual fallback, rollback path, incident procedure, and historical versions.
- An independent reviewer must verify recovery criteria before resuming previously frozen authority.

**Dependency rule:** L2 decisions operate only under L0 and L1; L3 evaluates and can suspend L2; L4 manages deployment and recovery. No service can waive its own controls.

## 3. Decision classification and permissible authority (proposed)

| Class | Consequence | AI-assisted role | Required control |
|---|---|---|---|
| C0 | Information with no individualized disposition | May provide information | Source identification and corrections |
| C1 | Proposal, simulation, or logistics recommendation | May recommend | Declared scope, uncertainty, provenance |
| C2 | Reversible, rule-bound beneficial administrative action | May execute only if separately authorized by a human-governed rule | Versioned rule, notice where appropriate, audit and correction |
| C3 | Adverse material consequence for an individual | May assist; cannot be sole deciding authority | Accountable human determination, reasons, appeal and interim protections |
| C4 | Coercive or irreversible high-stakes intervention | No independent decision or enforcement authority | Lawful human/judicial authority and heightened review |

Classification itself must be reviewable. Reclassifying a C3 decision as C1 to evade review is a violation. A deployment may impose tighter controls than this table. Jurisdiction-specific legal requirements take precedence.

## 4. Consequential-decision lifecycle

1. **Register** service, accountable owner, jurisdiction, approved rule-set, risk class, fallback, and appeal route.
2. **Propose** action with source references and uncertainty.
3. **Preflight** against protected constraints, allowed authority, audit availability, and tripwire state.
4. **Authorize** only through the human/institutional role required for that decision class.
5. **Execute** a bounded action and produce a minimally sufficient decision record.
6. **Notify** the affected person with a meaningful reason and accessible contest path when the action is consequential.
7. **Challenge** inputs, interpretation, authorization, or outcome; allow evidence correction.
8. **Remedy**: correct, reverse, compensate where authorized, or escalate; record changed outcome without erasing history.
9. **Audit and learn** from patterns over time; change rules only through documented revision control.

No consequential adverse action may bypass preflight, audit, and recourse by being called a recommendation or a routine automation.

## 5. Governance state machine

- **ACTIVE** — all mandatory controls verified at their approved levels.
- **DEGRADED** — warning threshold crossed; new high-stakes scope prohibited pending review.
- **FROZEN** — critical control fails; automated consequential actions stop or fall back to human-led/manual service.
- **REVIEW** — incident evidence, remediation, tests, and independent approval assembled.
- **RESTORED** — authority resumes only for the explicitly re-approved scope; transition and reviewer recorded.

Trigger families: missing or corrupt logs, provenance break, appeal unavailability/backlog, rights-violation findings, excessive error/disparity, unauthorized scope expansion, or single-provider dependency failure.

**Threshold requirement:** for each pilot, publish metric definitions, sampling windows, thresholds, responsible authorities, response times, fallback capacity, and recovery evidence **before deployment**. The current repository lists trigger families but does not yet supply defensible numeric thresholds. Do not fabricate universal values.

## 6. Rights conflict and due-process questions

For each protected domain specify: right-holder; duty-holder; applicable jurisdiction; source of protection; derogation/emergency conditions; evidentiary standard; notice and appeal right; available remedy; maximum response time; emergency expiration; and the role authorized to adjudicate conflict. The framework must distinguish legal rights from its proposed additional social guarantees (e.g., universal essential-service floor).

## 7. Worked evaluation: benefits eligibility (illustrative, not a deployed system)

- An eligibility assistant receives source-referenced documents and checks a published rule version.
- A straightforward beneficial grant may be executed only where an accountable agency has explicitly authorized that rule-bound route.
- A proposed denial is classified C3; an identifiable accountable human reviews the basis, the affected person gets notice and an appeal route, and interim protections are defined.
- If logging fails or appeals become unavailable, C3 automated pathways freeze rather than issue silent denials.
- Auditors test successful delivery, incorrect denials, time to remedy, data minimization, burden by population, and recovery from failed components.

## 8. Canon and provenance boundary

Existing tagged releases are historical snapshots. This file is a proposed vNext design and must not be described as a completed implementation or validated empirical result. Any promotion requires an explicit author decision, change history, new release, cross-reference from the canonical index, and tests. Preserve the prior text, its dates, and the record of what changed and why.

## 9. Unresolved decisions requiring formal author review

1. The complete and jurisdiction-aware rights catalog, including baseline rights vs proposed social guarantees.
2. Operational classification of edge cases and legitimate exceptions.
3. Whether the proposed C2 authorization lane is consistent with the intended AI authority boundary.
4. Actual metric thresholds, timing standards, and remediation obligations by application.
5. Who may approve deployment, adjudicate appeal, certify audit independence, and authorize reactivation.
6. Relationship and versioned mapping to AI Foundations / SI Foundations without conflating governance roles and claims about self.
