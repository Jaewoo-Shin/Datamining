#!/bin/python3
import sys

def _write(key, value):
    sys.stdout.write(f"{key}\t{value}\n")

def _map(key, value):
    _write(key, value[0]) # print output, input
    _write(value[0], "#") # ptiny input, #

for line in sys.stdin:
    tokens = line.strip().split("\t")
    # key, value = tokens[0], tokens[1:]
    _map(tokens[0], tokens[1:])
