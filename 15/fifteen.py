print("Welcome to Day 15!")

from collections import defaultdict
import numpy as np
import os

import time

BOX = "O"
WALL = "#"
ROBOT = "@"
BLANK = "."
BIGBOX = "[]"

LEFT = ">"
RIGHT = "<"
UP = "^"
DOWN = "v"

LEFT_DIR = (-1, 0)
RIGHT_DIR = (1, 0)
UP_DIR = (0, -1)
DOWN_DIR = (0, 1)

DIROFMOVE = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1)
}

def load_map(input_file):
    map = []
    movements = []
    rx = ry = 0

    with open(input_file, 'r') as f:
        line = f.readline().strip()
        y=0
        #read the map
        while line != "":
            x = 0
            row = []
            map.append(row)
            for c in line:
                row.append(c)
                if c == ROBOT:
                    rx = x
                    ry = y
                x+=1            
            y+=1
            line = f.readline().strip()

        #now read the movement        
        lines = f.readlines()
        for mline in lines:
            mline = mline.strip()
            for c in mline:
                movements.append(c)

    return map, movements, rx, ry

def move(map, movement, rx, ry):
    #look if there is a blank space in the direction of the movement
    dir = DIROFMOVE[movement]
    x = rx+dir[0]
    y = ry+dir[1]
    while map[y][x] != BLANK and map[y][x] != WALL:
        x += dir[0]
        y += dir[1]
        
    if map[y][x] == WALL:
        return rx, ry

    #move the robot and push boxes if needed
    while map[y][x] != ROBOT:
        map[y][x] = map[y-dir[1]][x-dir[0]]
        x -= dir[0]
        y -= dir[1]
    
    map[y][x] = BLANK
    return x + dir[0], y + dir[1]

def sum_boxes(map):
    total = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == BOX or map[y][x] == BIGBOX[0]:
                total += 100*y + x
    return total

def do1(map, movements, rx, ry):
    total = 0
    x = rx
    y = ry

    for m in movements:
        x, y = move(map, m, x, y)

    total = sum_boxes(map)

    print(f"total: {total}")

def display_map(map):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    for row in map:
        print(''.join(row))
    print("\n")



def transform_map(map):
    new_map = []
    for y in range(len(map)):
        row = []
        new_map.append(row)
        for x in range(len(map[y])):
            c = map[y][x]
            if c == BOX:
                row.append(BIGBOX[0])
                row.append(BIGBOX[1])
            elif c == ROBOT:
                row.append(ROBOT)
                row.append(BLANK)
            else:
                row.append(c)
                row.append(c)

    return new_map

