#!/usr/bin/env python3

import json
import numpy
import os
import sys


def process(fname):
    with open(f'{fname}.json') as _file:
        data = json.load(_file)
        print(data)

        return data


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: main.py <fname>")
        sys.exit(1)
    
    # Read Inputs
    # You can read your input to your action from args or
    # as env variables renamed as INPUT_<input_var_in_caps>
    print(f"Input: {sys.argv[1]} = {os.environ['INPUT_FNAME']}")


    fname = sys.argv[1]
    print(f"Argument `fname` received is ${fname}")

    user = process(fname)
    
    response = f"User {user.get('name')} is available at {user.get('website')}"

    # Set Outputs
    # print(f"::set-output name=response-text::{response}") # ::set-output is soon to be deprecated
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'response-text={response}', file=fh)
