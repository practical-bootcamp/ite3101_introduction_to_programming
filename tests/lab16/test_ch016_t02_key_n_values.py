import unittest
from ..console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab16/ch016_t02_key_n_values.py")
        expect = {
            "Name": "Peter",
            "Age": 18,
            "BDFL": True
        }
        self.assertDictEqual(expect, temp_locals['my_dict'])
        expect_output = """dict_keys(['Name', 'Age', 'BDFL'])
dict_values(['Peter', 18, True])
"""
        self.assertEqual(expect_output, output)


if __name__ == '__main__':
    unittest.main()