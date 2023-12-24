import re
def get_points(card):
    my_nums = [int(num) for num in card[0].split()]
    winning_nums = [int(num) for num in card[1].split()]
    no_of_matched_cards = 0
    for num in my_nums:
        if num in winning_nums:
            no_of_matched_cards += 1
    if no_of_matched_cards == 0:
        return 0
    return 1 * (2 ** (no_of_matched_cards - 1))

def main():
    with open("./day4input.txt", "r") as file:
        input_data = file.read()
    cards = []
    for x in (re.match(r"^Card\s*\d+: (.*?) \| (.*)$", line) for line in input_data.splitlines()):
        cards.append([x.groups()[0],x.groups()[1]])
    total_points = 0
    for card in cards:
        total_points += get_points(card)
    print("ANSWER ==",total_points)
    
main()