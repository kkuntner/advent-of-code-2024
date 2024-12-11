print("Welcome to Day 11!")

from collections import defaultdict
import time

def loadStones(input_file):

    stones = []

    with open(input_file, 'r') as infile:
        line = infile.readline()
        line = line.strip()
        # split the line separated by spaces into a list of numbers
        stones = [int(x) for x in line.split(" ")]  

    return stones


def processStone(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        s = str(stone)
        return [int(s[0:len(s)//2]), int(s[len(s)//2:])]
    else:
        return [stone * 2024]


def getStones(stones, iteration):
    counts = dict()
    # put stones into count with counter 1
    for stone in stones:
        counts[stone] = 1
    
    # do the iterations
    for i in range(iteration):
        newcounts = dict()

        # go over the counts and process each stone
        for (key, count) in counts.items():
            newstones = processStone(key)
            for newstone in newstones:
                if newstone in newcounts:
                    newcounts[newstone] += count
                else:
                    newcounts[newstone] = count 

        counts = newcounts
    
    return counts


def do2(stones, steps):
    counts = getStones(stones, steps)
    
    print(f"sum of counts: {sum(counts.values())}")

    return counts

# brute force, calculating all values. this would have run for thousands of years
# for step 2 :) 
def do1(stones, steps):
    
    for count in range(steps):
        t1 = time.time()
        i = 0
        while i < len(stones):
            newstones = processStone(stones[i])
            if len(newstones) == 1:
                stones[i] = newstones[0]
                i += 1
            else:
                stones.pop(i)
                for j in range(len(newstones)):
                    stones.insert(i+j, newstones[j])
                i += 2
        t2 = time.time()
        print(f"step: {count}, time: {(t2-t1)}, count: {len(stones)}")#, stones: {stones}")  
    return stones

# still have to figure out how to look for local file in VS Code :(
input_file = r'd:\OneDrive\Documents\Projects\AoC\2024\advent-of-code-2024\11\input.txt'   

stones = loadStones(input_file)

t1 = time.time()
do2(stones, 25)
t2 = time.time()

print(f"elapsed time: {(t2-t1)} seconds")

t1 = time.time()
do2(stones, 75)
t2 = time.time()
print(f"elapsed time: {(t2-t1)} seconds")
