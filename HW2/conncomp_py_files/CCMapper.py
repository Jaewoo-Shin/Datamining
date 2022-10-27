#!/bin/python3
import sys

def _write(key, value):
    sys.stdout.write(f"{key}\t{value}\n")

def _map(key, value):
    value[1] = value[0] # move the new_label to old_label place
    value[0] = "Yeep" # for "Yeep" this data has the information which node is connected to
    _write(key, "\t".join(value)) # the data is semms like (curr_node, "Yeep", new_label, node connected)
    output = value[2].strip().split(",")
    for output_ele in output:
        value[0] = "Nope" #for "Nope" changes the plcae of node connected and curr_node one by one 
        _write(output_ele, "\t".join(value)) # the data seems like (one of connected node, "Nope", new_label, curr_node)


for line in sys.stdin:
    tokens = line.strip().split("\t")
    # key, value = tokens[0], tokens[1:]
    _map(tokens[0], tokens[1:])
