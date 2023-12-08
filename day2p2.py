from collections import Counter
from functools import reduce
from operator import mul, or_

thres = Counter({"red":12, "green":13, "blue":14})

tot_1 = 0
tot_2 = 0
with open("day2input.txt", "r") as f:
    for game in f:
        game_id, draws = game.strip().split(": ")
        game_id = int(game_id.split(" ")[1])
        draws = [[c.split(" ") for c in d.split(", ")] for d in draws.split("; ")]
        print("Aft Split Split")
        print(draws)
        draws = [Counter({c[1]:int(c[0]) for c in d}) for d in draws]
        print("Aft Counter")
        print(draws)
        # all -> returns true/1 if all items in the list are true
        tot_1 += all(d<=thres for d in draws) * game_id
        tot_2 += reduce(mul, reduce(or_, draws).values())
        

print(1, tot_1)
print(2, tot_2)

## MY METHOD:
# import re

# class Bag:
#     def __init__(self):
#         self.container = { "r" : 0, "b" : 0, "g" : 0}
        
#     def get_multiplication(self):
#         return self.container["r"] * self.container["g"] * self.container["b"]

# with open("day2input.txt", "r") as file:
#     input_data = file.read()
# input_data = input_data.splitlines()
# input_len = len(input_data)

# res = 0
# for i,line in enumerate(input_data):
#     bag = Bag()
#     draws = re.split(r'\s*;\s*',line)
#     for draw in draws:
#         colours = re.findall(r'\d+ [rgb]',draw)
#         for colour in colours:
#             count = re.findall(r'\d+',colour)
#             if int(count[0]) > bag.container[colour[-1]]:
#                 bag.container[colour[-1]] = int(count[0])
#     res += bag.get_multiplication()

# print(res)