print("Welcome to Day 7!")

from collections import defaultdict
import time


def loadMap(input_file):

    rows = []
    with open(input_file, 'r') as infile:
        
        for line in infile:
            row = line.strip()
            result = int(row.split(':')[0])
            numbers = [int(x) for x in row.split(':')[1].split()]

            rows.append((result, numbers))

    return rows

def checkRow(result, numbers):
    # we have this many positions
    numofplaces = len(numbers)-1
    sum = 0

    found = False
    for i in range(2 ** numofplaces): # go until 2**n-1
        binn = format(i, f"0{numofplaces}b")
        currentsum = numbers[0]
        for j in range(numofplaces):
            # 0 means add, 1 means multiply
            if binn[j] == '0':
                currentsum += numbers[j+1]
            else:   
                currentsum *= numbers[j+1]
        if currentsum == result:
            sum += result
            found = True
            break
    return found

def do1(rows):
    sum = 0
    incorrects = []
    for (result, numbers) in rows:

        if checkRow(result, numbers):
            sum += result
        else:
            incorrects.append((result, numbers))

    print(f"the result is: {sum}")
    return sum, incorrects

def toBase3(number, places):
    if number == 0:
        return '0'.zfill(places)
    
    base3 = []
    while number>0:
        base3.append(str(number % 3))
        number //= 3
    return ''.join(reversed(base3)).zfill(places)


def do2(rows):
    #rows are the incorrects
    sum = 0
    c = 0
    for (result, numbers) in rows:
        c += 1
        print(f"checking row {c}...")
        # we have this many positions
        numofplaces = len(numbers)-1

        found = False
        for i in range(3 ** numofplaces): # go until 3**n-1
            trin = toBase3(i, numofplaces)

            # if there is no concatenation - we've done this in part 1, no need to check
            if trin.find('2') == -1:
                continue
            currentsum = numbers[0]
            for j in range(numofplaces):
                if trin[j] == '2':
                    # if concat, concat the last result with the next number
                    currentsum = int(f"{currentsum}{numbers[j+1]}")
                elif trin[j] == '0':
                    currentsum += numbers[j+1]
                else:   
                    currentsum *= numbers[j+1]  
            if currentsum == result:
                sum += result
                found = True
                break

    print(f"the result is: {sum}")
    return sum

# still have to figure out how to look for local file in VS Code :(
input_file = r'd:\OneDrive\Documents\Projects\AoC\2024\advent-of-code-2024\7\input.txt'   

t1 = time.time()

rows = loadMap(input_file)
sum, incorrects = do1(rows)

sum2 = do2(incorrects)

print(f"total of the two sums:{sum+sum2}")
# do2()

t2 = time.time()
print(f"elapsed time: {(t2-t1)} seconds")
# ????  :)