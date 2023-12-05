import os


HERE = os.path.dirname(os.path.abspath(__file__))
EXAMPLE = os.path.join(HERE, "../example.txt")
EXAMPLE2 = os.path.join(HERE, "../example2.txt")
INPUT = os.path.join(HERE, "../input.txt")


def get_data(the_file: str):
    data = []
    with open(the_file, 'r') as it:
        for line in it.readlines():
            data.append(line.strip())

    return data


def part_1(the_data):
    print("Part 1")

    total = 0

    for line in the_data:
        # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        card, numbers = line.split("|")
        winning_numbers = card.split(" ")[2:]
        winning_numbers = list(filter(None, winning_numbers))
        print(f"Winning Numbers are {winning_numbers}")
        numbers_i_have = numbers.split(" ")
        numbers_i_have = list(filter(None, numbers_i_have))
        print(f"Numbers I have are {numbers_i_have}")

        same = set(numbers_i_have).intersection(set(winning_numbers))
        print(f"Same = {same}")

        if same:
            total += 2 ** (len(same) - 1)
            print(f"Total = {total}")

    return total


from dataclasses import dataclass

@dataclass
class ScratchCard:
    card_id: int
    winning_numbers: list
    numbers: list
    amount: int


def part_2(the_data):
    print("Part 2")
    all_cards = {}
    total_scratch_cards = 0

    for i in range(len(the_data)):
        all_cards[i + 1] = ScratchCard(card_id=i+1, winning_numbers=[], numbers=[], amount=1)

    for line_idx, line in enumerate(the_data):
        # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        card, numbers = line.split("|")
        card_split = list(filter(None, card.split(" ")))
        winning_numbers = card_split[2:]
        card_id = int(card_split[1].strip(":"))
        numbers_i_have = numbers.split(" ")
        numbers_i_have = list(filter(None, numbers_i_have))

        print(f"ID={card_id}, Winning Numbers={winning_numbers}, Numbers I have={numbers_i_have}")

        all_cards[card_id].winning_numbers = winning_numbers
        all_cards[card_id].numbers = numbers_i_have

        same = set(numbers_i_have).intersection(set(winning_numbers))

        if same:
            wins = len(same)
            print(f"Winner ({wins})! [{same}]")

            for i in range(wins):
                next_card_id = card_id + i + 1
                if next_card_id in all_cards:
                    all_cards[next_card_id].amount += all_cards[card_id].amount
                else:
                    pass

        total_scratch_cards += all_cards[card_id].amount

    return total_scratch_cards



def main():
    print("Day 4")

    # example_data = get_data(EXAMPLE)
    # result = part_1(example_data)
    # print(result)
    # #
    # input_data = get_data(INPUT)
    # result = part_1(input_data)
    # print(result)

    # example_2_data = get_data(EXAMPLE)
    # result = part_2(example_2_data)
    # print(result)
    #
    input_data = get_data(INPUT)
    result = part_2(input_data)
    print(result)


if __name__ == "__main__":
    main()