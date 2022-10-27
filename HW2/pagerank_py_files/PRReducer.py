#!/bin/python3
import sys
import os

curr_key, curr_state, curr_vect = None, 0, None
damping_factor = float(os.environ["pagerank_damping_factor"])

def _write(key, value):
    sys.stdout.write(f"{key}\t{value}\n")

def _reduce(key, value):
    global curr_key, curr_state, curr_vect
    if key!= "#": # if the key is # we don't need to calculate the rank for it
        if key != curr_key:
            if curr_key is not None and curr_vect is not None:
                curr_vect[0] = str(curr_state) # change the curr_vect[0] to new_rank
                _write(curr_key, "\t".join(curr_vect))
            curr_vect = [] #curr_vect is the vect which contains the information which node points to
            curr_key = key #curr_key is the key which we are thinking of
            curr_state = 0 #curr_state sums up the rank inputted which means new_rank
        if value is not None:
            if int(key) != int(value[0]):
                curr_state += float(value[1]) / float(value[2]) * damping_factor    
            if int(key) == int(value[0]):
                curr_vect = value
                

for line in sys.stdin:
    tokens = line.strip().split("\t")
    _reduce(tokens[0], tokens[1:])
_reduce(None, None)

