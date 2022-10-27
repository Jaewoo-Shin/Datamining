#!/bin/python3
import sys

sum_all = 0
def _write(key, value):
    sys.stdout.write(f"{key}\t{value}\n")

def _reduce(key, value):
    global sum_all
    sum_all += int(value) # sum up all the differences

for line in sys.stdin:
    tokens = line.strip().split("\t")
    _reduce(tokens[0], tokens[1])

_write("DIFF", str(sum_all))
