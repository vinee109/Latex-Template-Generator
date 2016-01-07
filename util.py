"""
Utility functions
"""
__author__ = "Vineet Jain"

import os


def read_file(filename):
    with open(filename, "rb") as f:
        contents = f.readlines()
    return [line.rstrip() for line in contents]


def file_exists(path):
    """
    Checks if the specified path actually exists as a file or not
    :param path: the path in question
    :return: True if the path is a file and it exists, False otherwise
    """
    if os.path.exists(path):
        return os.path.isfile(path)
    else:
        return False