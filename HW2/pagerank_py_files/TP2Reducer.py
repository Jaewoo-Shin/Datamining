#!/bin/python3
import sys

def _write(key, value):
    sys.stdout.write(f"{key}\t{value}\n")

def _reduce(key, value):
    if key is not None:
        _write(key, "\t".join(value)) # print the data same as TP2Reducer.py
 
for line in sys.stdin:
    tokens = line.strip().split("\t")
    _reduce(tokens[0], tokens[1:])
_reduce(None, None)
