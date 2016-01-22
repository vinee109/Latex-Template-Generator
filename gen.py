"""
Runner script that initiates the program.
"""
__author__ = "Vineet Jain"

import argparse
import ttg.config
import ttg.populate
import util


def gen_template(template_file, output_file, config_file):
    config = ttg.config.TTGConfiguration(config_file)
    populator = ttg.populate.TTGPopulator(template_file, config)
    contents = populator.populate()
    util.write_file(contents, output_file)


def do_command(args):
    gen_template(args.source, args.output, args.config)


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