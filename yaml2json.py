#!/usr/bin/env python                                                                                                                                          

import argparse
import json
import yaml

def parse_arguments():
    """This method is used to parse arguments """
    parser = argparse.ArgumentParser(description='yaml to json converter')
    parser.add_argument('--input', '-i', required=True, help='input file')
    parser.add_argument('--output', '-o', required=True, help='output file')
    args = parser.parse_args()
    return args 

def main(args):
    with open(args.input) as input_file, open(args.output, "w") as output_file:
        data = yaml.load(input_file)
        json.dump(data, output_file, sort_keys=True, indent=4)
 
if __name__ == "__main__":
    PARSED_ARGS = parse_arguments()
    main(PARSED_ARGS)
