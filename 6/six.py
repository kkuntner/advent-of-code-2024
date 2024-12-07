print("Welcome to Day 6!")

from collections import defaultdict
import time

OBSTACLE = '#'
START = '^'
FIELD = '.'
startx = 0
starty = -1

N = (0,-1)
S = (0, 1)
E = (1 ,0)
W = (-1,0)

RightTurnDirections = {N: E, E: S, S: W, W: N}

def loadMap(input_file):
    map = []
    with open(input_file, 'r') as infile:
        ypos = 0
        for line in infile:
            row = line.strip()
            map.append(list(row))
            p = line.find(START)
            if p != -1: # found the start pos, set startx and starty
                global startx
                global starty
                starty = ypos
                startx = p
            else:
                ypos+=1
    return map

def runAroundOnce(map, needPositions):
    # will return a list of fields we moved on. obstacles outside these will have no effect.

    xsize =len(map[0])
    ysize = len(map)

    currx = startx
    curry = starty
    (xdir, ydir) = N # direction of movement on the x and y axis

    result = -1 # 0 = infinite, 1 = walked offmap
    
    # we'll put direction and coordinate values here 
    visiteds = set()

    # run while we stay in the grid
    while 0 <= currx < xsize and 0 <= curry < ysize and result == -1:
        position = (currx, curry)
        direction = (xdir, ydir)
        
        # check if we have been at this position, walking in the same direction. 
        # If yes, this is an infinite loop
        # if no, put it in the appropriate direction's set to see if we come back later        
        
        if (position, direction) in visiteds:
            #print("we've been here before, walking the same direction")
            result = 0
            break
        else:
            visiteds.add((position, direction))

        if currx+xdir < 0 or currx+xdir == xsize or curry+ydir < 0 or curry+ydir == ysize:
            # walked off the map
            result = 1
            break
            
        while map[curry+ydir][currx+xdir] == OBSTACLE:
            # we'd hit an obstacle, turn right until path is clear
            (xdir, ydir) = RightTurnDirections[(xdir, ydir)]
                           
        currx += xdir
        curry += ydir
    
    if needPositions:
        visitedfields = set()
        for (p, d) in visiteds: visitedfields.add(p)

        #print(f"places visited = {len(visitedfields)+1}")                      

        return result, visitedfields
    
    return result

def tryObstacles(map, positions):
    infiniteLoopCounter = 0

    for (x,y) in positions:
        # if the current position to check is the start or an existing obstacle, skip checking.
        if map[y][x] != FIELD:
            continue
        
        #put an obstacle there, and see if it loops or exits
        map[y][x] = OBSTACLE
        result = runAroundOnce(map, False)
        if result == 0: # resulted in an infinite loop
            infiniteLoopCounter += 1

        map[y][x] = FIELD

    print(f"inifinite loops occurred {infiniteLoopCounter} times")

# still have to figure out how to look for local file in VS Code :(
input_file = r'd:\OneDrive\Documents\Projects\AoC\2024\advent-of-code-2024\6\input.txt'   

t1 = time.time()
map = loadMap(input_file)
r, positions = runAroundOnce(map, True)
tryObstacles(map, positions)
t2 = time.time()
print(f"elapsed time: {(t2-t1)} seconds")
# 1711 :)