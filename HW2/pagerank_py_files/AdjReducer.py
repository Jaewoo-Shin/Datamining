#!/bin/python3
import sys

curr_key, curr_state = None, []

def _write(key, value):
    sys.stdout.write(f"{key}\t{value}\n")

def _reduce(key, value):
    global curr_key, curr_state
    if key != curr_key:
        if curr_key is not None:
            _write(curr_key, "\t".join(["0.0", "0.0", "#" if len(curr_state) == 0 else ",".join(curr_state)])) # print when key_balue chaneges which print all inpurts for each inputs
        curr_key = key
        curr_state = []
    if value[0] != "#": curr_state.append(value[0])

for line in sys.stdin:
    tokens = line.strip().split("\t")
    _reduce(tokens[0], tokens[1:])
_reduce(None, ["#"])
