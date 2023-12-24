import re
def get_matched_cards(card):
    my_nums = [int(num) for num in card[0].split()]
    winning_nums = [int(num) for num in card[1].split()]
    num_of_matched_cards = 0
    for num in my_nums:
        if num in winning_nums:
            num_of_matched_cards += 1
    return num_of_matched_cards

def update(counts_of_cards,card_num,list_of_cards):
    num_of_matched_cards = get_matched_cards(list_of_cards[card_num-1])
    for i in range(1,num_of_matched_cards+1):
        counts_of_cards[card_num + i] += counts_of_cards[card_num]

def main():
    with open("./day4input.txt", "r") as file:
        input_data = file.read()
    list_of_cards = []
    counts_of_cards = {}
    for x in (re.match(r"^Card\s*(\d+): (.*?) \| (.*)$", line) for line in input_data.splitlines()):
        list_of_cards.append([x.group(2),x.group(3)])
        counts_of_cards.update({int(x.group(1)):1})
    # iterates through all the cards by card numbers and updaets the next few number of cards
    for card_num in range(1,len(list_of_cards)+1):
        update(counts_of_cards,card_num,list_of_cards)
    print(counts_of_cards)
    print("ANSWER ==",sum(counts_of_cards.values()))
    
main()