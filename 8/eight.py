print("Welcome to Day 8!")

from collections import defaultdict
import time

BLANK = '.'

def loadMap(input_file):

    map = []
    antennas = defaultdict(list)
    freequencies = set()
    with open(input_file, 'r') as infile:
        y = 0
        for line in infile:
            row = line.strip()
            map.append(row)
            x = 0
            for field in row:
                if field != BLANK:
                    antennas[field].append((x,y))
                    freequencies.add(field)
                x += 1
            y += 1

    return map, antennas, freequencies

def do1(map, antennas, frequencies):
    sum = 0
    antinodes = set()
    mapxsize = len(map[0])
    mapysize = len(map)
    for f in frequencies:
        # get all the antennas for this freq
        currentantennas = antennas[f]
        
        # go through each, and pair it with all others
        # only look at the subsequent ones
        for i in range(len(currentantennas)):
            (x, y) = currentantennas[i]
            for j in range(i+1, len(currentantennas)):
                (cx, cy) = currentantennas[j]
                dx = cx - x
                dy = cy - y
                anupx = cx+dx
                anupy = cy+dy
                andownx = x - dx
                andowny = y - dy
                # if within bounds, found one
                if 0 <= anupx < mapxsize and 0 <= anupy < mapysize:
                    antinodes.add((anupx, anupy))

                if 0 <= andownx < mapxsize and 0 <= andowny < mapysize:
                    antinodes.add((andownx, andowny))
        
    print(f"the result is: {len(antinodes)}")
    return sum


def do2(map, antennas, frequencies):
    sum = 0
    antinodes = set()
    mapxsize = len(map[0])
    mapysize = len(map)
    for f in frequencies:
        # get all the antennas for this freq
        currentantennas = antennas[f]
        
        # go through each, and pair it with all others
        # only look at the subsequent ones
        for i in range(len(currentantennas)):
            (x, y) = currentantennas[i]
            for j in range(i+1, len(currentantennas)):
                (cx, cy) = currentantennas[j]
                dx = cx - x
                dy = cy - y
                anupx = cx
                anupy = cy
                andownx = x
                andowny = y
                # while within bounds, found one
                while 0 <= anupx < mapxsize and 0 <= anupy < mapysize:
                    antinodes.add((anupx, anupy))
                    anupx += dx
                    anupy += dy

                while 0 <= andownx < mapxsize and 0 <= andowny < mapysize:
                    antinodes.add((andownx, andowny))
                    andownx -= dx
                    andowny -= dy

    print(f"the result is: {len(antinodes)}")
    return sum

# still have to figure out how to look for local file in VS Code :(
input_file = r'd:\OneDrive\Documents\Projects\AoC\2024\advent-of-code-2024\8\input.txt'   


t1 = time.time()

map, antennas, freequencies = loadMap(input_file)
do1(map, antennas, freequencies)

do2(map, antennas, freequencies)


t2 = time.time()
print(f"elapsed time: {(t2-t1)} seconds")
