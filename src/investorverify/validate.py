"""Validate CSV schema, source pointers and references (not factual truth)."""
from __future__ import annotations
import csv
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

REQUIRED = {
 "candidates.csv": {"investor_id","name","aliases","country_focus","category_proposed","discovery_source_url","status"},
 "evidence.csv": {"evidence_id","investor_id","field","value","unit","source_url","source_type","source_published_date","accessed_date","verification_status","notes"},
 "ai_predictions.csv": {"investor_id","ai_prediction","reason","supporting_evidence_ids","prediction_date","human_review_status"},
 "manual_audit.csv": {"investor_id","human_label","reviewer","review_date","minutes_spent","evidence_checked","decision_reason"}
}
NUMERIC = {"typical_ticket_min","typical_ticket_max","typical_ticket_min_historical","typical_ticket_max_historical","funds_managed_historical","portfolio_company_count_2025q4","managed_capital_reported","funds_managed_count","optional_initial_cash","follow_on_investment_ceiling","new_fund_target","aum_reported","current_fund_size_reported","fund_size_reported","reported_fund_capital"}
SOURCE_TYPES = {"primary","association","press","government","regulatory","other"}
EVIDENCE_STATUSES = {"pending_manual_review","ai_source_checked_pending_human","human_verified","rejected"}

def is_public_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.hostname) and parsed.hostname not in {"localhost", "127.0.0.1", "::1"}

def read_csv(path: Path) -> list[dict[str,str]]:
    with path.open(encoding="utf-8-sig",newline="") as file:
        reader = csv.DictReader(file)
        missing = REQUIRED[path.name] - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"{path.name}: missing columns {sorted(missing)}")
        return list(reader)

def valid_date(value: str) -> bool:
    try:
        date.fromisoformat(value)
        return True
    except ValueError:
        return False

def validate(data_dir: Path) -> list[str]:
    errors = []
    try:
        tables = {name: read_csv(data_dir / name) for name in REQUIRED}
    except (OSError,ValueError) as e:
        return [str(e)]
    candidates,evidence,predictions,audit = (tables[name] for name in REQUIRED)
    if not candidates: errors.append("candidates.csv: empty")
    if not evidence: errors.append("evidence.csv: empty")
    ids,names = set(),set()
    for line,row in enumerate(candidates,2):
        ident,name = row["investor_id"].strip(),row["name"].strip()
        if not ident or not name: errors.append(f"candidates.csv:{line}: missing id/name")
        if ident in ids or name.casefold() in names: errors.append(f"candidates.csv:{line}: duplicate")
        ids.add(ident); names.add(name.casefold())
        if not is_public_url(row["discovery_source_url"]): errors.append(f"candidates.csv:{line}: invalid source URL")
    evidence_owners = {}
    for line,row in enumerate(evidence,2):
        ref = row["evidence_id"]
        if not ref or ref in evidence_owners: errors.append(f"evidence.csv:{line}: duplicate/missing ID")
        evidence_owners[ref] = row["investor_id"]
        if row["investor_id"] not in ids: errors.append(f"evidence.csv:{line}: unknown investor")
        if not row["field"].strip() or not row["value"].strip(): errors.append(f"evidence.csv:{line}: missing field/value")
        if not is_public_url(row["source_url"]): errors.append(f"evidence.csv:{line}: invalid source URL")
        if row["source_type"] not in SOURCE_TYPES: errors.append(f"evidence.csv:{line}: unknown source type")
        if row["verification_status"] not in EVIDENCE_STATUSES: errors.append(f"evidence.csv:{line}: unknown status")
        if not valid_date(row["accessed_date"]): errors.append(f"evidence.csv:{line}: invalid access date")
        if row["source_published_date"] and not valid_date(row["source_published_date"]):
            errors.append(f"evidence.csv:{line}: invalid published date")
        if row["field"] in NUMERIC:
            try:
                if float(row["value"]) < 0: raise ValueError()
            except ValueError:
                errors.append(f"evidence.csv:{line}: invalid numeric value")
            if not row["unit"]: errors.append(f"evidence.csv:{line}: missing numeric unit")
    seen = set()
    for line,row in enumerate(predictions,2):
        ident = row["investor_id"]
        if ident in seen or ident not in ids: errors.append(f"ai_predictions.csv:{line}: duplicate/unknown investor")
        seen.add(ident)
        if row["ai_prediction"] not in {"include","exclude","review"}: errors.append(f"ai_predictions.csv:{line}: unknown prediction")
        if not valid_date(row["prediction_date"]): errors.append(f"ai_predictions.csv:{line}: invalid date")
        refs = [ref.strip() for ref in row["supporting_evidence_ids"].split(";") if ref.strip()]
        if not refs or any(evidence_owners.get(ref) != ident for ref in refs):
            errors.append(f"ai_predictions.csv:{line}: missing, unknown or cross-investor evidence")
    # Discovery-only entries deliberately have no AI prediction and cannot count as screened.
    missing_screen = [row["investor_id"] for row in candidates
                      if row["investor_id"] not in seen and row["status"] != "discovered_unreviewed"]
    if missing_screen:
        errors.append(f"ai_predictions.csv: missing predictions for screened candidates: {missing_screen}")
    for line,row in enumerate(candidates,2):
        if row["status"] == "discovered_unreviewed" and row["investor_id"] in seen:
            errors.append(f"candidates.csv:{line}: discovery-only row already has AI prediction; update workflow status")
        if row["status"] == "ai_screened_pending_human" and row["investor_id"] not in seen:
            errors.append(f"candidates.csv:{line}: screened row missing AI decision")
    reviewed = set()
    for line,row in enumerate(audit,2):
        ident = row["investor_id"]
        if ident not in ids or ident in reviewed: errors.append(f"manual_audit.csv:{line}: unknown/duplicate investor")
        reviewed.add(ident)
        if row["human_label"] not in {"include","exclude","unclear"}: errors.append(f"manual_audit.csv:{line}: unknown label")
        if not row["reviewer"] or not row["evidence_checked"] or not row["decision_reason"]:
            errors.append(f"manual_audit.csv:{line}: reviewer/evidence/reason missing")
        if not valid_date(row["review_date"]): errors.append(f"manual_audit.csv:{line}: invalid date")
        if row["minutes_spent"].strip():
            try:
                if float(row["minutes_spent"]) <= 0: raise ValueError()
            except ValueError:
                errors.append(f"manual_audit.csv:{line}: invalid minutes")
        for link in row["evidence_checked"].split(";"):
            if not is_public_url(link.strip()):
                errors.append(f"manual_audit.csv:{line}: invalid evidence URL")
    return errors

if __name__ == "__main__":
    errors = validate(Path(__file__).resolve().parents[2] / "data")
    for error in errors: print("ERROR:",error)
    print(f'Validation: {"FAIL" if errors else "PASS"} ({len(errors)} errors)')
    raise SystemExit(bool(errors))
