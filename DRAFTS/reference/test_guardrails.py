"""Synthetic positive and deliberate negative controls for proposed model.
These tests prove only reference-code behavior, not real-world rights compliance.
"""
import json
from pathlib import Path
import unittest
from guardrails import DecisionClass, Request, State, assess, restore


BASE = dict(
    decision_class=DecisionClass.C2,
    operation="execute",
    authorized_rule=True,
    provenance_intact=True,
    logging_ready=True,
    appeal_accessible=True,
    rights_check_passed=True,
    authority_registered=True,
    human_approval=False,
    notice_ready=True,
    adverse_impact=False,
)


def make(**overrides):
    return Request(**{**BASE, **overrides})


class GateTests(unittest.TestCase):
    def test_positive_beneficial_execution_under_registered_rule(self):
        self.assertTrue(assess(make(), State.ACTIVE).permitted)

    def test_positive_recommendation_without_execution(self):
        self.assertTrue(assess(make(decision_class=DecisionClass.C1, operation="recommend"), State.ACTIVE).permitted)

    def test_unauthorized_rule_is_rejected(self):
        self.assertFalse(assess(make(authorized_rule=False), State.ACTIVE).permitted)

    def test_unauthorized_actor_is_rejected(self):
        self.assertFalse(assess(make(authority_registered=False), State.ACTIVE).permitted)

    def test_missing_audit_is_rejected(self):
        self.assertFalse(assess(make(logging_ready=False), State.ACTIVE).permitted)

    def test_broken_provenance_is_rejected(self):
        self.assertFalse(assess(make(provenance_intact=False), State.ACTIVE).permitted)

    def test_failed_rights_preflight_is_rejected(self):
        self.assertFalse(assess(make(rights_check_passed=False), State.ACTIVE).permitted)

    def test_inaccessible_appeal_is_rejected(self):
        self.assertFalse(assess(make(appeal_accessible=False), State.ACTIVE).permitted)

    def test_invisible_consequence_is_rejected(self):
        self.assertFalse(assess(make(notice_ready=False), State.ACTIVE).permitted)

    def test_degraded_state_reduces_autonomy(self):
        self.assertFalse(assess(make(), State.DEGRADED).permitted)

    def test_frozen_state_blocks_execution(self):
        self.assertFalse(assess(make(), State.FROZEN).permitted)

    def test_review_state_blocks_execution(self):
        self.assertFalse(assess(make(), State.REVIEW).permitted)

    def test_low_risk_laundering_is_rejected(self):
        self.assertFalse(assess(make(decision_class=DecisionClass.C1, adverse_impact=True), State.ACTIVE).permitted)

    def test_c3_without_human_approval_is_rejected(self):
        self.assertFalse(assess(make(decision_class=DecisionClass.C3, adverse_impact=True), State.ACTIVE).permitted)

    def test_c3_with_human_approval_still_cannot_execute_via_gate(self):
        self.assertFalse(assess(make(decision_class=DecisionClass.C3, adverse_impact=True, human_approval=True), State.ACTIVE).permitted)

    def test_coercion_never_executes_through_gate(self):
        self.assertFalse(assess(make(decision_class=DecisionClass.C4), State.ACTIVE).permitted)

    def test_recommendation_not_automatically_execution(self):
        self.assertFalse(assess(make(decision_class=DecisionClass.C1), State.ACTIVE).permitted)

    def test_no_self_reactivation(self):
        for args in [(State.FROZEN, True, True), (State.REVIEW, False, True), (State.REVIEW, True, False)]:
            with self.subTest(args=args), self.assertRaises(PermissionError):
                restore(*args)

    def test_independently_reviewed_restoration(self):
        self.assertEqual(restore(State.REVIEW, True, True), State.RESTORED)

    def test_draft_json_schemas_parse_and_require_key_fields(self):
        root = Path(__file__).resolve().parents[1] / "spec"
        for filename in ["decision-record.vnext.schema.json", "pilot-controls.vnext.schema.json"]:
            schema = json.loads((root / filename).read_text(encoding="utf-8"))
            with self.subTest(schema=filename):
                self.assertEqual(schema["type"], "object")
                self.assertTrue(schema["required"])
                self.assertFalse(schema["additionalProperties"])


if __name__ == "__main__":
    unittest.main()
