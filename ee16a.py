"""
Creates intial hw tex source with populated questions for EE16A homework
assignments
"""
__author__ = "Vineet Jain"

import argparse
import gen
from os.path import expanduser
import ttg.config

HOME = expanduser("~")
EE16A_DIR = HOME + "/Desktop/School/Spring-2016/EE16A/"
TEMPLATE = EE16A_DIR + "hw/template/template.tex"


def create_config(hw_num, qlayout):
    config_dict = {
        "fields": {
            "hw": hw_num
        },
        "questions": qlayout
    }
    return ttg.config.TTGConfiguration(json_fields=config_dict)


def do_command(args):
    hw_num = args.hw_num
    hw_dir = EE16A_DIR + "/hw/hw{}/".format(hw_num)
    hw_filename = hw_dir + "hw{}.tex".format(hw_num)

    # create the config file
    qlayout_filename = hw_dir + "hw{}.layout".format(hw_num)
    config = create_config(hw_num, qlayout_filename)
    config.current_dir = hw_dir

    # generate template
    gen.gen_template(TEMPLATE, hw_filename, config)


def parse_command():
    parser = argparse.ArgumentParser(description="HW Template Gen for EE16A")
    parser.add_argument("hw_num", type=int, help="(int) the homework number")
    return parser.parse_args()

if __name__ == "__main__":
    do_command(parse_command())
