"""
Runner script that initiates the program.
"""
__author__ = "Vineet Jain"

import argparse
import ttg.config
import ttg.populate
import util


def gen_template(template_file, output_file, config):
    """
    Populates and generates a new template
    :param template_file: the initial template file
    :param output_file: the output file where the populated template will live
    :param config: the config object of type TTGConfiguration that will be used
    """
    populator = ttg.populate.TTGPopulator(template_file, config)
    contents = populator.populate()
    util.write_file(contents, output_file)


def do_command(args):
    config = ttg.config.TTGConfiguration(args.config)
    gen_template(args.source, args.output, config)


def parse_command():
    parser = argparse.ArgumentParser(description="Latex Template Generator")
    parser.add_argument("source", type=str, help="(str) the path to the file "
                                                 "that is to be populated")
    parser.add_argument("output", type=str, help="(str) the path where the "
                                                 "resulting populated latex "
                                                 "file will exist")
    parser.add_argument("config", type=str, help="(str) the path where the "
                                                 "config lies dictating how "
                                                 "the source is to be "
                                                 "populated")
    return parser.parse_args()

# Parses flags passed in by the user and initiates the program. Exits on
# completion or if an error occurred.
if __name__ == "__main__":
    do_command(parse_command())