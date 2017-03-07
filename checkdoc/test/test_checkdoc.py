import unittest
from pathlib import Path

from checkdoc import search_cdef_functions

HERE = Path(__file__).resolve().parent


class TestExtractCdefFunctions(unittest.TestCase):

    def test_simple(self):
        pxd = HERE / 'data' / 'simple.pxd'
        with pxd.open() as f:
            lines = f.readlines()

        line_numbers = search_cdef_functions(lines)

        self.assertEqual(line_numbers, [15, 18, 21, 30, 32, 35, 39])

if __name__ == '__main__':
    unittest.main()
