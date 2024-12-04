import re

print("Welcome to Day 3!")

# check if s is "mul(X,Y)" where X and Y are 1-3 digit numbers.
# so the longest possibility is mul(123,456) = 12 characters, so let's look at 12 char chunks
# if they match regex
def checkIfMul(s):
    pattern = r"^mul\((\d{1,3}),(\d{1,3})\).*"

    match = re.match(pattern, s)
    if match:
        print (f"match: {s}")
        x, y = match.groups()
        return int(x)*int(y)
    return -1

def checkIfDo(s):
    pattern = r"^do\(\).*"

    match = re.match(pattern, s)
    if match:
        return True
    return False


def checkIfDont(s):
    pattern = r"^don't\(\).*"

    match = re.match(pattern, s)
    if match:
        return True
    return False

def summarize_muls(input_file):
    sum = 0
    on = True

    with open(input_file, 'r') as infile:
        content = infile.read()

        i = 0
        while i < len(content):
            if checkIfDo(content[i:i+4]): 
                on = True
                i = i + 4
            elif checkIfDont(content[i:i+7]): 
                on = False
                i = i + 7
            else:
                mul = checkIfMul(content[i:i+12])
                if mul == -1:
                    i = i + 1
                else:
                    if on: sum += mul
                    i = i + 8 # ugly but better than nothing: 8 is the shortest possible match
            
    print(f"sum = {sum} ")    

input_file = r'd:\OneDrive\Documents\Projects\AoC\2024\advent-of-code-2024\3\input.txt'   

summarize_muls(input_file)
# 182351453 is too low