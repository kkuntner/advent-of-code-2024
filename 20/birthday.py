print("Welcome to Day 20. Happy Birthday Krisztian :)")

from collections import defaultdict
import numpy as np
import os
import heapq

import time

START = -2
END = -3
WALL = -1

def load_input(input_file, size):

    map = np.zeros((size, size), dtype=int)
    start = (0, 0)    
    end = (0, 0)

    with open(input_file, 'r') as f:
        y = 0
        for line in f:
            x = 0
            for c in line:
                if c == '#':
                    map[y][x] = WALL
                elif c == '.':
                    map[y][x] = 0
                elif c == 'S':
                    map[y][x] = START
                    start = (x, y)
                elif c == 'E':
                    map[y][x] = END
                    end = (x, y)
                x += 1
            y += 1

    return map, start, end

def calc_times(map, start, end):
    cx = start[0]
    cy = start[1]
    t = 0

    while True: #not END in [map[cy][cx+1], map[cy][cx-1],map[cy+1][cx],map[cy-1][cx]]:
        t += 1
        if map[cy][cx+1] == 0:
            map[cy][cx+1] = t
            cx += 1
        elif map[cy][cx-1] == 0:
            map[cy][cx-1] = t
            cx -= 1
        elif map[cy+1][cx] == 0:
            map[cy+1][cx] = t
            cy += 1
        elif map[cy-1][cx] == 0:
            map[cy-1][cx] = t
            cy -= 1
        elif map[cy][cx+1] == END:
            map[cy][cx+1] = t
            break
        elif map[cy][cx-1] == END:
            map[cy][cx-1] = t
            break
        elif map[cy+1][cx] == END:
            map[cy+1][cx] = t
            break
        elif map[cy-1][cx] == END:
            map[cy-1][cx] = t
            break

    map[start[1]][start[0]] = 0


def check_cheats(map, x, y):
    c = map[y][x]
    if c < 0:
        return []
    
    size = len(map[0])
    cheats = []
    #UP
    if (y > 1 and map[y-2][x] > c+2):
        # cheat contains x1, y1, x2, y2, save
        cheats.append((y-1, x, y-2, x, map[y-2][x]-c-2))
    #DOWN
    if (y < size-2 and map[y+2][x] > c+2):
        cheats.append((y+1, x, y+2, x, map[y+2][x]-c-2))
    #LEFT
    if (x > 1 and map[y][x-2] > c+2):
        cheats.append((y, x-1, y, x-2, map[y][x-2]-c-2))
    #RIGHT
    if (x < size-2 and map[y][x+2] > c+2):
        cheats.append((y, x+1, y, x+2, map[y][x+2]-c-2))
    return cheats

def check_cheats_many(map, x, y, allowed):
    current = map[y][x]
    if current < 0:
        return []
    
    size = len(map[0])
    cheats = []

    for cy in range(y-allowed-1, y+allowed+1):
        for cx in range(x-allowed-1, x+allowed+1):
            if cy < 0 or cy >= size or cx < 0 or cx >= size:
                continue

            dist = abs(cy-y) + abs(cx-x)
            if dist > allowed:
                continue
            reached = map[cy][cx]

            if reached != -1 and reached-current-dist > 0:
                cheats.append((cy, cx, y, x, reached-current-dist))
    return cheats
    
def do1(map, start, end):
    result = 0
    
    calc_times(map, start, end)

    cheats = []

    for y in range(1, len(map)-1):
        for x in range(1, len(map[0])-1):
            c = check_cheats(map, x, y)
            if len(c) > 0:
                cheats += c

    counts = dict()
    # count cheats where save is at least 100
    for c in cheats:
        if counts.get(c[4]) == None:
            counts[c[4]] = [c]
        else:
            counts[c[4]].append(c)
        if c[4] >= 100:
            result += 1
        

    return result



def do2(map, start, end):
    result = 0
    
    calc_times(map, start, end)

    cheats = []

    for y in range(1, len(map)-1):
        for x in range(1, len(map[0])-1):
            c = check_cheats_many(map, x, y, 20)
            if len(c) > 0:
                cheats += c

    counts = dict()
    counts2 = dict()

    # count cheats where save is at least 100
    for c in cheats:
        if c[4] >= 100:
            if counts.get(c[4]) == None:
                counts[c[4]] = [c]
                counts2[c[4]] = 1
            else:
                counts[c[4]].append(c)
                counts2[c[4]] += 1

        if c[4] >= 100:
            result += 1
        
    # 1 107 951 - too high :(
    # 1 000 000 - too high as well :(
    # 982425

    return result

        
# this year I won't figure out how to look for local file in VS Code :)
input_file = r'd:\OneDrive\Documents\Projects\AoC\2024\advent-of-code-2024\20\input.txt'   

map, start, end = load_input(input_file, 141)
# map, start, end = load_input(input_file, 15)

# t1 = time.time()
# result = do1(map, start, end)
# print(f"Result: {result}")
# t2 = time.time()
# print(f"elapsed time: {(t2-t1)} seconds")

t1 = time.time()
result2 = do2(map, start, end)
print(f"result: {result2}")
t2 = time.time()
print(f"elapsed time: {(t2-t1)} seconds")