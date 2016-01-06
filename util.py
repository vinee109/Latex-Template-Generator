"""
Utility functions
"""
__author__ = "Vineet Jain"


def read_file(filename):
    with open(filename, "rb") as f:
        contents = f.readlines()
    return [line.rstrip() for line in contents]
