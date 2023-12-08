import re
from collections import Counter

MAPPINGS = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 1,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}

def get_type(cards):
    counter = Counter()
    for ch in cards:
        counter.update(ch)
    
    keys = counter.keys()
    has_J = False
    for key in keys:
        if key == 'J':
            has_J = True
    
    if has_J:
        no_of_Js = counter['J']
        if not no_of_Js == 5:
            del counter['J']
            sorted_counter = counter.most_common()
            counter[sorted_counter[0][0]] += no_of_Js
    
    length = len(counter)
    counter = counter.most_common()
    # high card
    if length == 5:
        return 10000000000
    # one pair
    elif length == 4:
        return 20000000000
    # two pair
    elif length == 3 and counter[0][1] == 2:
        return 30000000000
    # three of a kind
    elif length == 3 and counter[0][1] == 3:
        return 40000000000
    # full house
    elif length == 2 and counter[0][1] == 3:
        return 50000000000
    # four of a kind
    elif length == 2 and counter[0][1] == 4:
        return 70000000000
    # five of a kind
    else:
        return 80000000000

def get_card_order(cards):
    ten = 100000000
    ret = 0
    for ch in cards:
        ret += ten * MAPPINGS[ch]
        ten //= 100
    return ret

def main():
    key_to_value = {}
    for line in input_data:
        data = line.split()
        key_to_value.update({data[0]:int(data[1])})

    worth_to_key = {}
    for key in key_to_value:
        worth = 0x0
        worth += get_type(key)
        worth += get_card_order(key)
        worth_to_key.update({worth:key})
    sorted_worth_to_key = dict(sorted(worth_to_key.items()))
    sorted_keys = sorted_worth_to_key.values()
    ret = 0
    for i,key in enumerate(sorted_keys):
        print(key)
        ret += (i+1) * key_to_value[key]
    print(ret)

with open("day7input.txt", "r") as file:
    input_data = file.read()
input_data = input_data.splitlines()
main()
