print("Welcome to Day Friday, 13!")

from collections import defaultdict
import time

def loadMap(input_file):

    map = []
    types = set()

    with open(input_file, 'r') as infile:
        for line in infile:
            row = line.strip()        
            # split the line separated by spaces into a list of numbers
            map.append(row)
            for c in row:
                types.add(c)

    return types, map



def do1(map, types):
    total = 0
    
    print(f"total: {total}")

def do2(regions):
    total = 0
    

    print(f"total: {total}")


# still have to figure out how to look for local file in VS Code :(
input_file = r'd:\OneDrive\Documents\Projects\AoC\2024\advent-of-code-2024\12\input.txt'   

types, map = loadMap(input_file)

t1 = time.time()
regions = do1(map, types)
t2 = time.time()

print(f"elapsed time: {(t2-t1)} seconds")

t1 = time.time()
do2(regions)
t2 = time.time()
print(f"elapsed time: {(t2-t1)} seconds")
