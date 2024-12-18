print("Welcome to Day Friday, 13!")

class machine:
    def __init__(self, ax, ay, bx, by, rx, ry):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.rx = rx
        self.ry = ry


from collections import defaultdict
import time

def loadRules(input_file):

    machines = []

    # input file is structured like this:
    # Button A: X+94, Y+34
    # Button B: X+22, Y+67
    # Prize: X=8400, Y=5400
    # read input file
    with open(input_file, 'r') as infile:
               
        while True:
            rowa = infile.readline().strip()
            if rowa == '' :
                rowa = infile.readline().strip()
                if rowa == '' :
                    break
            rowb = infile.readline().strip()
            rowres = infile.readline().strip()
            
            ax = int(rowa.split('+')[1].split(',')[0])
            ay = int(rowa.split('+')[2])

            bx = int(rowb.split('+')[1].split(',')[0])
            by = int(rowb.split('+')[2])

            rx = int(rowres.split('=')[1].split(',')[0])
            ry = int(rowres.split('=')[2])

            machines.append(machine(ax, ay, bx, by, rx, ry))

    return machines


def find_solutions(ax, bx, rx):
    solutions = set()
    # find the solutions where an*ax+bn*bx = rx
    bn = 0
    while (bn*bx) <= rx:
        an = 0
        if (rx-bn*bx) % ax == 0:
            an = (rx-bn*bx) // ax
            solutions.add((an, bn))
        
        bn += 1
    return solutions

def find_minimum_cost_solutions(solutions):
    # find the minimum cost solution
    # where the cost of the solution is 3*an+bn
    mincost = 99999999
    for solution in solutions:
        cost = 3*solution[0] + solution[1]
        if cost < mincost:
            mincost = cost
    return mincost

def do1(machines):
    total = 0

    for machine in machines:
        xsolutions = find_solutions(machine.ax, machine.bx, machine.rx)
        ysolutions = find_solutions(machine.ay, machine.by, machine.ry)
        
        solutions = xsolutions.intersection(ysolutions)
        if len(solutions) == 0:
            print(f"No solutions found")
        else:
            mincost = find_minimum_cost_solutions(solutions)
            total += mincost

    print(f"total: {total}")

def do2(machines):
    total = 0
    offset = 10000000000000
    # that is 10 000 000 000 000

    for machine in machines:
        xsolutions = find_solutions(machine.ax, machine.bx, machine.rx+offset)
        ysolutions = find_solutions(machine.ay, machine.by, machine.ry+offset)
        
        solutions = xsolutions.intersection(ysolutions)
        if len(solutions) == 0:
            print(f"No solutions found")
        else:
            mincost = find_minimum_cost_solutions(solutions)
            total += mincost

    print(f"total: {total}")


# still have to figure out how to look for local file in VS Code :(
input_file = r'd:\OneDrive\Documents\Projects\AoC\2024\advent-of-code-2024\13\input.txt'   

rules = loadRules(input_file)

t1 = time.time()
regions = do1(rules)
t2 = time.time()

print(f"elapsed time: {(t2-t1)} seconds")

t1 = time.time()
regions = do2(rules)
t2 = time.time()

print(f"elapsed time: {(t2-t1)} seconds")
