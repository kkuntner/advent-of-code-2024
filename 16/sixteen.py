print("Welcome to Day 16!")

from collections import defaultdict
import numpy as np
import os
import heapq

import time

WALL = "#"
START = "S"
FINISH = "E"
BLANK = "."

LEFT_DIR = (-1, 0)
RIGHT_DIR = (1, 0)
UP_DIR = (0, -1)
DOWN_DIR = (0, 1)


def load_map(input_file):
    map = []
    sx, sy, fx, fy = 0, 0, 0, 0

    with open(input_file, 'r') as f:
        line = f.readline().strip()
        y=0
        #read the map
        while line != "":
            x = 0
            row = []
            map.append(row)
            for c in line:
                if c == WALL:
                    row.append(1)
                elif c == BLANK:
                    row.append(0)
                elif c == START:
                    row.append(0)
                    sx = x
                    sy = y
                elif c == FINISH:
                    row.append(0)
                    fx = x
                    fy = y
                x+=1      
            y+=1
            line = f.readline().strip()

    return map, sx, sy, fx, fy

def do1(map, sx, sy, fx, fy):
    sizex = len(map[0])
    sizey = len(map)
    step = 0

    dirs = [RIGHT_DIR, DOWN_DIR, LEFT_DIR, UP_DIR]
    visited = set()

    queue = [] # A* queue
    heapq.heappush(queue, (0, sx, sy, RIGHT_DIR))

    while queue:
        cost, x, y, predvir = heapq.heappop(queue)
        step += 1
        if step % 100000 == 0:
            print(f"step {step}")
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if x == fx and y == fy:
            return cost
        
        # check all neighbors
        for i, (dx, dy) in enumerate(dirs):
            # skip if we are going backwards - no need to go back
            if predvir == (-dx, -dy):
                continue
            
            newx, newy = x + dx, y + dy

            # check if withon bounds and if not a wall
            if 0 <= newx < sizex and 0 <= newy < sizey and map[newy][newx] == 0:
                newcost = cost + 1
                if predvir != (dx, dy):
                    newcost += 1000
                heapq.heappush(queue, (newcost, newx, newy, (dx, dy)))

    return -1

def do2(map, sx, sy, fx, fy):
    sizex = len(map[0])
    sizey = len(map)

    dirs = [RIGHT_DIR, DOWN_DIR, LEFT_DIR, UP_DIR]
    visited = {}
    allmincostpaths = [] 
    mincost = 999999999999999
    step = 0
    queue = [] # A* queue
    heapq.heappush(queue, (0, sx, sy, RIGHT_DIR, [(sx, sy)]))


    while queue:
        cost, x, y, predvir, path = heapq.heappop(queue)
        #print(f"({x}, {y}) - {cost}, {predvir}")
        
        step += 1
        if step % 100000 == 0:
            count = len(set([item for sublist in allmincostpaths for item in sublist]))
            qs = len(queue)
            print(f"step {step}, mincost: {mincost}, count: {count}, queue: {qs}")

        if cost > mincost:
            continue

        # if we are at the end
        if x == fx and y == fy:
            if cost < mincost:
                mincost = cost
                allmincostpaths = [path]
            elif cost == mincost:
                allmincostpaths.append(path)
            continue
            
        
        # check all neighbors
        for i, (dx, dy) in enumerate(dirs):
            # skip if we are going backwards - no need to go back
            if predvir == (-dx, -dy):
                continue

            newx, newy = x + dx, y + dy

            # check if withon bounds and if not a wall
            if 0 <= newx < sizex and 0 <= newy < sizey and map[newy][newx] == 0:
                newcost = cost + 1
                if predvir != (dx, dy):
                    newcost += 1000
                heapq.heappush(queue, (newcost, newx, newy, (dx, dy), path + [(newx, newy)]))

    return mincost, allmincostpaths

def display_map(map):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    for row in map:
        print(''.join(row))
    print("\n")


def print_maze(maze, paths):
    
    map = []
    for row in maze:
        maprow = []
        map.append(maprow)
        for c in row:
            if c == 1:
                maprow.append("#")
            else:
                maprow.append(" ")

    for path in paths:
        for x, y in path:
            map[y][x] = "*"
    display_map(map)

        
# still have to figure out how to look for local file in VS Code :(
input_file = r'd:\OneDrive\Documents\Projects\AoC\2024\advent-of-code-2024\16\input.txt'   

map, sx, sy, fx, fy = load_map(input_file)

t1 = time.time()
total = do1(map, sx, sy, fx, fy)
print(f"Total cost: {total}")
t2 = time.time()

# print(f"elapsed time: {(t2-t1)} seconds")

t1 = time.time()
cost, paths = do2(map, sx, sy, fx, fy)

assert cost == total

# paths is a list of paths, each path is a list of coordinates
# union all paths, and count its length
count = len(set([item for sublist in paths for item in sublist]))

#print_maze(map, paths)
print(f"Total count: {count}")

t2 = time.time()

print(f"elapsed time: {(t2-t1)} seconds")