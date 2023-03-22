#!/usr/bin/env python3

import pandas as pd
import numpy as np

import sys


def example(fname):

    users = {'Name': ['Person1', 'Person2', 'Person3'],
        'Age': [20,21,25]}
    
    df = pd.DataFrame(users, columns=['Name','Age'])
    
    df.to_csv(f'${fname}.csv', sep='\t', index=False,header=True)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: main.py <fname>")
        sys.exit(1)

    fname = sys.argv[1]
    print(f"fname is ${fname}")
    example(fname)