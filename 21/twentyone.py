print("Welcome to Day 21. The end is near! :)")

from collections import defaultdict
import numpy as np
import os
import heapq

import time


def load_input(input_file):
    codes = []
    with open(input_file, 'r') as f:
        codes = [s.strip() for s in  f.readlines()]
        
    return codes

class p:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

def get_numpad_movements(c, finish):

    buttons = dict([('7', (0,0)), ('8', (0,1)), ('9', (0,2)), ('4', (1,0)), ('5', (1,1)), ('6', (1,2)), ('1', (2,0)), ('2', (2,1)), ('3', (2,2)), ('0', (3,1)), ('A', (3,2))])
    nuke_button = (3, 0)

    start_coord = buttons[c]
    target_coord = buttons[finish]

    result = ""

    # to avoid nuke button
    # when moving down, always start with horizontal movement
    if start_coord[0] < target_coord[0]:
        if start_coord[1] < target_coord[1]:
            result = ">" * (target_coord[1] - start_coord[1])
        else:
            result = "<" * (start_coord[1] - target_coord[1])
        result += "v" * (target_coord[0] - start_coord[0])
    # and otherwise (when moving up or stay in line), always start with vertical movement 
    else:
        result = "^" * (start_coord[0] - target_coord[0])
        if start_coord[1] < target_coord[1]:
            result += ">" * (target_coord[1] - start_coord[1])
        else:
            result += "<" * (start_coord[1] - target_coord[1])

    result += 'A'

    print(f"movinf from {c} to {finish}: {result}")

    return result, 'A'

def get_dirpad_movements(c, finish):

    buttons = dict([('^', (0,1)), ('A', (0,2)), ('<', (1,0)), ('v', (1,1)), ('>', (1,2))])
    nuke_button = (0, 0)

    start_coord = buttons[c]
    target_coord = buttons[finish]

    result = ""

    # to avoid nuke button - 
    # when moving down, always start with vertical movement
    if start_coord[0] < target_coord[0]:
        result = "v" * (target_coord[0] - start_coord[0])
        if start_coord[1] < target_coord[1]:
            result += ">" * (target_coord[1] - start_coord[1])
        else:
            result += "<" * (start_coord[1] - target_coord[1])
    # and otherwise (when moving up or stay in line), always start with horizontal movement 
    else:
        if start_coord[1] < target_coord[1]:
            result = ">" * (target_coord[1] - start_coord[1])
        else:
            result = "<" * (start_coord[1] - target_coord[1])
        result += "^" * (start_coord[0] - target_coord[0])

    result += 'A'

    print(f"movinf from {c} to {finish}: {result}")

    return result, 'A'

def do1(codes):
    result = 0

    start = 'A'
    start2 = 'A'
    start3 = 'A'

    for code in codes:
        path = ""
        path2 = ""
        path3 = ""
        print(f"procesing code: {code}")
        for c in code:
            p, finish = get_numpad_movements(start, c)
            path += p
            start = c
        
        # we got movements for numpad, now this needs to be pressed on dirpad 1
        print(f"  procesing code: {path}")
        for c in path:
            p, finish = get_dirpad_movements(start2, c)
            path2 += p
            start2 = c

        # we got movements for numpad, now this needs to be pressed on dirpad 2
        print(f"    procesing code: {path2}")
        for c in path2:
            p, finish = get_dirpad_movements(start3, c)
            path3 += p
            start3 = c

        result += len(path3) * int(code.strip('A'))

    return result



def do2(codes):
    result = 0
    

    return result

        
# this year I won't figure out how to look for local file in VS Code :)
input_file = r'd:\OneDrive\Documents\Projects\AoC\2024\advent-of-code-2024\21\sample.txt'   

codes = load_input(input_file)

t1 = time.time()
result = do1(codes)
# 214358 - too high :(
print(f"Result: {result}")
t2 = time.time()
print(f"elapsed time: {(t2-t1)} seconds")

# t1 = time.time()
# result2 = do2(map, start, end)
# print(f"result: {result2}")
# t2 = time.time()
# print(f"elapsed time: {(t2-t1)} seconds")