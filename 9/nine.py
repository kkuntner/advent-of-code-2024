print("Welcome to Day 8!")

from collections import defaultdict
import time

BLANK = -1

def loadMap(input_file):

    disk = []
    firstblank = -1

    # load a file with a single row into an array
    with open(input_file, 'r') as infile:
        
        y = 0
        line = infile.readline()
        file = 1 # represents if this is a file or a space
        fileID = 0
        for char in line:
            for i in range(int(char)):
                if (file):
                    disk.append(fileID)
                else:
                    if firstblank == -1:
                        firstblank = len(disk)
                    disk.append(BLANK)

            if (file):
                fileID += 1
            file = 1 - file # 1 -> 0 -> 1 -> 0            

    return disk, firstblank


def nextBlank(disk, searchAt):
    for i in range(searchAt, len(disk)):
        if disk[i] == BLANK:
            return i
    return -1

def nextBlank(disk, searchAt, last, size):
    s = 0
    for i in range(searchAt, last):
        if (disk[i] == BLANK):
            s += 1
            if s == size:
                return i - size + 1
        else:
            s = 0

    return -1


def defrag1(disk, firstblank):
    # go through disk from the end, and move files to the first blank position
    for i in range(len(disk)-1, firstblank, -1):
        id = disk[i]
        if id == BLANK:
            disk.pop(i)
            continue
        else:
            
            blank = nextBlank(disk, firstblank)
            if blank == -1:
                break
            else:
                disk[blank] = disk[i]
                disk.pop(i)
    
def defrag2(disk, firstblank):
    i = len(disk)-1
    highsetIdMoved = 99999999999
    while i > firstblank:
        id = disk[i]
        if (id == BLANK):
            i -= 1
            continue
        j = i-1
        # look for the beginning of the file - it will be j
        while (disk[j] == id and j > firstblank):
            j -= 1
        size = i - j

        # if we have already moved this file, skip it
        if id > highsetIdMoved:
            i -= size
            continue

        print(f"trying to move file {id}")

        moveto = nextBlank(disk, firstblank, i, size)
        highsetIdMoved = id
        if moveto == -1:
            i -= size
            continue
        else:
            for k in range(size):
                disk[moveto+k] = id
                disk[j+k+1] = BLANK
            i -= size

def countChecksum(disk):
    sum = 0
    for i in range(len(disk)):
        if disk[i] != BLANK:
            sum += i * disk[i]
    print(f"the result is: {sum}")
    return sum


def do1(disk, firstblank):
    
    defrag1(disk, firstblank)

    countChecksum(disk)

    #print(f"the result is: {sum}")
    return sum


def do2(disk, firstblank):
    
    defrag2(disk, firstblank)

    countChecksum(disk)

    # print(f"the result is: {len(antinodes)}")
    return sum

# still have to figure out how to look for local file in VS Code :(
input_file = r'd:\OneDrive\Documents\Projects\AoC\2024\advent-of-code-2024\9\input.txt'   


t1 = time.time()

disk, firstblank = loadMap(input_file)
#do1(disk, firstblank)

do2(disk, firstblank)

t2 = time.time()
print(f"elapsed time: {(t2-t1)} seconds")
