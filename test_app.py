import unittest
from app import soma

class TestSoma(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
