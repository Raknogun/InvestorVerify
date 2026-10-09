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
    def test_two_verified_candidates_still_preliminary(self):
        result=measure(ROOT/"data")
        self.assertEqual(result["status"],"preliminary_small_sample")
        self.assertEqual(result["audited"],2)
        self.assertEqual(result["TP"],2)
        self.assertEqual(result["FP"],0)
        self.assertEqual(result["precision"],1.0)
    def copy_fixture(self,target):
        for source in (ROOT/"data").glob("*.csv"):
            (target/source.name).write_bytes(source.read_bytes())
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
