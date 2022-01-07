import unittest
from bys.urls import url_code

convert_to_alphanum_cases = [
    (0, 'a'),
    (3, 'd'),
    (35, '9'),
    (36, 'ba'),
    (73, 'cb'),
]


class UrlCodeTestCase(unittest.TestCase):
    def test_convert_to_alphanum(self):
        for num, expected in convert_to_alphanum_cases:
            with self.subTest():
                self.assertEqual(url_code._convert_to_alphanum(num), expected)
