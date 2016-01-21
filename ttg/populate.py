"""
populate.py
"""
__author__ = "Vineet Jain"

from config import QUESTIONS
import error
import os
import util


class TTGPopulator:

    def __init__(self, template_file, config):
        self.config = config
        self.__parse_template_file(template_file)
        self.__parse_question_layout()

    def __parse_template_file(self, template_file):
        """
        Parses the template file if it exists, this is just a helper method
        for error checking. If the file exists, the contents of the file is
        stored into an instance variable
        :param template_file: the path to the template file of interest
        """
        if util.file_exists(template_file):
            self.template_contents = util.read_file_str(template_file)
        else:
            raise error.FileDoesNotExistException(template_file)

    def __parse_question_layout(self):
        qlf_path = os.path.join(
            self.config.current_dir,
            self.config.question_layout_file)
        ques_struct = util.read_file(qlf_path)
        self.qtree = QuestionTree(ques_struct)


    def populate(self, with_questions=True):
        """
        Actually populates the template with the values from the config and
        the question structure.
        :param with_questions: if we are populating questions, for example
        for a homework template
        :return: A new string identical to the template contents but with all
        necessary information populated
        """
        populated_contents = self.template_contents
        for field, value in self.config.fields.items():
            if field != QUESTIONS:
                pattern = "<<{}>>".format(field)
                populated_contents = populated_contents.replace(pattern, value)
        if with_questions:
            body = self.qtree.to_latex()
            return populated_contents.replace("<<{}>>".format(QUESTIONS), body)
        else:
            return populated_contents


class QuestionTree:

    def __init__(self, questions):
        self.__construct(questions)


    def __construct(self, questions):
        self._root = Node()
        self.__construct_helper(questions)

    def __construct_helper(self, questions):
        stack = [(self._root, -1)]
        for question in questions:
            parent, parent_depth = stack[-1]
            q_text = question.lstrip()
            depth = len(question) - len(q_text)
            while len(stack) > 1 and depth != parent_depth + 1:
                stack.pop()
                parent, parent_depth = stack[-1]
            child = Node(val=q_text)
            parent.children.append(child)
            stack.append((child, depth))

    def to_latex(self):
        lines = []
        self.__to_latex_helper(self._root, -1, lines)
        return "\n".join(lines[1:])

    def __to_latex_helper(self, node, depth, lines):
        if len(node.children) == 0:
            return
        tabs = self.__tabs(depth)
        if depth >= 0:
            lines.append(tabs + "\\begin{enumerate}")
        for child in node.children:
            if depth >= 0:
                lines.append(tabs + "\t" + "\\item[{}]".format(child.value))
            else:
                lines.append("\\newpage")
                lines.append("")
                lines.append("\\section*{{{}}}".format(child.value))
            self.__to_latex_helper(child, depth+1, lines)
        if depth >= 0:
            lines.append(tabs + "\\end{enumerate}")

    def __tabs(self, num):
        return "".join(["\t" for _ in range(num)])

    def __repr__(self):
        return "".join(map(str, self._root.children))


class Node:
    def __init__(self, val=None):
        self.children = []
        self.value = val

    def __repr__(self):
        repr = str(self.value) + "\n"
        for child in self.children:
            for line in ["-" + s for s in str(child).split()]:
                repr += line + "\n"
        return repr
