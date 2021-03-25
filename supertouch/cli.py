#!/usr/bin/env python3

import argparse
import sys
from supertouch import supertouch


def main() -> None:
    parser = argparse.ArgumentParser(description="Creates or touches paths and files.")
    parser.add_argument("path", type=str, nargs="+", help="Path(s) to create")
    args = parser.parse_args()

    for path in args.path:
        try:
            supertouch(path)
        except IsADirectoryError:
            # Conflict, directory exists with the same name as the file.
            sys.stdout.write("Directory already exists with the provided filename.\n")

