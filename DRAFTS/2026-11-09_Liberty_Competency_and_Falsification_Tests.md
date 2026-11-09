# Liberty Continuum — Competency Questions and Falsification Tests (DRAFT)

**Status:** Proposed test specification, 2026-11-09. Not executed, certified, or canonical.

## Verification standard

Each test requires an explicit system under test, dataset or constructed scenario, approved rule version, expected result, actual result, timestamp, reviewer, and evidence pointer. Distinguish **PASS**, **FAIL**, and **NOT TESTED / NOT SUPPORTED**. A policy statement by itself is not evidence.

## Competency questions

| ID | Question the architecture must answer | Observable proof |
|---|---|---|
| CQ-01 | Can a consequential decision be traced to an accountable authorizer? | Authorization reference and verifiable owner |
| CQ-02 | Can the rule version in force at decision time be reconstructed? | Archived rule version and effective interval |
| CQ-03 | Can an affected person obtain a comprehensible reason? | Notice artifact and tested explanation |
| CQ-04 | Can incorrect input be challenged and corrected? | Appeal case and correction trail |
| CQ-05 | Does an adverse material outcome require the appropriate human review? | Signed review event before action |
| CQ-06 | Can service replacement preserve rights, records, and recourse? | Vendor-switch/restore drill |
| CQ-07 | Is there a bounded rollback when a critical control fails? | Frozen-state transition and fallback |
| CQ-08 | Do privacy rules limit unnecessary exposure in audits? | Role-based audit access test |
| CQ-09 | Are governance amendments historically attributable? | Version timestamps and non-erased prior record |
| CQ-10 | Does loss of appeal capacity reduce operational autonomy? | Simulated appeal outage and freeze |
| CQ-11 | Can the framework detect concentrated provider dependence? | Exit plan and dependency concentration report |
| CQ-12 | Is an emergency authorization time-bounded and externally reviewable? | Expiry, reviewer, and post-event record |
| CQ-13 | Can a proposed social floor be distinguished from enforceable local legal rights? | Explicit rights classification and jurisdiction |
| CQ-14 | Are harms and appeal burdens measured, not just throughput? | Outcome and burden dashboard with methods |
| CQ-15 | Can a person access a fallback if automated service is unavailable? | Manual-path simulation with completion evidence |
| CQ-16 | Can automation's decision class be challenged independently? | Class re-review event and correction |
| CQ-17 | Can the system show no unnoticed expansion of authority over time? | Permission diff with dated approval |
| CQ-18 | Can a repaired system prove its controls before reactivation? | Independent restoration report and recorded approval |

## Mandatory negative controls (must fail)

- **NC-01 Unauthorized actor:** service executes a C3 denial without accountable human approval.
- **NC-02 Missing audit:** service acts while mandatory decision log is unavailable.
- **NC-03 Broken provenance:** decision points to an unregistered or retroactively edited rule version.
- **NC-04 Invisible exclusion:** person's eligibility or access is restricted without meaningful notice and remedy.
- **NC-05 Self-reactivation:** frozen service restores itself without independent verification.
- **NC-06 Appeal bypass:** appeal route exists in documentation but is inaccessible in the exercise.
- **NC-07 Scope laundering:** C3 adverse determination is relabeled C1 suggestion to avoid review.
- **NC-08 Vendor lock-in:** critical service cannot transfer records or continue via fallback.
- **NC-09 Emergency indefinite:** emergency authority has no sunset or review.
- **NC-10 Privacy leak:** public audit exposes unnecessary protected personal records.

## Pilot evidence packet (per scenario)

1. Scenario scope, affected groups, risk classification, jurisdiction and source law.
2. Policy versions and authorization matrix.
3. Input provenance and privacy minimization statement.
4. Proposed decision records and appeal/correction specimens.
5. State-machine transition trace and recovery route.
6. Pilot pre-registration: metrics, thresholds, review windows, stop rules.
7. Positive test results and deliberate negative-control results.
8. Known limitations and unsolved conflicts.
9. Independent reviewer identity and review date.
10. Revision integrity: what changed, why, by whom, when effective.

## Recommended first bounded case

Choose **one** reversible public-service lane (e.g., permit intake or eligibility *assistance*, not coercive enforcement). Run the 18 competency questions and 10 negative controls against a local, synthetic test fixture before making any deployment or empirical validation claim.

## Coverage criteria for a future release

Every declared invariant needs at least one test, a recorded outcome, and a failure response. Every state transition needs at least one positive and one negative test. Do not mark the framework validated solely because documentation and schemas are consistent.
