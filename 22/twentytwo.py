print("Welcome to Day 22. The end is nearer! :)")

from collections import defaultdict
import numpy as np
import os
import heapq

import time


def load_input(input_file):
    numbers = []
    with open(input_file, 'r') as f:
        numbers = [int(s.strip()) for s in  f.readlines()]
        
    return numbers

def next_secret(n):
    bitmask = (1 << 24) - 1 # 2^24 - 1


    n2 = n << 6 # shift left 6 bits == multiply by 64
    n = n ^ n2  # bitwise XOR (mix)
    n = n & bitmask # mod 2^24 (prune)
    n2 = n >> 5 # shift right 5 bits == divide by 32
    n = n ^ n2  # bitwise XOR (mix)
    n = n & bitmask # mod 2^24 (prune)
    n2 = n << 11 # shift left 11 bits == multiply by 2048
    n = n ^ n2  # bitwise XOR (mix)
    n = n & bitmask # mod 2^24 (prune)

    return n

def do2(numbers):
    result = 0


    diffs = []
    globalpatterns = dict()

    i = 0
    for n in numbers:

        diffs.append([])
        diffs[i].append(np.nan)

        currentpatterns = dict()

        for j in range(2000):
            nx = next_secret(n)
            diffs[i].append(nx % 10 - n % 10)

            # once we have a sequence of 4 diffs, we can start storing the prices
            if j >= 3:
                # encode the diffs into a 8-digit number, and store the price for this sequence
                # add 20 to each diff so that it becomes a unique 8-digit number
                # so -1 0 6 -4 becomes 19 20 26 16 => 19202616
                # (adding 10 would have cause negative ones to be one-digit numbers)
                pattern = (diffs[i][j-2]+20)*1000000 + (diffs[i][j-1]+20)*10000 + (diffs[i][j]+20)*100 + (diffs[i][j+1]+20)

                if pattern not in currentpatterns:
                    currentpatterns[pattern] = nx % 10

            n = nx
        
        # now we have the prices for the first pattern encounters 
        # add/increase the prices in the global patterns dictionary
        for pattern, price in currentpatterns.items():
            if pattern not in globalpatterns:
                globalpatterns[pattern] = price
            else:
                globalpatterns[pattern] += price

        i += 1
        result += n

    # now we have all the patterns, look for the largest price
    maxprice = max( globalpatterns.values() )
    
    return maxprice


def do1(numbers):
    result = 0
    
    for n in numbers:
        for c in range(2000):
            n = next_secret(n)
        
        result += n

    return result

        
# this year I won't figure out how to look for local file in VS Code :)
input_file = r'd:\OneDrive\Documents\Projects\AoC\2024\advent-of-code-2024\22\input.txt'   

numbers = load_input(input_file)

# t1 = time.time()
# result = do1(numbers)
# print(f"Result: {result}")
# t2 = time.time()
# print(f"elapsed time: {(t2-t1)} seconds")

t1 = time.time()
result2 = do2(numbers)
print(f"result: {result2}")
t2 = time.time()
print(f"elapsed time: {(t2-t1)} seconds")