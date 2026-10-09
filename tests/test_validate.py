"""Technical tests. The manual-audit fixture is synthetic and is NOT a quality result."""
import csv
import tempfile
import unittest
from pathlib import Path
from investorverify.validate import validate,is_public_url
from investorverify.quality import measure

ROOT = Path(__file__).resolve().parents[1]

class ValidationTests(unittest.TestCase):
    def test_seed_data(self):
        self.assertEqual(validate(ROOT/"data"), [])
    def test_public_urls(self):
        self.assertTrue(is_public_url("https://example.org/portfolio"))
        self.assertFalse(is_public_url("http://localhost/a"))
        self.assertFalse(is_public_url("file:///etc/passwd"))
    def test_eight_reviewed_one_ai_abstention(self):
        result=measure(ROOT/"data")
        self.assertEqual(result["status"],"preliminary_small_sample")
        self.assertEqual(result["audited"],8)
        self.assertEqual(result["evaluated"],7)
        self.assertEqual(result["ambiguous_or_deferred"],1)
        self.assertEqual(result["TP"],5)
        self.assertEqual(result["TN"],2)
        self.assertEqual(result["FP"],0)
        self.assertEqual(result["precision"],1.0)
    def copy_fixture(self,target):
        for source in (ROOT/"data").glob("*.csv"):
            (target/source.name).write_bytes(source.read_bytes())
    def test_n1_capital_claim_unit_is_validated(self):
        with tempfile.TemporaryDirectory() as tmp:
            target=Path(tmp); self.copy_fixture(target)
            source=(target/"evidence.csv").read_text(encoding="utf-8")
            self.assertIn("E040,czvc004,managed_capital_reported,60000000,USD",source)
            (target/"evidence.csv").write_text(source.replace("E040,czvc004,managed_capital_reported,60000000,USD","E040,czvc004,managed_capital_reported,60000000,"),encoding="utf-8")
            self.assertTrue(any("missing numeric unit" in e for e in validate(target)))

    def test_extended_discovery_coverage(self):
        from investorverify.discover import load_rows, merge
        existing = load_rows(ROOT/"data"/"candidates.csv")
        sightings = load_rows(ROOT/"data"/"discovery_sightings.csv")
        self.assertEqual(len(existing), 27)
        self.assertEqual(len(sightings), 25)
        combined, added, matches = merge(existing, sightings)
        self.assertEqual(len(combined), 27)
        self.assertEqual(len(added), 0)
        self.assertEqual(len(matches), 25)
        self.assertFalse(any(r["investor_id"] in {"czneg001","czneg002"}
                             and r["status"] == "discovered_unreviewed" for r in combined))

    def test_alias_collision_and_idempotent_merge(self):
        from investorverify.discover import merge, name_key
        self.assertEqual(name_key("Nation 1"), name_key("Nation1"))
        base = [{"investor_id": "czvc004", "name": "Nation1", "aliases": "N1; Nation 1", "status":"reviewed",
                 "country_focus": "CZ", "category_proposed": "VC", "discovery_source_url":"https://example.org"}]
        sightings = [
            {"candidate_name": "N1", "source_url": "https://example.org"},
            {"candidate_name": "Beta Ventures", "source_url": "https://example.org"}
        ]
        combined, added, duplicates = merge(base, sightings)
        self.assertEqual((len(combined),len(added),len(duplicates)),(2,1,1))
        again, more, duplicates2 = merge(combined, sightings)
        self.assertEqual((len(again),len(more),len(duplicates2)),(2,0,2))

    def test_html_headings_stay_staged(self):
        from investorverify.discover import parse_directory_headings
        html = "<h4>Alpha VC</h4><h4><span>Beta</span> Ventures</h4><h4>Alpha VC</h4>"
        self.assertEqual(parse_directory_headings(html), ["Alpha VC","Beta Ventures"])

    def test_old_missing_screening_still_invalid(self):
        from investorverify.validate import validate
        with tempfile.TemporaryDirectory() as tmp:
            target=Path(tmp); self.copy_fixture(target)
            path=target/"ai_predictions.csv"
            lines=path.read_text(encoding="utf-8").splitlines()
            path.write_text("\n".join(row for row in lines if not row.startswith("czvc001,"))+"\n",encoding="utf-8")
            self.assertTrue(any("missing predictions for screened candidates" in e for e in validate(target)))

    def test_frozen_screening_batch_and_source_links(self):
        from investorverify.discover import load_rows
        candidates=load_rows(ROOT/"data"/"candidates.csv")
        predictions=load_rows(ROOT/"data"/"ai_predictions.csv")
        evidence=load_rows(ROOT/"data"/"evidence.csv")
        new={row["investor_id"]:row for row in candidates if row["investor_id"].startswith("cznew")}
        newer=[row for row in predictions if row["investor_id"].startswith("cznew")]
        self.assertEqual(len(new),20)
        self.assertEqual(len(newer),20)
        self.assertEqual({label:sum(1 for r in newer if r["ai_prediction"]==label)
                         for label in ["include","review","exclude"]},
                         {"include":13,"review":5,"exclude":2})
        self.assertTrue(all(r["status"]=="ai_screened_pending_human" for r in new.values()))
        self.assertEqual([r["investor_id"] for r in newer if r["human_review_status"]=="reviewed"],["cznew010"])
        self.assertEqual(sum(r["human_review_status"]=="not_reviewed" for r in newer),19)
        owner={r["evidence_id"]:r["investor_id"] for r in evidence}
        self.assertTrue(all(all(owner.get(x)==r["investor_id"] for x in
                            r["supporting_evidence_ids"].split(";")) for r in newer))
        self.assertEqual(len(evidence),96)

    def test_mixed_type_angel_group_is_not_false_investor_label(self):
        from investorverify.discover import load_rows
        rows={r["investor_id"]:r for r in load_rows(ROOT/"data"/"ai_predictions.csv")}
        self.assertEqual(rows["cznew014"]["ai_prediction"],"exclude")
        self.assertIn("angel",rows["cznew014"]["reason"].lower())
        self.assertEqual(rows["cznew001"]["ai_prediction"],"review")

    def test_startupyard_partner_financing_not_as_own_ticket(self):
        from investorverify.discover import load_rows
        evidence={r["evidence_id"]:r for r in load_rows(ROOT/"data"/"evidence.csv")}
        self.assertEqual(evidence["E065"]["field"],"partner_follow_on_investment_ceiling")
        self.assertEqual(evidence["E065"]["value"],"100000")
        self.assertIn("DEPO",evidence["E065"]["notes"])
        self.assertEqual(evidence["E088"]["field"],"in_kind_convertible_note_value")
        self.assertEqual(evidence["E089"]["unit"],"percent")
        self.assertEqual(evidence["E064"]["verification_status"],"human_verified")
        self.assertEqual(evidence["E091"]["value"],"70000")
        predictions={r["investor_id"]:r for r in load_rows(ROOT/"data"/"ai_predictions.csv")}
        self.assertEqual(predictions["cznew001"]["ai_prediction"],"review")
        self.assertEqual(predictions["cznew001"]["human_review_status"],"not_reviewed")

    def test_purple_strategy_author_checked_transaction_still_pending(self):
        from investorverify.discover import load_rows
        evidence={r["evidence_id"]:r for r in load_rows(ROOT/"data"/"evidence.csv")}
        for key in ["E053","E077","E078","E092","E093","E094","E095"]:
            self.assertEqual(evidence[key]["verification_status"],"human_verified")
        self.assertEqual(evidence["E096"]["verification_status"],"human_verified")
        self.assertIn("financing rounds",evidence["E095"]["value"])
        predictions={r["investor_id"]:r for r in load_rows(ROOT/"data"/"ai_predictions.csv")}
        self.assertEqual(predictions["cznew010"]["ai_prediction"],"include")
        self.assertEqual(predictions["cznew010"]["human_review_status"],"reviewed")
        self.assertEqual(measure(ROOT/"data")["audited"],8)

    def test_bad_evidence_reference(self):
        with tempfile.TemporaryDirectory() as tmp:
            target=Path(tmp); self.copy_fixture(target)
            path=target/"ai_predictions.csv"
            path.write_text(path.read_text().replace("E001;E006","E999;E006"))
            self.assertTrue(any("cross-investor evidence" in e for e in validate(target)))
    def test_quality_math_synthetic_labels(self):
        with tempfile.TemporaryDirectory() as tmp:
            target=Path(tmp); self.copy_fixture(target)
            with (target/"manual_audit.csv").open("w",encoding="utf-8",newline="") as f:
                w=csv.writer(f)
                w.writerow(["investor_id","human_label","reviewer","review_date","minutes_spent","evidence_checked","decision_reason"])
                for ident,label,url in [
                  ("czvc001","include","https://www.credoventures.com/"),
                  ("czvc002","exclude","https://cvca.cz/en/depo-ventures-2/"),
                  ("czneg001","exclude","https://cvca.cz/en/about-us/"),
                  ("czvc004","unclear","https://cvca.cz/en/nation1-2/")
                ]:
                    w.writerow([ident,label,"test_fixture","2026-10-09","5",url,"synthetic test only"])
            result=measure(target)
            self.assertEqual((result["TP"],result["FP"],result["TN"],result["ambiguous_or_deferred"]),(1,1,1,1))
            self.assertEqual(result["precision"],0.5)

if __name__=="__main__":
    unittest.main()
