print("Welcome to Day 17!")

from collections import defaultdict
import numpy as np
import os
import heapq

import time

A = "A"
B = "B"
C = "C"

def load_prog(input_file):

    with open(input_file, 'r') as f:
        # first three lines are "Register X: 123"
        # read the number and store it in the register
        line = f.readline().strip()
        reg, val = line.split(":")
        reg = reg.split()[1]
        Ax = int(val)

        line = f.readline().strip()
        reg, val = line.split(":")
        reg = reg.split()[1]
        Bx = int(val)

        line = f.readline().strip()
        reg, val = line.split(":")
        reg = reg.split()[1]
        Cx = int(val)

        line = f.readline().strip()
        # next line is "Program: n, n, n, ..."
        line = f.readline().strip()
        prog = [int(x) for x in line.split(":")[1].split(",")]

    return Ax, Bx, Cx, prog

def extr_combo_operand(operand, registers):
    if operand<=3:
        return operand
    elif operand == 4: return registers[A]        
    elif operand == 5: return registers[B]        
    elif operand == 6: return registers[C]        
    else: return -1

result = ""

def resout(val):
    global result

    if (result != ""):
        result += ","

    result += str(val)

def adv(regs, operand):
    operand = extr_combo_operand(operand, regs)
    numerator = regs[A]
    denominator = 2 ** operand
    regs[A] = int(numerator // denominator)

def bdv(regs, operand):
    operand = extr_combo_operand(operand, regs)
    numerator = regs[A]
    denominator = 2 ** operand
    regs[B] = int(numerator // denominator)

def cdv(regs, operand):
    operand = extr_combo_operand(operand, regs)
    numerator = regs[A]
    denominator = 2 ** operand
    regs[C] = int(numerator // denominator)

def bxl(regs, operand):
    regs[B] = regs[B] ^ operand

def bst(regs, operand):
    operand = extr_combo_operand(operand, regs)
    regs[B] = operand % 8

def bxc(regs, operand):
    regs[B] = regs[B] ^ regs[C]

def out(regs, operand):
    operand = extr_combo_operand(operand, regs)
    resout(operand % 8)

def printstate(regs, memory, ip):
        global result
        print(f"A: {str.rjust(str(regs[A]), 8)} B: {str.rjust(str(regs[B]), 8)} C: {str.rjust(str(regs[C]), 8)} Memory: {memory}, result: {result}")
        if (ip != -1):
            print(f"     {" "*(3*ip+5+35)}"+"^")

def do1(regs, memory):
    ip = 0
    global result
    result = ""
    steps = 0

    while ip < len(memory):
        steps += 1
        #printstate(regs, memory, ip)

        opcode = memory[ip]
        operand = memory[ip+1]

        if opcode == 0: # adv
            adv(regs, operand)
            ip += 2
        elif opcode == 1: # bxl
            bxl(regs, operand)
            ip += 2
        elif opcode == 2: # bst
            bst(regs, operand)
            ip += 2
        elif opcode == 3: # jnz
            if regs[A] != 0:
                ip = operand
            else:
                ip += 2
        elif opcode == 4: # bxc
            bxc(regs, operand)
            ip += 2
        elif opcode == 5: # out
            out(regs, operand)
            ip += 2
        elif opcode == 6: # bdv
            bdv(regs, operand)
            ip += 2
        elif opcode == 7: # cdv
            cdv(regs, operand)
            ip += 2
    
    return result, steps

def do2(regs, memory):
    nregs = regs.copy()
    nmemory = memory.copy()
    memstr = ",".join([str(x) for x in memory])
    
    # a is between 3 * 2**45 and 4 * 2**45 - 1 --> the 16th number is 0

    a = 4 * 2**45 - 1
    # a =  35184372088832 first 16 digits 
    # a = 281474976710655 last 16 digits 
    # a = 100000000000000
    # a = 300000000000000 below this one
    #a = 39999999999999

    # with open("output.txt", "w") as f:

    while True:
        # if a % 100000 == 0:
        nregs[A]= a
        result = ""
        res, steps = do1(nregs, nmemory)

        #f.write(f"with A = {a}; memory: {memory}; after {steps} steps; res: {res}\n")
        print(f"with A = {a}; memory: {memory}; after {steps} steps; res: {res}\n")

        # print(f"res vs memstr: {len(res)} vs {len(memstr)}")

        if len(res) == len(memstr):
            if res == memstr:
                print(f"Found a match: {a}")
                break


        a += 1

def run_with_a(Ax, prog):
    registers = {A: Ax, B: 0, C: 0}
    res, steps = do1(registers, prog)
    result = [int(x) for x in res.split(",")]
    return result


def do2new(regs, memory):
    matches = [0]
    # going backwards from the end of the program
    # first check the last digit, starting at 8^(num of the digit)

    i = 15
    # iterate from n-1 to 0 backwards
    while i >= 0:
        # check every 2^(3*i) input to see which will result in the correct last digit
        # after the previous matches
        print(f"Checking digit {i}")
        check_skips = 2 ** (3*i)
        nmatches = []
        
        for m in matches:
            # now check all possible inputs for the current digit
            for j in range(0, 8):
                # Ax will be each j * 2^(3*i) after m
                a = m + j * check_skips

                res = run_with_a(a, memory)
                # if the end of the result matches the end of the desired result, a match is nearer :)
                if res[i:] == memory[i:]:
                    nmatches.append(a)
        matches = nmatches
        i -= 1 
    
    return min(matches)



def run(Ax, Bx, Cx, prog):
    registers = {A: Ax, B: Bx, C: Cx}
    do1(registers, prog)
    printstate(registers, prog, -1)
    print(f"Result: {result}")
        
# still have to figure out how to look for local file in VS Code :(
input_file = r'd:\OneDrive\Documents\Projects\AoC\2024\advent-of-code-2024\17\input.txt'   

# run(0, 0, 9, [2,6])
# result = ""
# run(10, 0, 0, [5,0,5,1,5,4])
# result = ""
# run(2024, 0, 0, [0,1,5,4,3,0])
# result = ""
# run(0, 29, 0, [1,7])
# result = ""
# run(0, 2024, 43690, [4,0])
# result = ""

Ax, Bx, Cx, prog = load_prog(input_file)
registers = {"A": Ax, "B": Bx, "C": Cx}

t1 = time.time()
do1(registers, prog)
print(f"Result: {result}")
#0,2,5,2,0,2,2,6,1 -> not OK
#6,5,4,7,1,6,0,3,1 -> OK :)
t2 = time.time()

print(f"elapsed time: {(t2-t1)} seconds")

t1 = time.time()
Ax, Bx, Cx, prog = load_prog(input_file)
registers = {"A": Ax, "B": Bx, "C": Cx}

t1 = time.time()
# registers = {A: 2024, B: 0, C: 0}
# prog = [0,3,5,4,3,0]

minmatch = do2new(registers, prog)
print(f"Min match: {minmatch}")

# t2 = time.time()

print(f"elapsed time: {(t2-t1)} seconds")