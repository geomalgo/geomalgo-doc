#!/usr/bin/env python

import argparse
import glob
import pathlib
from typing import List


def parse_command_line():
    """ Parse command line options and arguments """
    parser = argparse.ArgumentParser()

    parser.add_argument('geomalgo', type=pathlib.Path,
                        help='path to geomalgo package')

    args = parser.parse_args()

    return args


def find_geomalgo_root(geomalgo, testfile='base2d.pxd'):
    """
    geomalgo/
        geomalgo/       <- we want this directory
            base2d.pxd
            ...
        setup.py
        ...
    """
    if (geomalgo / testfile).exists():
        return geomalgo

    elif (geomalgo / 'geomalgo' / testfile).exists():
        return geomalgo / 'geomalgo'

    else:
        raise OSError(f'geomalgo path: {geomalgo} is wrong')


def read_pxd_files(geomalgo):
    return {fp.relative_to(geomalgo): fp.open().readlines()
            for fp in geomalgo.rglob('*.pxd')}


def locate_cdef_functions(lines: List[str]) -> List[int]:
    """First line number of all cdef functions

    Line numbers are counted from zero.

    Example
    -------

        >>> lines = [
        ...     'cdef void foo()',  # 0  <- first cdef function
        ...     '',                 # 1
        ...     'cdef struct A:',   # 2
        ...     '    double x',     # 3
        ...     '    double y',     # 4
        ...     '',                 # 5
        ...     '# comment',        # 6
        ...     'cdef void bar()',  # 7  <- second cdef function
        ... ]

        >>> locate_cdef_functions(lines)
        [0, 7]
    """
    line_numbers = []
    for i, line in enumerate(lines):
        # A line like '    cdef' is a method, not a function.
        if not line or line[0] == ' ':
            continue
        words = line.split()
        if len(words) < 2:
            continue
        if not words[0] == 'cdef':
            continue
        if words[1] in ('struct', 'class'):
            continue
        line_numbers.append(i)
    return line_numbers


class Signature:

    def __init__(self, lines: List[str], start, end):
        pass


def locate_cdef_signature(lines: List[str], line_number: int):
    count = 0
    for iline, line in enumerate(lines[line_number:]):
        for icol, char in enumerate(line):
            if char == '(':
                if count==0:
                    start = (line_number+iline, icol+1)
                count += 1
            elif char == ')':
                count -= 1
                if count==0:
                    end = (line_number+iline, icol)
                    return start, end


def main():
    args = parse_command_line()
    geomalgo = find_geomalgo_root(args.geomalgo)
    pxd = read_pxd_files(geomalgo)


if __name__ == '__main__':
    main()
