import re
from functools import reduce
from operator import __mul__

def get_ways_to_win(data_set):
    distance_need = data_set[1]
    time_given = data_set[0]
    min_time_to_hold = 0
    while min_time_to_hold <= time_given and min_time_to_hold * (time_given - min_time_to_hold) <= distance_need:
        min_time_to_hold += 1
    if (min_time_to_hold > time_given):
        return 0
    return time_given - 2 * min_time_to_hold + 1

def main():
    with open("./day6input.txt", "r") as file:
        input_data = file.read()
    input_data = input_data.splitlines()
    times = re.findall(r"(\d+)",input_data[0])
    distances = re.findall(r"(\d+)",input_data[1])
    times_to_dists = []
    for i in range(len(times)):
        times_to_dists.append([int(times[i]),int(distances[i])])
    ways_to_win = []
    for data_set in times_to_dists:
        ways_to_win.append(get_ways_to_win(data_set))
    print("ANSWER ==", reduce(__mul__,ways_to_win,1))
    
main()