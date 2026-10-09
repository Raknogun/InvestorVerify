import unittest
from pathlib import Path
from investorverify.validate import validate, is_public_url

ROOT = Path(__file__).resolve().parents[1]

class ValidationTests(unittest.TestCase):
    def test_seed_data(self):
        self.assertEqual(validate(ROOT / 'data'), [])

    def test_url_rules(self):
        self.assertTrue(is_public_url('https://example.com/page'))
        self.assertFalse(is_public_url('http://localhost/private'))
        self.assertFalse(is_public_url('file:///etc/passwd'))

if __name__ == '__main__':
    unittest.main()
