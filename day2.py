import re
CUBES = {
    "r" : 12,
    "g" : 13,
    "b" : 14
}
with open("day2input.txt", "r") as file:
    input_data = file.read()
input_data = input_data.splitlines()
input_len = len(input_data)

res = 0
for i,line in enumerate(input_data):
    possible = True
    draws = re.split(r'\s*;\s*',line)
    for draw in draws:
        colours = re.findall(r'\d+ [rgb]',draw)
        for colour in colours:
            count = re.findall(r'\d+',colour)
            if int(count[0]) > CUBES[colour[-1]]:
                possible = False
    if possible:
        res += i + 1

print(res)