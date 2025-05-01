import unittest
from app import app  # Ensure the correct object is being imported from app.py

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.data, b"Hello, World!")

if __name__ == '__main__':
    unittest.main()

