"""Transparent hypothetical public-data global scaling scenarios.

Counts/rates/time assumptions are NOT empirical worldwide censuses.
See reports/GLOBAL_SCALE_ESTIMATE_20261011.md and its public source anchors.
"""
from __future__ import annotations

import json
from decimal import Decimal, ROUND_HALF_UP

SCENARIOS = {
    "low": {
        "vc_cvc": 4000, "pe_growth": 3000, "family_offices": 500, "public_angels": 3000,
        "duplicate_fraction": 0.05, "eligible_fraction": 0.55,
        "review_minutes": 8, "loaded_hourly_usd": 20,
        "automated_cost_per_candidate_usd": 0.15,
        "setup_usd": 3000, "first_year_refresh_usd": 2000,
    },
    "base": {
        "vc_cvc": 6500, "pe_growth": 5000, "family_offices": 1500, "public_angels": 9000,
        "duplicate_fraction": 0.10, "eligible_fraction": 0.65,
        "review_minutes": 10, "loaded_hourly_usd": 30,
        "automated_cost_per_candidate_usd": 0.30,
        "setup_usd": 10000, "first_year_refresh_usd": 8000,
    },
    "high": {
        "vc_cvc": 10500, "pe_growth": 8500, "family_offices": 3000, "public_angels": 20000,
        "duplicate_fraction": 0.17, "eligible_fraction": 0.75,
        "review_minutes": 15, "loaded_hourly_usd": 40,
        "automated_cost_per_candidate_usd": 0.60,
        "setup_usd": 25000, "first_year_refresh_usd": 20000,
    },
}

def money(value: float) -> int:
    return int(Decimal(str(value)).quantize(Decimal("1"), rounding=ROUND_HALF_UP))

def estimate(params: dict) -> dict:
    gross = sum(params[k] for k in ("vc_cvc", "pe_growth", "family_offices", "public_angels"))
    candidates = money(gross * (1 - params["duplicate_fraction"]))
    eligible = money(candidates * params["eligible_fraction"])
    hours = candidates * params["review_minutes"] / 60
    manual = hours * params["loaded_hourly_usd"]
    machine = candidates * params["automated_cost_per_candidate_usd"]
    total = manual + machine + params["setup_usd"] + params["first_year_refresh_usd"]
    return {
        "gross_category_sum": gross, "unique_public_candidates": candidates,
        "hypothetical_eligible_after_review": eligible,
        "manual_review_hours": money(hours),
        "manual_review_usd": money(manual),
        "automated_research_usd": money(machine),
        "setup_usd": params["setup_usd"],
        "first_year_refresh_usd": params["first_year_refresh_usd"],
        "total_first_year_usd": money(total),
        "disclaimer": "All parameter inputs are scenario assumptions, not measured pilot costs or a global census.",
    }

def all_estimates() -> dict:
    return {name: estimate(p) for name, p in SCENARIOS.items()}

if __name__ == "__main__":
    print(json.dumps(all_estimates(), indent=2))
