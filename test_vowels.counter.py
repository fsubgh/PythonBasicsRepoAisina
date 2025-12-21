import unittest
from vowels_counter import count_vowels


class TestCountVowels(unittest.TestCase):

    def test_simple_string(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("world"), 1)
        self.assertEqual(count_vowels("python"), 1)

    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("bcdfg"), 0)
        self.assertEqual(count_vowels("xyz"), 0)
        self.assertEqual(count_vowels("123"), 0)
        self.assertEqual(count_vowels("!@#$%"), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)