def move2(map, movement, rx, ry):
    #look if there is a blank space in the direction of the movement
    dir = DIROFMOVE[movement]

    #left and right will be the same as before
    if (dir == LEFT_DIR) or (dir == RIGHT_DIR):
        x = rx+dir[0]
        y = ry+dir[1]
        while map[y][x] != BLANK and map[y][x] != WALL:
            x += dir[0]
            y += dir[1]
            
        if map[y][x] == WALL:
            return rx, ry

        #move the robot and push boxes if needed
        while map[y][x] != ROBOT:
            map[y][x] = map[y-dir[1]][x-dir[0]]
            x -= dir[0]
            y -= dir[1]

    #up and down will be different, as the boxes are wider
    else:
        x = rx
        y = ry
        currentrow = y
        can_move = True

        affected_boxes_to_check = []
        all_affected_boxes = []

        if dir == UP_DIR:
            if map[y-1][x] == "[":
                affected_boxes_to_check.append((x, y-1))
            elif map[y-1][x] == "]":
                affected_boxes_to_check.append((x-1, y-1))
            elif map[y-1][x] == WALL:
                return rx, ry

            # iterate upwards on the map, and if all affected boxes can move upwards
            while len(affected_boxes_to_check) != 0:
                box = affected_boxes_to_check.pop()
                all_affected_boxes.append(box)
                bx = box[0]
                by = box[1]
                # if any cell above is a wall, the box can't move
                if map[by-1][bx] == WALL or map[by-1][bx+1] == WALL:
                    can_move = False
                    break
                
                # if the cell above is a box, add it to the list of affected boxes
                if map[by-1][bx] == "[":
                    affected_boxes_to_check.append((bx, by-1))
                elif map[by-1][bx] == "]":
                    affected_boxes_to_check.append((bx-1, by-1))
                if map[by-1][bx+1] == "[":

                    affected_boxes_to_check.append((bx+1, by-1))
                #no need to check for "]", it was covered by the first 'if'

            if not can_move:
                return rx, ry
            
            # remove the duplicates from the list of affected boxes
            all_affected_boxes = list(set(all_affected_boxes))

            #sort the affected boxes based on their y coordinate
            all_affected_boxes.sort(key=lambda x: x[1])

            for box in all_affected_boxes:
                bx = box[0]
                by = box[1]
                map[by-1][bx] = map[by][bx]
                map[by-1][bx+1] = map[by][bx+1]
                map[by][bx] = BLANK
                map[by][bx+1] = BLANK
            
            map[ry+dir[1]][rx] = ROBOT

        if dir == DOWN_DIR:
            if map[y+1][x] == "[":
                affected_boxes_to_check.append((x, y+1))
            elif map[y+1][x] == "]":
                affected_boxes_to_check.append((x-1, y+1))
            elif map[y+1][x] == WALL:
                return rx, ry

            # iterate downwards on the map, and if all affected boxes can move downwards
            while len(affected_boxes_to_check) != 0:
                box = affected_boxes_to_check.pop()
                all_affected_boxes.append(box)
                bx = box[0]
                by = box[1]
                # if any cell below is a wall, the box can't move
                if map[by+1][bx] == WALL or map[by+1][bx+1] == WALL:
                    can_move = False
                    break
                
                # if the cell below is a box, add it to the list of affected boxes
                if map[by+1][bx] == "[":
                    affected_boxes_to_check.append((bx, by+1))
                elif map[by+1][bx] == "]":
                    affected_boxes_to_check.append((bx-1, by+1))
                if map[by+1][bx+1] == "[":
                    affected_boxes_to_check.append((bx+1, by+1))
                #no need to check for "]", it was covered by the first 'if'

            if not can_move:
                return rx, ry
            
            # remove the duplicates from the list of affected boxes
            all_affected_boxes = list(set(all_affected_boxes))

            #sort the affected boxes based on their y coordinate, in reverse
            all_affected_boxes.sort(key=lambda x: x[1], reverse=True)

            for box in all_affected_boxes:
                bx = box[0]
                by = box[1]
                map[by+1][bx] = map[by][bx]
                map[by+1][bx+1] = map[by][bx+1]
                map[by][bx] = BLANK
                map[by][bx+1] = BLANK
            
            map[ry+dir[1]][rx] = ROBOT

    map[y][x] = BLANK
    return x + dir[0], y + dir[1]

def save_map_to_file(map, filename):
    with open(filename, 'w') as f:
        for row in map:
            for c in row:
                f.write(c)
            f.write("\n")

def do2(map, movements, rx, ry):
    map = transform_map(map)
    total = 0
    x = rx * 2
    y = ry

    save_map_to_file(map, "start-map.txt")

    counts = defaultdict(int)
    for row in map:
        for c in row:
            cc = counts.pop(c, 0)
            counts[c] = cc + 1

    i = 0

    counts2 = defaultdict(int)

    for m in movements:
        # if i > 1288:
        #     display_map(map)
        #     print(f"movement: {m}, step: {i}/{len(movements)}")        
        #     input("Press Enter to continue...")

        x, y = move2(map, m, x, y)
        i += 1

        if i % 100 == 0:
            counts2.clear()
            for row in map:
                for c in row:
                    cc = counts2.pop(c, 0)
                    counts2[c] = cc + 1

            print(f"step: {i}, counts: #: {counts2[WALL]}, O: {counts2[BOX]}, [: {counts2[BIGBOX[0]]}, ]: {counts2[BIGBOX[1]]}, @: {counts2[ROBOT]}, .: {counts2[BLANK]}")

            if counts[WALL] != counts2[WALL] or counts[BOX] != counts2[BOX] or counts[BIGBOX[0]] != counts2[BIGBOX[0]] or counts[BIGBOX[1]] != counts2[BIGBOX[1]] or counts[ROBOT] != counts2[ROBOT] or counts[BLANK] != counts2[BLANK]:
                print(f"counts changed at step {i}")
                print(f"movement: {m}, step: {i}/{len(movements)}")        
                input("Press Enter to continue...")


    #save map to a file
    #save_map_to_file(map, "result-map.txt")

    total = sum_boxes(map)

    # 1323714 - too low
    # 1337648 - BINGO :)
    print(f"total: {total}")
        
# still have to figure out how to look for local file in VS Code :(
input_file = r'd:\OneDrive\Documents\Projects\AoC\2024\advent-of-code-2024\15\input.txt'   

map, movements, rx, ry = load_map(input_file)

# t1 = time.time()
# do1(map, movements, rx, ry)
# t2 = time.time()

# print(f"elapsed time: {(t2-t1)} seconds")

t1 = time.time()
do2(map, movements, rx, ry)
t2 = time.time()

print(f"elapsed time: {(t2-t1)} seconds")