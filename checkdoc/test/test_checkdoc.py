import unittest
from pathlib import Path

from checkdoc import extract_cdef_functions

HERE = Path(__file__).resolve().parent


class TestExtractCdefFunctions(unittest.TestCase):

    def test_simple(self):
        pxd = HERE / 'data' / 'simple.pxd'
        with pxd.open() as f:
            lines = f.readlines()
        extract_cdef_functions(lines)


if __name__ == '__main__':
    unittest.main()
