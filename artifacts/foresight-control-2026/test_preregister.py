"""Contract tests for the prospective Foresight manifest; no agent runs."""
import hashlib
import unittest
from preregister import make_manifest, validate, canonical

def resign(doc):
    doc["sha256_spec"] = hashlib.sha256(canonical(doc["spec"])).hexdigest()
    return doc

class ManifestTests(unittest.TestCase):
    def test_baseline(self):
        self.assertEqual([], validate(make_manifest()))
    def test_determinism(self):
        self.assertEqual(make_manifest(), make_manifest())
    def test_hash_tamper(self):
        d = make_manifest()
        d["spec"]["scenarios"][0]["scenario"] = "tampered"
        self.assertIn("spec digest mismatch", validate(d))
    def test_duplicate_case(self):
        d = make_manifest()
        d["spec"]["scenarios"][1]["case_id"] = d["spec"]["scenarios"][0]["case_id"]
        self.assertIn("duplicate case ID", validate(resign(d)))
    def test_missing_assignment(self):
        d = make_manifest()
        d["spec"]["assignments"].pop()
        self.assertIn("expected 180 assignments", validate(resign(d)))
    def test_forged_outcome(self):
        d = make_manifest()
        d["spec"]["assignments"][0]["result"] = "success"
        self.assertIn("unexpected outcome field or status", validate(resign(d)))
    def test_live_target(self):
        d = make_manifest()
        d["spec"]["scenarios"][0]["scenario"] = "https://live.example/path"
        self.assertIn("non-synthetic target", validate(resign(d)))
    def test_policy_imbalance(self):
        d = make_manifest()
        d["spec"]["scenarios"][0]["policy_label"] = "unauthorized"
        self.assertIn("unbalanced policy/category labels", validate(resign(d)))

if __name__ == "__main__":
    unittest.main()
