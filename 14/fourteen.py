print("Welcome to Day 14!")


from collections import defaultdict
from PIL import Image
import numpy as np

import time

class Robot:
    px, py, vx, vy = 0, 0, 0, 0

    def __init__(self, px, py, vx, vy):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy

    def __str__(self):
        return f"pos: {self.px}, {self.py}, vel: {self.vx}, {self.vy}"
        
        
def loadRobots(input_file):

    robots = []

    # input file is structured like this:
    # p=20,10 v=-23,-63
    # p=98,82 v=90,96
    # p=90,30 v=4,74
    # p=0,28 v=-73,8
    # p=88,102 v=51,-51
    # p=66,29 v=26,1
    # p=19,20 v=-61,-15

    # read input file
    with open(input_file, 'r') as infile:               
        while True:
            row = infile.readline().strip()
            if row == '' :
                break
            
            pos = [int(x) for x in row.split(' ')[0].split('=')[1].split(',')]
            vel = [int(x) for x in row.split(' ')[1].split('=')[1].split(',')]

            robots.append(Robot(pos[0], pos[1], vel[0], vel[1]))
        
    return robots

def move_robot(robot: Robot, steps, xsize, ysize):
    
    robot.px = (robot.px + steps*robot.vx) % xsize
    robot.py = (robot.py + steps*robot.vy) % ysize

    return robot

def move_all_robots_one_step(robots, xsize, ysize):
    for r in robots:
        move_robot(r, 1, xsize, ysize)
        
def print_robots(robots, xsize, ysize):
    map = [[0 for x in range(xsize)] for y in range(ysize)]

    for r in robots:
        map[r.py][r.px] = 1

    # remove stand-alone pixels from map
    for y in range(ysize):
        for x in range(xsize):
            if map[y][x] == 1:
                if y > 0 and y < ysize-1 and x > 0 and x < xsize-1:
                    if map[y-1][x] + map[y+1][x] + map[y][x-1] + map[y][x+1] + map[y-1][x-1] + map[y-1][x+1] + map[y+1][x-1] + map[y+1][x+1] == 0:
                        map[y][x] = 0

    array = np.array(map, dtype=np.uint8) * 255
    
    # create an image of the robots
    image = Image.fromarray(array, 'L') # for grayscale
    return image

def do1(robots, steps, xsize, ysize):
    total = 0
    q1, q2, q3, q4 = 0, 0, 0, 0

    for r in robots:
        move_robot(r, steps, xsize, ysize)
        print(f"pos: {r.px}, {r.py}")

        if r.px < xsize//2 and r.py < ysize//2: q1 += 1
        elif r.px > xsize//2 and r.py < ysize//2: q2 += 1
        elif r.px > xsize//2 and r.py > ysize//2: q3 += 1
        elif r.px < xsize//2 and r.py > ysize//2: q4 += 1

    print(f"q1: {q1}, q2: {q2}, q3: {q3}, q4: {q4}")
    print(f"total: {q1*q2*q3*q4}")


def do2(robots, xsize, ysize):

    c = 0
    while c < 10000:
        c += 1
        move_all_robots_one_step(robots, xsize, ysize)
    
        image = print_robots(robots, xsize, ysize)
        # save the image into a file named after the current step, padded with zeroes
        image.save(f'14/frames/frame_{str(c).zfill(4)}.png')
        
        
        
# still have to figure out how to look for local file in VS Code :(
input_file = r'd:\OneDrive\Documents\Projects\AoC\2024\advent-of-code-2024\14\input.txt'   

robots = loadRobots(input_file)

t1 = time.time()
# do1(robots, 100, 101, 103)
t2 = time.time()

print(f"elapsed time: {(t2-t1)} seconds")

t1 = time.time()
do2(robots, 101, 103)
t2 = time.time()

# print(f"elapsed time: {(t2-t1)} seconds")