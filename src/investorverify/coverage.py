"""Human-verified completeness among manually included pilot investors.

An investee's sector is NOT necessarily the investor's usual sector.
Round sizes are NOT investor tickets; fund sizes are NOT dry powder.
"""
from __future__ import annotations
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "data"
FAMILIES = {
    "sector_strategy": {"sector_focus", "sector_focus_reported"},
    "investment_stage": {"investment_stage", "stage"},
    "ticket_lower": {"typical_ticket_min", "typical_ticket_min_historical"},
    "ticket_upper": {"typical_ticket_max", "typical_ticket_max_historical"},
    "reported_fund_or_managed_capital": {
        "managed_capital_reported", "aum_reported", "current_fund_size_reported",
        "fund_size_reported", "reported_fund_capital",
    },
}

def load_csv(filename: str, data_dir: Path = ROOT) -> list[dict[str, str]]:
    with (data_dir / filename).open(newline="", encoding="utf-8-sig") as stream:
        return list(csv.DictReader(stream))

def coverage(data_dir: Path = ROOT) -> dict:
    included = {r["investor_id"] for r in load_csv("manual_audit.csv", data_dir)
                if r["human_label"] == "include"}
    verified = {id_: set() for id_ in included}
    for entry in load_csv("evidence.csv", data_dir):
        if (entry["investor_id"] in verified
                and entry["verification_status"] == "human_verified"
                and entry["value"].strip()):
            verified[entry["investor_id"]].add(entry["field"])
    result = {"included_investors": len(included), "note":
              "Only human_verified evidence counts. Investor type and amount attribution must be interpreted separately."}
    for name, fields in FAMILIES.items():
        result[name] = sum(bool(verified[id_] & fields) for id_ in included)
    result["typical_ticket_range_both_bounds"] = sum(
        bool(verified[id_] & FAMILIES["ticket_lower"]) and
        bool(verified[id_] & FAMILIES["ticket_upper"]) for id_ in included)
    del result["ticket_lower"]
    del result["ticket_upper"]
    return result

if __name__ == "__main__":
    print(json.dumps(coverage(), indent=2))
