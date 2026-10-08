import os
import unittest
from unittest.mock import patch

from config import get_api_key, get_request_timeout


class TestConfiguration(unittest.TestCase):
    def test_api_key_can_be_injected_from_environment(self):
        with patch.dict(os.environ, {"MEDILINK_API_KEY": "ci-demo-secret"}, clear=False):
            self.assertEqual(get_api_key(), "ci-demo-secret")

    def test_timeout_has_safe_default(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(get_request_timeout(), 5)

    def test_invalid_timeout_is_rejected(self):
        with patch.dict(os.environ, {"REQUEST_TIMEOUT": "fast"}, clear=False):
            with self.assertRaisesRegex(ValueError, "integer"):
                get_request_timeout()


if __name__ == "__main__":
    unittest.main()
