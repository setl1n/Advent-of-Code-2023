import re
import sys
from math import lcm
sys.setrecursionlimit(100000)

def get_dir_idx(dir_idx,dir_mappings):
    if dir_idx + 1 == len(dir_mappings):
        return 0
    else: 
        return dir_idx + 1

def find_steps(step,input,mappings,dir_idx, dir_mappings):
    if (dir_idx == len(dir_mappings)):
        dir_idx = 0
    if (dir_mappings[dir_idx] == 'L'):
        output = mappings[input][0]
    elif(dir_mappings[dir_idx] == 'R'):
        output = mappings[input][1]
    if (output[2] == 'Z'):
        return step + 1
    return find_steps(step + 1, output, mappings,dir_idx + 1, dir_mappings)

def main(input_data):
    directions = input_data[0]
    directions = [ch for ch in directions]
    # input_data.pop(0)
    # input_data.pop(0)
    #NQT = (TXC, RVJ)

    mappings = {
        x[1] : (x[2],x[3])
        for x in (re.match(r'^(\w+)\s*=\s*\((\w+), (\w+)\)$',line) for line in input_data[2:])
    }
    #print(mappings)
    start_points = []
    for data in input_data:
        if not len(re.findall(r'(\w{2}A) =',data)) == 0:
            start_points.append(re.findall(r'(\w{2}A) =',data)[0])
    #     old working: :( get gud bruh
    #     key = re.findall(r'(.*) =', data)
    #     left = re.findall(r'\((.*),', data)
    #     right = re.findall(r', (.*)\)', data)
    #     mappings.update({key[0]:[left[0],right[0]]})
    
    steps_per_start_point = {start_points:0 for start_points in start_points}
    
    for start_point in start_points:
        steps_per_start_point[start_point] = find_steps(0,start_point,mappings,0, directions)
    print(lcm(*steps_per_start_point.values()))
    
with open("day8input.txt", "r") as file:
    input_data = file.read()
input_data = input_data.splitlines()

main(input_data)