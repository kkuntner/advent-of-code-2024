print("Welcome to Day 21. The end is near! :)")

from collections import defaultdict
import numpy as np
import os
import heapq
import itertools

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

    print(f"moving from {c} to {finish}: {result}")

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

    print(f"moving from {c} to {finish}: {result}")

    return result, 'A'


def get_path_permutations(path):
    res = path[0:-1]
    permutations = list(itertools.permutations(res))
    # remove duplicates from list
    permutations = list(set(permutations))
    #add A to the end of each permutation
    result = ["".join(p) + 'A' for p in permutations]
    return result

# return the list of safe paths from the current position, which avoid the nuke button
def get_safe_paths_from(paths, start):
    buttons = dict([('7', (0,0)), ('8', (0,1)), ('9', (0,2)), ('4', (1,0)), ('5', (1,1)), ('6', (1,2)), ('1', (2,0)), ('2', (2,1)), ('3', (2,2)), ('0', (3,1)), ('A', (3,2))])
    nuke_button = (3, 0)

    start_coord = buttons[start]

    result = []

    for path in paths:
        curr = start_coord
        for c in path:
            if c == "<":
                curr = (curr[0], curr[1]-1)
            elif c == ">":
                curr = (curr[0], curr[1]+1)
            elif c == "^":
                curr = (curr[0]-1, curr[1]) 
            elif c == "v":
                curr = (curr[0]+1, curr[1])
            if curr == nuke_button:
                break
        if curr != nuke_button:
            result.append(path)

    return result

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
        # go through each numpad key to be pressed
        for c in code:
            # see how we need to move on the numpad 
            p, finish = get_numpad_movements(start, c)

            # get all path permutations - we need to find the ones with the shortest subsequent pad presses
            perm = get_path_permutations(p)
            print(f"  permutations: {perm}")

            # filter out the ones that would press the nuke button
            perm = get_safe_paths_from(perm, start)

            start = c
            shortest_p2 = ""
            shortest_p3 = ""
            shortest_perm = ""

            # now go through all permutations, and find which can be assembled with the shortest path
            for possible_path in perm:

                currentpath2 = ""
                currentpath3 = ""

                # we got movements for numpad, now this needs to be pressed on dirpad 1
                print(f"  procesing perm: {possible_path}")
                for c2 in possible_path:
                    p, finish = get_dirpad_movements(start2, c2)
                    currentpath2 += p
                    start2 = c2

                # we got movements for numpad, now this needs to be pressed on dirpad 2
                print(f"    procesing code: {path2}")
                for c3 in currentpath2:
                    p, finish = get_dirpad_movements(start3, c3)
                    currentpath3 += p
                    start3 = c3

                if shortest_p2 == "" or len(currentpath2) < len(shortest_p2):
                    shortest_p2 = currentpath2

                if shortest_p3 == "" or len(currentpath3) < len(shortest_p3):
                    shortest_p3 = currentpath3
                    shortest_perm = possible_path
            
            path += shortest_perm
            path2 += shortest_p2
            path3 += shortest_p3        
        
        print(f"  path3: {len(path3)}: {path3}")
        result += len(path3) * int(code.strip('A'))

    return result



def do2(codes):
    result = 0
    

    return result

        
# this year I won't figure out how to look for local file in VS Code :)
input_file = r'd:\OneDrive\Documents\Projects\AoC\2024\advent-of-code-2024\21\input.txt'   

codes = load_input(input_file)

t1 = time.time()
result = do1(codes)
# 214358 - too high :( there must be a shorter sequence somewhere. yes, in the sample 379A, my result is 68, the description says 64
# 200410 - too low :( now as I saw sample 3 and 4 are shorter than in the task description... because of the nuke button!
# 206798 - perfect :)

print(f"Result: {result}")
t2 = time.time()
print(f"elapsed time: {(t2-t1)} seconds")

t1 = time.time()
result2 = do2(codes)
print(f"result: {result2}")
t2 = time.time()
print(f"elapsed time: {(t2-t1)} seconds")