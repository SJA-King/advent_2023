import os
from dataclasses import dataclass

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

    time_list = []
    distance_list = []

    for line in the_data:
        title, values = list(filter(None, line.split(":")))
        values = list(filter(None, values.split(" ")))
        print(f"Title = '{title}', Values = {values}")
        if title == "Time":
            time_list = values
        elif title == "Distance":
            distance_list = values
        else:
            raise Exception("SHOULDNT GET HERE!")

    total = 1
    for idx in range(len(time_list)):
        idx = int(idx)
        winning_strategies = 0
        for i_hold in range(int(time_list[idx])):
            print(f"Hold for {i_hold}ms")
            time_left = int(time_list[idx]) - i_hold
            distance_travelled = time_left * i_hold
            if distance_travelled > int(distance_list[idx]):
                winning_strategies += 1

        total *= winning_strategies

    # 861300
    return total


def part_2(the_data):
    print("Part 2")

    time_available = 0
    distance_to_beat = 0

    for line in the_data:
        title, values = list(filter(None, line.split(":")))
        value = ''.join(list(filter(None, values.split(" "))))
        print(f"Title = '{title}', Value = {values}")
        if title == "Time":
            time_available = int(value)
        elif title == "Distance":
            distance_to_beat = int(value)
        else:
            raise Exception("SHOULDNT GET HERE!")

    winning_strategies = 0
    for i_hold in range(time_available):
        print(f"Hold for {i_hold}ms")
        time_left = time_available - i_hold
        distance_travelled = time_left * i_hold
        if distance_travelled > distance_to_beat:
            print(f"Travelled Further ({distance_travelled})")
            winning_strategies += 1

    return winning_strategies
    # 28101347


def main():
    print("Day 6")

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