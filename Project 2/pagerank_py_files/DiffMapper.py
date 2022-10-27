#!/bin/python3
import sys

def _write(key, value):
    sys.stdout.write(f"{key}\t{value}\n")

def _map(key, value):
    _write("DIFF", abs(float(value[0]) - float(value[1]))) # the difference of new_rank and old_rank

for line in sys.stdin:
    tokens = line.strip().split("\t")
    # key, value = tokens[0], tokens[1:]
    _map(tokens[0], tokens[1:])
