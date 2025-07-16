import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual((3), "Fizz")

if __name__ == "__main__":
    unittest.main()
