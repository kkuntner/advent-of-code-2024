print("Welcome to Day 18!")

from collections import defaultdict
import numpy as np
import os
import heapq

import time


LEFT_DIR = (-1, 0)
RIGHT_DIR = (1, 0)
UP_DIR = (0, -1)
DOWN_DIR = (0, 1)

def load_bytes(input_file):

    bytes = []

    with open(input_file, 'r') as f:
        for line in f:
            bytes.append([int(x) for x in line.strip().split(",")])
    
    return bytes


def print_mem(mem):
    for i in range(0, len(mem)):
        print(str.join([str(s) for s in mem[i]], ""))
        
# simulate the fall of bcount bytes starting at bstart
def fall_bytes(mem, bytes, bstart, bcount):
    for i in range(0, bcount):
        mem[bytes[bstart+i][1]][bytes[bstart+i][0]] = 1

def do1(bytes, memsize):
    result = 0

    mem = np.zeros((memsize, memsize), dtype=int)
    fall_bytes(mem, bytes, 0, 1024)

    sx = 0
    sy = 0
    fx = memsize-1
    fy = memsize-1
    
    #now find the shortest path in mem, from startpos to endpos

    step = 0

    dirs = [RIGHT_DIR, DOWN_DIR, LEFT_DIR, UP_DIR]
    visited = set()

    queue = [] # A* queue
    heapq.heappush(queue, (0, sx, sy))

    while queue:
        cost, x, y = heapq.heappop(queue)
        step += 1
        if step % 10 == 0:
            print(f"step {step}")
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if x == fx and y == fy:
            return cost
        
        # check all neighbors
        for i, (dx, dy) in enumerate(dirs):
            
            newx, newy = x + dx, y + dy

            # check if withon bounds and if not a wall
            if 0 <= newx < memsize and 0 <= newy < memsize and mem[newy][newx] == 0:
                newcost = cost + 1
                heapq.heappush(queue, (newcost, newx, newy))

    return -1

def find_exit(mem, memsize, sx, sy, fx, fy):
    step = 0

    dirs = [RIGHT_DIR, DOWN_DIR, LEFT_DIR, UP_DIR]
    visited = set()

    queue = [] # A* queue
    heapq.heappush(queue, (0, sx, sy))

    while queue:
        cost, x, y = heapq.heappop(queue)
        step += 1
        # if step % 100 == 0:
        #     print(f"step {step}")
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if x == fx and y == fy:
            return cost
        
        # check all neighbors
        for i, (dx, dy) in enumerate(dirs):
            
            newx, newy = x + dx, y + dy

            # check if withon bounds and if not a wall
            if 0 <= newx < memsize and 0 <= newy < memsize and mem[newy][newx] == 0:
                newcost = cost + 1
                heapq.heappush(queue, (newcost, newx, newy))

    return -1

def do2(bytes, memsize):
    result = 0

    mem = np.zeros((memsize, memsize), dtype=int)
    
    i = 0
    while True:          
        cbyte = bytes[i]
        print(f"trying byte {i} - {cbyte}")
        fall_bytes(mem, bytes, i, 1)

        sx = 0
        sy = 0
        fx = memsize-1
        fy = memsize-1
        
        if (find_exit(mem, memsize, sx, sy, fx, fy) == -1):
            return cbyte
        
        i += 1


        
# still have to figure out how to look for local file in VS Code :(
input_file = r'd:\OneDrive\Documents\Projects\AoC\2024\advent-of-code-2024\18\input.txt'   
mapsize = 71

bytes = load_bytes(input_file)

# t1 = time.time()
# result = do1(bytes, mapsize)
# print(f"Result: {result}")
# t2 = time.time()

# print(f"elapsed time: {(t2-t1)} seconds")

t1 = time.time()

result2 = do2(bytes, mapsize)
print(f"result: {result2}")


t2 = time.time()
#print(f"elapsed time: {(t2-t1)} seconds")