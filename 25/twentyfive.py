print("Welcome to Day 25. This is the end. It was fun :)")

from collections import defaultdict
import numpy as np
import os
import heapq
import networkx as nx

import time

def load_input(input_file):

    keys = []
    locks = []

    with open(input_file, 'r') as f:
       
        while True:
            something = [0,0,0,0,0]
            key = False

            # read 7 lines
            for i in range(7):
                line = f.readline().strip()
                if i == 0:
                    key = line[0] == '.'

                for j in range(5):
                    if line[j] == '#':
                        something[j] += 1

            for i in range(5):
                something[i] = something[i]-1

            if key:
                keys.append(something)
            else:
                locks.append(something)       

            if not f.readline():
                break

    return keys, locks

def fits(key, lock):
    for i in range(5):
        if key[i] + lock[i] > 5:
            return False
    return True


def do1(keys, locks):
    result = 0

    # check each key with each lock... why not?
    for key in keys:
        for lock in locks:
            if fits(key, lock):
                result += 1

    return result


def do2():
    result = ""

    return result
        
# this year I won't figure out how to look for local file in VS Code :)
input_file = r'd:\OneDrive\Documents\Projects\AoC\2024\advent-of-code-2024\25\input.txt'   

keys, locks = load_input(input_file)
print(f"We have {len(keys)} keys and {len(locks)} locks")

t1 = time.time()
result = do1(keys, locks)
print(f"Result: {result}")
t2 = time.time()
print(f"elapsed time: {(t2-t1)} seconds")

# t1 = time.time()
# result2 = do2(graph)
# print(f"result: {result2}")
# t2 = time.time()
# print(f"elapsed time: {(t2-t1)} seconds")