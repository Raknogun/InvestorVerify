"""Regression tests for disclosed-data completeness and hypothetical cost scenarios."""
import unittest
from investorverify.coverage import coverage
from investorverify.global_estimate import all_estimates, estimate, SCENARIOS


class GlobalScenarioTests(unittest.TestCase):
    def test_scenario_model_reproduces_report(self):
        out = all_estimates()
        self.assertEqual(out["low"]["unique_public_candidates"], 9975)
        self.assertEqual(out["low"]["total_first_year_usd"], 33096)
        self.assertEqual(out["base"]["unique_public_candidates"], 19800)
        self.assertEqual(out["base"]["hypothetical_eligible_after_review"], 12870)
        self.assertEqual(out["base"]["total_first_year_usd"], 122940)
        self.assertEqual(out["high"]["unique_public_candidates"], 34860)
        self.assertEqual(out["high"]["total_first_year_usd"], 414516)

    def test_wider_world_review_is_more_expensive(self):
        lo, base, hi = [estimate(SCENARIOS[k])["total_first_year_usd"]
                        for k in ("low", "base", "high")]
        self.assertLess(lo, base)
        self.assertLess(base, hi)

    def test_human_verified_field_coverage(self):
        fields = coverage()
        self.assertEqual(fields["included_investors"], 16)
        self.assertEqual(fields["sector_strategy"], 2)
        self.assertEqual(fields["investment_stage"], 4)
        self.assertEqual(fields["typical_ticket_range_both_bounds"], 4)
        self.assertEqual(fields["reported_fund_or_managed_capital"], 2)


if __name__ == "__main__":
    unittest.main()
