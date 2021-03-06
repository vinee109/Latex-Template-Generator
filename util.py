"""
Utility functions
"""
__author__ = "Vineet Jain"

import os


def read_file(filename):
    """
    Reads a specified file into a list of lines
    :param filename: the path to the file we want to read
    :return: a list of lines where the ith element in the list is the ith
    line in the file
    """
    with open(filename, "rb") as f:
        contents = f.readlines()
    return [line.rstrip() for line in contents]


def read_file_str(filename):
    """
    Reads a specified file into one large string
    :param filename: the path to the file we want to read
    :return: one string containing all the content of the file where each
    line is separated by a newline character
    """
    return "\n".join(read_file(filename))

def write_file(contents, filename):
    """
    Writes some content to a specified file
    :param contents: the contents to be written
    :param filename: the path of the file we want to write these contents to
    """
    with open(filename, "w") as f:
        f.write(contents)


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
    print dict_str(dictionary)


def dict_str(dictionary):
    """
    Generates a string containing a readable representation of the dictionary
    :param dictionary: the dictionary of interest
    :return: a readable string version of the dictionary
    """
    def __dict_str(dct, depth):
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
                val_string = __dict_str(val, depth+1)
            else:
                val_string = str(val)
            to_str += "{}{}: {}\n".format(tabs, key, val_string)
        return to_str + tabs[:-1] + "}"

    return __dict_str(dictionary, 0)
