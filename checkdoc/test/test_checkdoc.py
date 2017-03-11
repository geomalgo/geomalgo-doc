import unittest
from pathlib import Path
from collections import OrderedDict

import checkdoc as ck

HERE = Path(__file__).resolve().parent


class TestCdefFunctions(unittest.TestCase):

    def setUp(self):
        pxd = HERE / 'data' / 'simple.pxd'
        with pxd.open() as f:
            self.lines = f.readlines()

    def check_signature(self, line_number, expected_start, expected_end):
        start, end = ck.locate_cdef_signature(self.lines, line_number)
        self.assertEqual(start, expected_start)
        self.assertEqual(end, expected_end)

    def test_functions(self):
        line_numbers = ck.locate_cdef_functions(self.lines)
        self.assertEqual(line_numbers, [15, 18, 21, 30, 32, 35])

    def test_signatures(self):
        self.check_signature(15, (15, 19), (15, 19))
        self.check_signature(18, (18, 18), (18, 27))
        self.check_signature(21, (21, 27), (21, 50))
        self.check_signature(30, (30, 21), (30, 60))
        self.check_signature(32, (32, 31), (33, 55))
        self.check_signature(35, (35, 35), (35, 51))

if __name__ == '__main__':
    unittest.main()
