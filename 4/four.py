print("Welcome to Day 4!")

target = "XMAS"

def checkIfXmas(content, x, y, xdir, ydir ) -> bool:
    
    i = 0
    xorig = x
    yorig = y
    while i < len(target):
        if x<0 or y<0 or y>=len(content) or x>=len(content[y]): return False
        if content[y][x] != target[i]: return False
        x += xdir
        y += ydir
        i += 1

    print (f"found one at {xorig}, {yorig}")
    return True

def checkifX_Mas(content, x, y) -> bool:

    try:
        if content[y][x] == "A":
            if (content[y-1][x-1]=="M" and content[y+1][x+1]=="S") or (content[y-1][x-1]=="S" and content[y+1][x+1]=="M"): 
                if (content[y-1][x+1]=="M" and content[y+1][x-1]=="S") or (content[y-1][x+1]=="S" and content[y+1][x-1]=="M"): 
                    print (f"found one at {x}, {y}")
                    return True
        
    except:
        return False 

    return False



def countXmas(input_file):
    xmascount = 0
    
    with open(input_file, 'r') as infile:
        content = [line.strip() for line in infile]
        xs =len(content[0])
        ys = len(content)

        for y in range(0, ys):
            for x in range(0, xs):
                if content[y][x] == "X":
                    if checkIfXmas(content, x, y,  1,  0): xmascount += 1 # West
                    if checkIfXmas(content, x, y, -1,  0): xmascount += 1 # East
                    if checkIfXmas(content, x, y,  0,  1): xmascount += 1 # South
                    if checkIfXmas(content, x, y,  0, -1): xmascount += 1 # North
                    if checkIfXmas(content, x, y,  1, -1): xmascount += 1 # NE
                    if checkIfXmas(content, x, y,  1,  1): xmascount += 1 # SE
                    if checkIfXmas(content, x, y, -1, -1): xmascount += 1 # NW
                    if checkIfXmas(content, x, y, -1,  1): xmascount += 1 # SW
                        
    print(f"xmascount = {xmascount} ")    

def countX_Mas(input_file):
    xmascount = 0
    
    with open(input_file, 'r') as infile:
        content = [line.strip() for line in infile]
        xs =len(content[0])
        ys = len(content)

        for y in range(0, ys):
            for x in range(0, xs):
                if content[y][x] == "A":
                    if checkifX_Mas(content, x, y): xmascount += 1 # X :)
                    
                        
    print(f"x-mas count = {xmascount} ")    

# still have to figure out how to look for local file in VS Code :(
input_file = r'd:\OneDrive\Documents\Projects\AoC\2024\advent-of-code-2024\4\input.txt'   

countXmas(input_file)
countX_Mas(input_file)
