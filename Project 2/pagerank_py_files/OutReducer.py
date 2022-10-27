#!/bin/python3
import sys

all_list = []

def _write(key, value):
    sys.stdout.write(f"{key}\t{value}\n")

def _reduce(key, value):
    global all_list
    value_key = value, key #change the order of key and value
    all_list.append(value_key) # list appends all (value,key) tuples
        
   
for line in sys.stdin:
    tokens = line.strip().split("\t")
    _reduce(tokens[0], tokens[1])

all_list.sort(reverse=True) # line up the rank in large oreder

for element in all_list:
    if float(element[0]) >= 0.0005:
        _write(element[1], element[0]) # print the node and rank if the rank is bigger than 0.0005
    
