import unittest
from app import get_message

class TestApp(unittest.TestCase):
    def test_message(self):
        self.assertEqual(get_message(), "Hello from the DevOps pipeline!")

if __name__ == "__main__":
    unittest.main()
