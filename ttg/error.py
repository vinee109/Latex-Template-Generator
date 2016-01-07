"""
error.py
"""
__author__ = "Vineet Jain"

class ConfigFileDoesNotExistException(Exception):
    def __init__(self, filename):
        self.message = "{} could not be found.".format(filename)


class MalformedConfigFileException(Exception):

    def __init__(self, filename):
        self.message = "{} contains malformed syntax as a configuration " \
                  "file".format(filename)