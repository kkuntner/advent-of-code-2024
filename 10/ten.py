print("Welcome to Day 8!")

from collections import defaultdict
import time

def loadMap(input_file):

    map = []

    with open(input_file, 'r') as infile:
        for line in infile: 
            line = line.strip()
            row = []
            for c in line:
                row.append(int(c))
            map.append(row)

    return map

    

# go through a map, and look for number
# when found, count how many number+1 are around it
# and put the resulting sum in the countermap   
def search(map, number, countermap):
        
        newcountermap = [[0 for x in range(len(map[0]))] for y in range(len(map))] 

        for y in range(0, len(map)):
            for x in range(0, len(map[y])):
                if map[y][x] == number:
                    sum = 0
                    if number == 9:
                        sum = 1
                    else:
                        # see if above exists, and it is a number+1
                        # if yes, add countermap's same position to up                        
                        if y > 0 and map[y-1][x] == number+1:
                            sum += countermap[y-1][x]
                        # see if below exists, and it is a number+1
                        # if yes, add countermap's same position to up
                        if y < len(map)-1 and map[y+1][x] == number+1:
                            sum += countermap[y+1][x]
                        # see if left exists, and it is a number+1
                        # if yes, add countermap's same position to up
                        if x > 0 and map[y][x-1] == number+1:
                            sum += countermap[y][x-1]
                        # see if right exists, and it is a number+1
                        # if yes, add countermap's same position to up
                        if x < len(map[y])-1 and map[y][x+1] == number+1:
                            sum += countermap[y][x+1]

                    newcountermap[y][x] = sum
        return newcountermap

def sumAllMap(map):
    sum = 0
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            sum += map[y][x]
    return sum   


def do1(map):
    
    # create a list of int lists, with the same dimensions as the map
    # and fill it with 0's
    countermap = [[0 for x in range(len(map[0]))] for y in range(len(map))] 
    
    # go through the map, and for each number, call search
    # with the number, the map and the countermap
    for i in range(10, 0, -1):
        countermap = search(map, i-1, countermap)

    sum = sumAllMap(countermap)

    print(f"the result is: {sum}")
    return sum

# still have to figure out how to look for local file in VS Code :(
input_file = r'd:\OneDrive\Documents\Projects\AoC\2024\advent-of-code-2024\10\input.txt'   


t1 = time.time()

map = loadMap(input_file)
do1(map)

t2 = time.time()
print(f"elapsed time: {(t2-t1)} seconds")
