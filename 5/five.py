print("Welcome to Day 5!")

from collections import defaultdict

# if before[4] contains 23 that means that 23 must appear before 4
before = defaultdict(list)
# if after[23] contains 4 that means that 4 must appear after 23 (same as above)
after = defaultdict(list)

def checkLineMatchesRules(pages):
    fail = False
    # check each page
    for i in range(len(pages)):
        currentpage = pages[i]
        #then check each page after this one if any rules are violated
        for j in range(i+1, len(pages)):
            pageToCheck = pages[j]
            # if there is a rule that specifies that the j page must be before i, STOP
            if currentpage in before[pageToCheck]:
                fail = True
                break
            # else if there is a rule that specifies that the i page must be after j, STOP
            elif pageToCheck in after[currentpage]:
                fail = True
        if fail: break
    
    return not fail
    
def checkWhichPagesAreWrong(pages):
    fail = False
    # check each page
    for i in range(len(pages)):
        currentpage = pages[i]
        #then check each page after this one if any rules are violated
        for j in range(i+1, len(pages)):
            pageToCheck = pages[j]
            # if there is a rule that specifies that the j page must be before i, STOP
            if currentpage in before[pageToCheck]:
                fail = True
                break
            # else if there is a rule that specifies that the i page must be after j, STOP
            elif pageToCheck in after[currentpage]:
                fail = True
        if fail: break
    
    if not fail: 
        i = -1
        j = -1

    return i, j

def loadRules(input_file):
    correcttotal = 0
    incorrecttotal = 0

    incorrects = []

    with open(input_file, 'r') as infile:
        for line in infile:
            if line.strip() == '':
                break
            b, a = line.split('|')

            before[int(b)].append(int(a))
            after[int(a)].append(int(b))

        # now we loaded the rules. let's start loading the updates, and process them as we go
        for line in infile:
            pages = [int(x) for x in line.split(',')]

            if checkLineMatchesRules(pages):
                # add the middle page to total
                correcttotal += pages[len(pages) // 2]
            else:
                incorrects.append(pages)

    print(f"correcttotal = {correcttotal} ")    

    # now go throuth each incorrect and fix'em up
    for pages in incorrects:
        # might be an ugly bruteforce BUT :) let's check the rules, and where there is a mismatch
        # replace the two values, and start over to see if it breaks any other rule
        # let's hope the rules won't cause infinite loops :)
       
        while not checkLineMatchesRules(pages):
            i,j = checkWhichPagesAreWrong(pages)
            k = pages[i]
            pages [i] = pages [j]
            pages [j] = k

        incorrecttotal += pages[len(pages) // 2]                

    print(f"incorrecttotal = {incorrecttotal} ")    
                        
# still have to figure out how to look for local file in VS Code :(
input_file = r'd:\OneDrive\Documents\Projects\AoC\2024\advent-of-code-2024\5\input.txt'   

loadRules(input_file)
