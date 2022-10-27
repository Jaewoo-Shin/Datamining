#!/bin/python3
import sys
import math

curr_key, curr_state, min_value = None, [], math.inf

def _write(key, value):
    sys.stdout.write(f"{key}\t{value}\n")

def _reduce(key, value):
    global curr_key, curr_state, min_value
    if key != curr_key:
        if curr_key is not None:
            curr_state[0] = str(min_value)
            _write(curr_key, "\t".join(curr_state)) # print the calculated new new_label and data of new_label and connected nodes the data seems like this (curr_node, new new_label, new_label, connected nodes)
        curr_state = [] # curr_key gets the data for each key is connected to and new_label
        curr_key = key
        min_value = math.inf # to change min_value comparing with new_node make it infinite which becomes the new new_label
    if value is not None:
        if value[0] == "Yeep":
            curr_state = value # when value[0] is "Yeep" get the data ("Yeep", new_label, connected nodes)
        if int(value[1]) < min_value:
            min_value = int(value[1]) # when value[0] is "Nope" compare the new_label and min_value and make the min_value the smallest of new_labels

for line in sys.stdin:
    tokens = line.strip().split("\t")
    _reduce(tokens[0], tokens[1:])
_reduce(None, None)
