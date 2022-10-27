#!/bin/python3
import sys

S, N= 0.0, 0
def _write(key, value):
    sys.stdout.write(f"{key}\t{value}\n")

def _reduce(key, value):
    global S, N
    
    S += float(value[0]) # calculate the sum of rank
    N = N+1              # calculate the number of nodes

for line in sys.stdin:
    tokens = line.strip().split("\t")
    _reduce(tokens[0], tokens[1:])
_write("N", str(N))
_write("S", str(S))
