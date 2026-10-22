import unittest
from paramphantom.extractor import JSExtractor
from paramphantom.config import PhantomConfig

class TestParamPhantom(unittest.TestCase):
    def test_js_key_extraction(self):
        sample_code = "const user = { username: 'test', is_admin: false, role_id: 1 };"
        keys = JSExtractor.extract_keys_from_code(sample_code)
        self.assertIn("username", keys)
        self.assertIn("is_admin", keys)

    def test_config_initialization(self):
        config = PhantomConfig(target_url="https://api.example.com/update", custom_params=["is_admin"])
        self.assertEqual(config.target_url, "https://api.example.com/update")
        self.assertIn("is_admin", config.custom_params)

if __name__ == "__main__":
    main()
