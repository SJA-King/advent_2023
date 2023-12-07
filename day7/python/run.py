import os
from dataclasses import dataclass
from enum import Enum, auto
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
EXAMPLE = os.path.join(HERE, "../example.txt")
INPUT = os.path.join(HERE, "../input.txt")


def get_data(the_file: str):
    data = []
    with open(the_file, 'r') as it:
        for line in it.readlines():
            data.append(line.strip())

    return data


card_weighting = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "J": 9,
    "T": 8,
    "9": 7,
    "8": 6,
    "7": 5,
    "6": 4,
    "5": 3,
    "4": 2,
    "3": 1,
    "2": 0
}


class HandTypes(Enum):
    FIVE_KIND = 6
    FOUR_KIND = 5
    FULL_HOUSE = 4
    THREE_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0
    NULL = -1


@dataclass
class Hand:
    cards: str
    bid: int
    rank: int
    hand_type: HandTypes

    def __post_init__(self):
        self.c_cards = Counter(self.cards)

    def winning(self):
        return self.bid * self.rank

    def set_hand_type(self):
        # Five of a kind, where all five cards have the same label: AAAAA
        # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
        # Three of a kind, where three cards have the same label, and the remaining two cards are each different from
        # any other card in the hand: TTT98
        # Two pair, where two cards share one label, two other cards share a second label, and the remaining card
        # has a third label: 23432
        # One pair, where two cards share one label, and the other three cards have a different label from the pair
        # and each other: A23A4
        # High card, where all cards' labels are distinct: 23456
        if self.is_five_kind():
            self.hand_type = HandTypes.FIVE_KIND
        elif self.is_four_kind():
            self.hand_type = HandTypes.FOUR_KIND
        elif self.is_full_house():
            self.hand_type = HandTypes.FULL_HOUSE
        elif self.is_three_kind():
            self.hand_type = HandTypes.THREE_KIND
        elif self.is_two_pair():
            self.hand_type = HandTypes.TWO_PAIR
        elif self.is_one_pair():
            self.hand_type = HandTypes.ONE_PAIR
        else:
            self.hand_type = HandTypes.HIGH_CARD
        # else:
        #     raise Exception("SHOULDNT GET HERE!")

    def is_five_kind(self) -> bool:
        if len(self.c_cards) == 1:
            # print(f"Five of a Kind!")
            return True
        return False

    def is_four_kind(self) -> bool:
        for i_card in self.c_cards.values():
            if i_card == 4:
                # print(f"Four of a Kind!")
                return True
        return False

    def is_full_house(self) -> bool:
        if len(self.c_cards) != 2:
            return False
        for i_card in self.c_cards.values():
            if 2 < i_card < 4:
                # print(f"Full House!")
                return True
        return False

    def is_three_kind(self) -> bool:
        for i_card in self.c_cards.values():
            if i_card == 3:
                # print(f"Three of a Kind!")
                return True
        return False

    def is_two_pair(self) -> bool:
        if len(self.c_cards) != 3:
            return False
        for i_card in self.c_cards.values():
            if i_card > 2:
                return False
        # print("Two Pair!")
        return True

    def is_one_pair(self) -> bool:
        if len(self.c_cards) == 4:
            # print("One Pair!")
            return True
        return False


def part_1(the_data):
    print("Part 1")

    hands = []

    for line in the_data:
        hand, bid = line.split(" ")
        hands.append(Hand(cards=hand, bid=int(bid), rank=0, hand_type=HandTypes.NULL))

    print(f"Hands = {hands}")

    hands_of_types = {
        HandTypes.FIVE_KIND: [],
        HandTypes.FOUR_KIND: [],
        HandTypes.FULL_HOUSE: [],
        HandTypes.THREE_KIND: [],
        HandTypes.TWO_PAIR: [],
        HandTypes.ONE_PAIR: [],
        HandTypes.HIGH_CARD: []
    }

    for hand_idx, a_hand in enumerate(hands):
        a_hand.set_hand_type()
        hands_of_types[a_hand.hand_type].append(a_hand)
        print(a_hand)

    hands_in_order = []

    temp_list = []
    for high_card in hands_of_types[HandTypes.HIGH_CARD]:
        if len(temp_list) == 0:
            temp_list.append(high_card)
        else:
            for i_card in temp_list:
                pass
                # TODO something like below
                # for i in range(5):
                #     if card_weighting[i_card[i]] == card_weighting[high_card[i]]:
                #         continue
                #     else:
                #         if card_weighting[i_card[i]] > card_weighting[high_card[i]]:
                #             temp_list = [i_card] + temp_list
                #
                #         if card_weighting[i_card[i]] < card_weighting[high_card[i]]:
                #             temp_list += temp_list





    winning_scores = 0

    for a_hand_idx, a_hand in enumerate(hands_in_order):
        a_hand.rank = a_hand_idx + 1
        winning_scores += a_hand.winning()

    return winning_scores


def part_2(the_data):
    print("Part 2")


def main():
    print("Day 7")

    example_data = get_data(EXAMPLE)
    result = part_1(example_data)
    print(result)

    # input_data = get_data(INPUT)
    # result = part_1(input_data)
    # print(result)

    # example_2_data = get_data(EXAMPLE)
    # result = part_2(example_2_data)
    # print(result)
    #
    # input_data = get_data(INPUT)
    # result = part_2(input_data)
    # print(result)


if __name__ == "__main__":
    main()
