#!/bin/python3
import sys

curr_key, curr_count, max_count, num_count = None, 0, 0, 0

def _write(key, value):
    sys.stdout.write(f"{key}\t{value}\n")

def _reduce(key, value):
    global max_count, curr_key, curr_count, num_count

    if key != curr_key:
        if curr_key is not None:
            if max_count < curr_count: #compare max_count and curr_count and if curr_count is bigger change max_Count as curr_count
                max_count = curr_count
            num_count += 1 # num_count is the number of connected grapth
        curr_key = key
        curr_count = 0 # curr_count is the number of nodes in connected graph
    if value is not None:
        curr_count += 1
    
for line in sys.stdin:
    tokens = line.strip().split("\t")
    _reduce(tokens[0], tokens[1])
_reduce(None, None)
_write(str(num_count), str(max_count))



