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


def print_dict(dictionary):
    """
    Prints dictionary in a readable way
    :param dictionary: the dictionary to be printed
    """
    def dict_str(dct, depth):
        """
        Recursively computes the string representation for a given dict
        :param dct: the dict of interest
        :param depth: the current depth we are at, this determines how many
        tabs we use
        :return: the string representation of the given dict
        :rtype: str
        """
        to_str = "{\n"
        tabs = "".join(["\t" for _ in range(depth+1)])
        for key, val in dct.items():
            if type(val) is dict:
                val_string = dict_str(val, depth+1)
            else:
                val_string = str(val)
            to_str += "{}{}: {}\n".format(tabs, key, val_string)
        return to_str + tabs[:-1] + "}"

    print dict_str(dictionary, 0)
