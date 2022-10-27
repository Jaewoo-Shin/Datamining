#!/bin/python3
import sys

def _write(key, value):
    sys.stdout.write(f"{key}\t{value}\n")

def _map(key, value):
    value[1] = value[0] # move the new_rank to old_rank place
    value[0] = key      # this data keeps the information of which node is pointed to 
    _write(key, "\t".join(value))
    output = value[2].strip().split(",")
    value[2] = str(len(output)) # calculate the size of pointed node for calculating rank at PRReducer.py
    for output_ele in output:
        if output_ele != "#":
            value[0] = str(int(output_ele)-1) # value[0] is used to disthnguish with the data with keeps the information which node poites to
        _write(output_ele, "\t".join(value))

for line in sys.stdin:
    tokens = line.strip().split("\t")
    # key, value = tokens[0], tokens[1:]
    _map(tokens[0], tokens[1:])
    
