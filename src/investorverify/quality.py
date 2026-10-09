"""Compute precision from actual independent audit; never invent scores."""
from __future__ import annotations
import json
from pathlib import Path
from .validate import read_csv,validate

def measure(data_dir: Path) -> dict:
    errors = validate(data_dir)
    if errors:
        return {"status":"invalid_data","errors":errors}
    pred = {row["investor_id"]:row["ai_prediction"] for row in read_csv(data_dir/"ai_predictions.csv")}
    audit = read_csv(data_dir/"manual_audit.csv")
    if not audit:
        return {"status":"not_measured","reason":"No independent manual audit records","audited":0}
    counts = {"TP":0,"FP":0,"FN":0,"TN":0}
    deferred = 0
    mapping = {("include","include"):"TP",("include","exclude"):"FP",("exclude","include"):"FN",("exclude","exclude"):"TN"}
    for row in audit:
        pair = (pred[row["investor_id"]],row["human_label"])
        if pair not in mapping:
            deferred += 1
        else:
            counts[mapping[pair]] += 1
    denom = counts["TP"] + counts["FP"]
    return {"status":"measured" if denom else "insufficient_positive_predictions",
            "audited":len(audit),"evaluated":sum(counts.values()),"ambiguous_or_deferred":deferred,
            **counts,"precision":counts["TP"]/denom if denom else None,
            "scope_note":"Precision applies only to the manually audited candidate sample"}

if __name__ == "__main__":
    print(json.dumps(measure(Path(__file__).resolve().parents[2]/"data"),indent=2))
