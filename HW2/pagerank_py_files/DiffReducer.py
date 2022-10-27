#!/bin/python3
import sys

curr_key, curr_state = None, 0.0

def _write(key, value):
    sys.stdout.write(f"{key}\t{value}\n")

def _reduce(key, value):
    global curr_key, curr_state
    if key != curr_key:
        if curr_key is not None:
            _write(curr_key, curr_state)
        curr_key = key
        curr_state = 0.0
    if value is not None: curr_state += float(value[0]) # sum all the differences

for line in sys.stdin:
    tokens = line.strip().split("\t")
    _reduce(tokens[0], tokens[1:])
_reduce(None, None)
