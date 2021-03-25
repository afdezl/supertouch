#!/usr/bin/env python3

import os


def supertouch(path: str) -> str:
    """Creates paths and touches files.
    :param path: Path to create, including file, if any. To create a directory only, end the path with a '/'.
    :return:
    """
    file, *dirs = (None, path) if path.endswith("/") else path.split("/")[::-1]
    dir_path = "/".join(dirs[::-1])
    if dirs:
        try:
            os.makedirs(dir_path)
        except FileExistsError:
            pass
    if file:
        # File exists, abort creation
        if os.path.isfile(path):
            return path
        f = open(path, 'w')
        f.close()
    return path
