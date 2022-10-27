#!/bin/python3
import sys
import os

num_nodes = int(os.environ["pagerank_num_nodes"])
sum_scores =  float(os.environ["pagerank_sum_scores"])

def _write(key, value):
    sys.stdout.write(f"{key}\t{value}\n")

def _map(key, value):
    value[0] = str(float(value[0]) + (1 - sum_scores) / num_nodes) # calculate the rank after teleport
    _write(key, "\t".join(value))                                  # print the data with the changed rank

for line in sys.stdin:
    tokens = line.strip().split("\t")
    # key, value = tokens[0], tokens[1:]
    _map(tokens[0], tokens[1:])
