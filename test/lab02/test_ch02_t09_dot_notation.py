import unittest
from test.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        result = get_script_output("lab02/ch02_t09_dot_notation.py")
        self.assertEqual("27\nTHE MINISTRY OF SILLY WALKS\n", result)


if __name__ == '__main__':
    unittest.main()
