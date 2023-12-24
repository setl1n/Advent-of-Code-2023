import re
import sys
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
    if (output == "ZZZ"):
        return step + 1
    return find_steps(step + 1, output, mappings,dir_idx + 1, dir_mappings)

def main(input_data):
    directions = input_data[0]
    directions = [ch for ch in directions]
    input_data.pop(0)
    input_data.pop(0)
    mappings = {}
    for data in input_data:
        key = re.findall(r'(.*) =', data)
        left = re.findall(r'\((.*),', data)
        right = re.findall(r', (.*)\)', data)
        mappings.update({key[0]:[left[0],right[0]]})
    input = "AAA"
    print(find_steps(0,input,mappings,0, directions))
    
with open("day8input.txt", "r") as file:
    input_data = file.read()
input_data = input_data.splitlines()

main(input_data)