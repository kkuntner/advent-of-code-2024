print("Welcome to Day 24. Merry Christmas! :)")

from collections import defaultdict
import numpy as np
import os
import heapq
import networkx as nx

import time

class rule:
    input1 = ""
    input2 = ""
    op = ""
    output = ""

    def __init__(self, input1, input2, op, output):
        self.input1 = input1
        self.input2 = input2
        self.op = op
        self.output = output

    def __str__(self):
        return f"{self.input1} {self.op} {self.input2} -> {self.output}"

def load_input(input_file):

    inputs = dict()
    rules = []
    outputs = dict()

    with open(input_file, 'r') as f:
        # read line by line

        line = f.readline().strip()
        while line != "":
            inputs[line.split(':')[0]] = line.split(': ')[1]
            line = f.readline().strip()

        line = f.readline().strip()
        # x00 AND y00 -> z00
        while line != "":
            r = rule(line.split(' ')[0], line.split(' ')[2], line.split(' ')[1], line.split(' ')[4])
            rules.append(r)
            outputs[r.output] = r

            line = f.readline().strip()
            
    return inputs, rules, outputs

def apply_op(input1, input2, op):
    result = 0

    if op == 'AND':
        result = input1 & input2
    elif op == 'OR':
        result = input1 | input2
    elif op == 'XOR':
        result = input1 ^ input2

    return result

def get_value_for(wire, inputs, rules, outputs):
    # if this has already been calculated, return it 
    if wire in inputs:
        return int(inputs[wire])
    # otherwise, look for the rule defining this wire
    else:
        r = outputs[wire]
        
        val1 = get_value_for(r.input1, inputs, rules, outputs)
        val2 = get_value_for(r.input2, inputs, rules, outputs)
        result = apply_op(val1, val2, r.op)
        inputs[wire] = result
        return result    


def do1(inputs, rules, outputs):
    result = ""

    values = dict()

    # calculate all values of Zs
    # iterate through all outputs starting with 'z'
    for z in outputs:
        if z[0] == 'z':
            v = get_value_for(z, inputs, rules, outputs)
            values[int(z[1:])] = v
 
    # put values from values into a string, ordered by key
    for key in sorted(values.keys(), reverse=True):
        result += f"{values[key]}"

    # now convert the binary string to an integer
    result = int(result, 2)
    
    return result


def do2():
    result = "well. see notes.xlsx, where I built the addition based on the rules, and figured out which bits are incorrectly calculated... and found the solution."

    return result
        
# this year I won't figure out how to look for local file in VS Code :)
input_file = r'd:\OneDrive\Documents\Projects\AoC\2024\advent-of-code-2024\24\input.txt'   

inputs, rules, outputs = load_input(input_file)

t1 = time.time()
result = do1(inputs, rules, outputs)
print(f"Result: {result}")
t2 = time.time()
print(f"elapsed time: {(t2-t1)} seconds")

t1 = time.time()
result2 = do2()
print(f"result: {result2}")
t2 = time.time()
print(f"elapsed time: {(t2-t1)} seconds")