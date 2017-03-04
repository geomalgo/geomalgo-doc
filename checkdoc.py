#!/usr/bin/env python

import argparse
import glob
import pathlib


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
        raise OSError("geomalgo path: {} is wrong".format(geomalgo))


def read_pxd_files(geomalgo):
    return {fp.relative_to(geomalgo): fp.open().readlines()
            for fp in geomalgo.rglob('*.pxd')}


def extract_cdef_functions(pxd):
    vector2d = pathlib.Path('base2d/vector2d.pxd')
    print(pxd[vector2d])


def main():
    args = parse_command_line()
    geomalgo = find_geomalgo_root(args.geomalgo)
    pxd = read_pxd_files(geomalgo)
    extract_cdef_functions(pxd)


if __name__ == '__main__':
    main()
