print("Welcome to Day 2!")

def checkIfSave(level) -> bool:
    dir = 0 # -1 for desc, 1 for inc

    for i in range (1, len(level)): # omit the first item, start with the second since we only need the difference
        diff = int(level[i]) - int(level[i-1])
        if abs(diff) == 0 or abs(diff) > 3:
            return False
        if dir == 0: # if this is the first diff, set direction
            if diff > 0:
                dir = 1
            else:
                dir = -1
        else:
            if dir * diff < 0:
                return False
    return True


def level_safety(input_file):
    safecount = 0
    with open(input_file, 'r') as infile:
        for line_number, line in enumerate(infile, start=1):
            levellist = line.split()

            if checkIfSave(levellist): safecount = safecount + 1
    
    print(f"safecount = {safecount} ")    


def level_safety_dampened(input_file):
    safecount = 0
    with open(input_file, 'r') as infile:
        for line_number, line in enumerate(infile, start=1):
            levellist = line.split()

            if checkIfSave(levellist): safecount = safecount + 1
            else:
                for i in range(0, len(levellist)):
                    newlist = levellist.copy() # copy the list so that we can remove items one by one... not nice but working :)
                    newlist.pop(i)
                    if checkIfSave(newlist):
                        safecount = safecount + 1
                        break
                        
    print(f"safecount = {safecount} ")    


input_file = r'd:\OneDrive\Documents\Projects\AoC\2024\advent-of-code-2024\2\input.txt'   

level_safety(input_file)
level_safety_dampened(input_file)
