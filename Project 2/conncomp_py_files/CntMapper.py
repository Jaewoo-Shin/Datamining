#!/bin/python3
import sys

def _write(key, value):
    sys.stdout.write(f"{key}\t{value}\n")

def _map(key, value):
    _write(value[0], key) # change the place of key and value[0] which becomes (new_node, curr_node) same new_node means there are connected

for line in sys.stdin:
    tokens = line.strip().split("\t")
    # key, value = tokens[0], tokens[1:]
    _map(tokens[0], tokens[1:])

