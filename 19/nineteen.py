print("Welcome to Day 19!")

from collections import defaultdict
import numpy as np
import os
import heapq

import time

def load_input(input_file):

    towels = []
    designs = []

    with open(input_file, 'r') as f:
        towels = [t.strip() for t in f.readline().split(",")]
        f.readline()

        designs = [l.strip() for l in f.readlines()]

    return towels, designs

unassembleables = set()
assembleables = dict()

def look_for_possible_matches(design, towels, levels):
    global unassembleables
    max_len = max([len(t) for t in towels])

    if (len(design) < max_len):
        max_len = len(design)

    # YAY - this was the trick that made it work :)
    # if we've already determined that this design is unassembleable, we can skip it 
    # (and thus all its sub-designs!!!)
    if design in unassembleables:
        return False

    for i in range(max_len, 0, -1):
        # get all towels of length i that design starts with
        m = design[:i]
        possible_towel = m in towels
        if possible_towel:
            #print(f"{levels}")
            # if this was the complete design, we're done
            if len(m) == len(design):
                return True
            # possible match - look for the rest of the design
            if look_for_possible_matches(design[len(m):], towels, levels + str(i)):
                return True            
            else:
                unassembleables.add(design[len(m):])


def do1(towels, designs):
    result = 0
    count = 0
    global unassembleables

    for design in designs:
        count += 1
        print(f"design {count}")
        unassembleables.clear()
        if look_for_possible_matches(design, towels, ""):
            result += 1    

    return result


def look_for_all_matches(design, towels, levels):
    global unassembleables
    matchcount = 0
    max_len = max([len(t) for t in towels])

    if (len(design) < max_len):
        max_len = len(design)

    if design in unassembleables:
        return 0

    if design in assembleables:
        return assembleables[design]
    
    for i in range(max_len, 0, -1):
        # get all towels of length i that design starts with
        m = design[:i]
        possible_towel = m in towels
        
        if possible_towel:
            #print(f"{levels}")
            # if this was the complete design, we're done - but keep looking for more matches
            if len(m) == len(design):
                matchcount += 1
            else:
                # possible match - look for the rest of the design
                count = look_for_all_matches(design[len(m):], towels, levels + str(i))
                if count == 0:
                    unassembleables.add(design[len(m):])
                else:
                    assembleables[design[len(m):]] = count
                    matchcount += count
    return matchcount


def do2(towels, designs):
    result = 0
    count = 0
    global unassembleables

    for design in designs:
        count += 1
        print(f"design {count}")
        unassembleables.clear()
        assembleables.clear()
        r = look_for_all_matches(design, towels, "")
        print(f"r = {r}")
        result += r
        
    return result

    result = 0


        
# this year I will not  figure out how to look for local file in VS Code :)
input_file = r'd:\OneDrive\Documents\Projects\AoC\2024\advent-of-code-2024\19\input.txt'   

towels, designs = load_input(input_file)

t1 = time.time()
result = do1(towels, designs)
print(f"Result: {result}")
t2 = time.time()
print(f"elapsed time: {(t2-t1)} seconds")

t1 = time.time()
result2 = do2(towels, designs)
print(f"result: {result2}")
t2 = time.time()
print(f"elapsed time: {(t2-t1)} seconds")