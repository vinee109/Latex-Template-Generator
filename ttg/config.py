"""
config.py
"""
__author__ = "Vineet Jain"

import error
import json
import os
import util

# Constants pertaining to required fields
FIELDS = "fields"
QUESTIONS = "questions"

class TTGConfiguration:

    def __init__(self, filename, fields=None):
        if util.file_exists(filename):
            self.__parse_config(filename)
        else:
            raise error.FileDoesNotExistException(filename)

    def __parse_config(self, filename):
        """
        Parses a configuration specified at the given filename into the
        necessary fields. Assumes that the file already exists and is valid. If
        the syntax of the config file is not correct,
        a MalformedConfigFileException is raised.

        :param filename: the path to the configuration file of interest
        :raises: MalformedConfigFileException
        """
        self.current_dir = os.path.dirname(filename)
        str_contents = "\n".join(util.read_file(filename))
        try:
            contents = json.JSONDecoder().decode(str_contents)
            self.__validate_json_contents(contents)
        except ValueError:
            raise error.MalformedConfigFileException(filename)

    def __validate_json_contents(self, contents):
        """
        Validates the contents of the json file passed in as config. Ensures
        that there is a questions layout that is passed in.

        :param contents: the json contents to be validated
        """
        if FIELDS in contents:
            self._fields = contents[FIELDS]
        else:
            self._fields = None

        if QUESTIONS in contents or util.file_exists(contents[QUESTIONS]):
            self._question_layout_file = contents[QUESTIONS]
        else:
            raise error.MissingQuestionLayoutFile(contents[QUESTIONS])

    @property
    def question_layout_file(self):
        return self._question_layout_file

    @property
    def fields(self):
        return self._fields
