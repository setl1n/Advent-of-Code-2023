import re

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
        input_data = file.read().replace(' ', '')
    # commented old method, BOOO GET GOOD
    # time = int(''.join(re.match(r"Time:\s*(\d.*)",input_data[0])[1].split()))
    # distance = int(''.join(re.match(r"Distance:\s*(\d.*)",input_data[1])[1].split()))
    time = int(re.findall(r'\d+', input_data)[0])
    distance = int(re.findall(r'\d+', input_data)[1])
    time_to_dist = [time,distance]

    print("ANSWER ==", get_ways_to_win(time_to_dist))
    
main()