"""
Runner script that initiates the program.
"""
__author__ = "Vineet Jain"


import argparse


def do_command(args):
    return

def parse_command():
    parser = argparse.ArgumentParser(description="Latex Template Generator")
    parser.add_argument("source", type=str, help="(str) the path to the file "
                                                 "that is to be populated")
    parser.add_argument("output", type=str, help="(str) the path where the "
                                                 "resulting populated latex "
                                                 "file will exist")
    return parser.parse_args()

# Parses flags passed in by the user and initiates the program. Exits on
# completion or if an error occurred.
if __name__ == "__main__":
    do_command(parse_command())