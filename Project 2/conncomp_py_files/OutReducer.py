#!/bin/python3
import sys

max_count, num_count = 0, 0
def _write(key, value):
    sys.stdout.write(f"{key}\t{value}\n")

def _reduce(key, value):
    global max_count, num_count
    if max_count < int(value):
        max_count = int(value) # compare the max node of each connected graphs and get the maximum value
    num_count += int(key) # for all number of connected graphs sum up the graph counted
for line in sys.stdin:
    tokens = line.strip().split("\t")
    _reduce(tokens[0], tokens[1])

_write("COUNT", str(num_count)) # print the number of connected graph
_write("MAX", str(max_count))   # print the maximum node number of connected graph


