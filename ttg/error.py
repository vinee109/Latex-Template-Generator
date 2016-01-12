"""
error.py
"""
__author__ = "Vineet Jain"

class FileDoesNotExistException(Exception):
    def __init__(self, filename):
        self.message = "{} could not be found.".format(filename)


class MalformedConfigFileException(Exception):

    def __init__(self, filename):
        self.message = "{} contains malformed syntax as a configuration " \
                  "file".format(filename)


class MissingQuestionLayoutFile(Exception):

    def __init__(self, filename):
        self.message = "{} does not exist as a question layout file".format(filename)
