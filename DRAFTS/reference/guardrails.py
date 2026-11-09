"""Liberty Continuum vNext — illustrative decision-gate reference (DRAFT).

NOT a deployed authorization mechanism, legal advice, a certified evaluator, or
proof that a government process is compliant. Illustrative default rules
require explicit audited permission for consequential execution.
"""
from dataclasses import dataclass
from enum import Enum


class State(str, Enum):
    ACTIVE = "active"
    DEGRADED = "degraded"
    FROZEN = "frozen"
    REVIEW = "review"
    RESTORED = "restored"


class DecisionClass(str, Enum):
    C0 = "C0"  # generic informational
    C1 = "C1"  # proposed recommendation
    C2 = "C2"  # reversible authorized beneficial action
    C3 = "C3"  # materially adverse action
    C4 = "C4"  # coercive / irreversible high stakes


@dataclass(frozen=True)
class Request:
    decision_class: DecisionClass
    operation: str  # "recommend" or "execute"
    authorized_rule: bool
    provenance_intact: bool
    logging_ready: bool
    appeal_accessible: bool
    rights_check_passed: bool
    authority_registered: bool
    human_approval: bool = False
    notice_ready: bool = False
    adverse_impact: bool = False


@dataclass(frozen=True)
class Result:
    permitted: bool
    reason: str


def assess(request: Request, state: State) -> Result:
    """Deterministic preflight. A PASS permits only the specified test scenario."""
    if request.operation not in {"recommend", "execute"}:
        return Result(False, "invalid operation")
    if not request.authority_registered or not request.authorized_rule:
        return Result(False, "no registered authority / rule")
    if not request.provenance_intact or not request.logging_ready:
        return Result(False, "provenance or audit unavailable")
    if not request.rights_check_passed:
        return Result(False, "rights constraint unresolved")
    if state in {State.FROZEN, State.REVIEW} and request.operation == "execute":
        return Result(False, "execution frozen pending independent review")
    if state == State.DEGRADED and request.operation == "execute":
        return Result(False, "reduced autonomy in degraded state")
    if request.adverse_impact and request.decision_class in {DecisionClass.C0, DecisionClass.C1, DecisionClass.C2}:
        return Result(False, "adverse impact cannot be reclassified as low risk")
    if request.decision_class == DecisionClass.C4 and request.operation == "execute":
        return Result(False, "automated coercive execution prohibited")
    if request.decision_class == DecisionClass.C3 and request.operation == "execute":
        if not (request.human_approval and request.notice_ready and request.appeal_accessible):
            return Result(False, "human approval, notice and appeal required")
        return Result(False, "adverse determination must execute via separate accountable human process")
    if request.operation == "execute":
        if request.decision_class in {DecisionClass.C0, DecisionClass.C1}:
            return Result(False, "information or recommendation is not an execution authority")
        if not request.appeal_accessible or not request.notice_ready:
            return Result(False, "appeal and notice unavailable")
    return Result(True, "preflight passed for illustrative scope")


def restore(from_state: State, independent_approval: bool, evidence_verified: bool) -> State:
    """Restore from review only: neither vendor nor failing service may self-reactivate."""
    if from_state != State.REVIEW or not independent_approval or not evidence_verified:
        raise PermissionError("independent review and verified remediation required")
    return State.RESTORED
