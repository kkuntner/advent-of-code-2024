print("Welcome to Day 12!")

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

def next_unseen(currentx, currenty, unseens):
    x = currentx
    for y in range(currenty, len(unseens)):
        while x < len(unseens[0]):
            if unseens[y][x] == 0:
                return x, y
            x += 1
        x = 0
    return -1, -1

def get_same_type_unvisited_neighbors(x, y, map, typ, visiteds):
    neighbors = []    
    if x > 0 and map[y][x-1] == typ and visiteds[y][x-1] == 0:
        neighbors.append((x-1, y))
    if x < len(map[0]) - 1 and map[y][x+1] == typ and visiteds[y][x+1] == 0:
        neighbors.append((x+1, y))
    if y > 0 and map[y-1][x] == typ and visiteds[y-1][x] == 0:
        neighbors.append((x, y-1))
    if y < len(map) - 1 and map[y+1][x] == typ and visiteds[y+1][x] == 0:
        neighbors.append((x, y+1))
    return neighbors

def get_same_type_neighbors(x, y, map, typ):
    neighbors = []    
    if x > 0 and map[y][x-1] == typ:
        neighbors.append((x-1, y))
    if x < len(map[0]) - 1 and map[y][x+1] == typ:
        neighbors.append((x+1, y))
    if y > 0 and map[y-1][x] == typ:
        neighbors.append((x, y-1))
    if y < len(map) - 1 and map[y+1][x] == typ:
        neighbors.append((x, y+1))
    return neighbors

def do1(map, types):
    # unsens ia a two dimensional array of integers
    visiteds = [[0 for i in range(len(map[0]))] for j in range(len(map))]
    
    total = 0

    regions = []

    xpos = ypos = 0

    while True:
        # get the current plot type
        typ = map[ypos][xpos]
        region = [(xpos, ypos)]
        unprocesseds = region.copy()

        perimeter = 0
        while len(unprocesseds) > 0:
            x, y = unprocesseds.pop()
            visiteds[y][x] = 1
            neighbors = get_same_type_unvisited_neighbors(x, y, map, typ, visiteds)

            perimeter += 4 - len(get_same_type_neighbors(x, y, map, typ))
            for x, y in neighbors:
                if visiteds[y][x] == 0:
                    region.append((x, y))
                    unprocesseds.append((x, y))
                    visiteds[y][x] = 1

        # now we have a region of the same type
        # count its area - easy
        area = len(region)
        regions.append(region)

        print(f"type: {typ}, area: {area}, perimeter: {perimeter}")

        total += area * perimeter

        xpos, ypos = next_unseen(xpos, ypos, visiteds)

        if (xpos, ypos) == (-1, -1):
            break

    
    
    print(f"total: {total}")
    return regions

def normalize_region(region : list):
    x0 = min(region, key = lambda x: x[0])[0]
    y0 = min(region, key = lambda x: x[1])[1]
    return [(x - x0, y - y0) for x, y in region]

def region_to_map(region):
    xmin = min(region, key = lambda x: x[0])[0]
    ymin = min(region, key = lambda x: x[1])[1]
    xmax = max(region, key = lambda x: x[0])[0]
    ymax = max(region, key = lambda x: x[1])[1]

    map = [[0 for i in range(xmax-xmin+1)] for j in range(ymax-ymin+1)]
    for x, y in region:
        map[y-ymin][x-xmin] = 1
    return map


def rotate_map(map):
    newmap = [['0' for i in range(len(map))] for j in range(len(map[0]))]
    for y in range(len(map)):
        for x in range(len(map[0])):
            newmap[x][len(map) - y - 1] = map[y][x]
    return newmap    

def is_above(map, x, y):
    if y == 0:
        return False
    return map[y-1][x] == 1

def is_left(map, x, y):
    if x == 0:
        return False
    return map[y][x-1] == 1

def is_left_and_leftabove(map, x, y):
    if x == 0 or y == 0:
        return False
    return map[y][x-1] == 1 and map[y-1][x-1] == 1

def calculate_upper_edges(map):
    count = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] and not is_above(map, x, y):
                if (not is_left(map, x, y)) or (is_left_and_leftabove(map, x, y)):
                    print(f"upper edge at {x}, {y}")
                    count += 1
    return count                            

def do2(regions):
    total = 0
    for region in regions:
        region = normalize_region(region)
        map = region_to_map(region)

        fences = 0
        for i in range(4):
            print(f"rotation {i}")
            fences += calculate_upper_edges(map)        
            
            map = rotate_map(map)

        cost = fences * sum([sum([1 for c in row if c == 1]) for row in map])
        total += cost
        print(f"region cost: {cost}")
    print(f"total cost: {total}")


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
