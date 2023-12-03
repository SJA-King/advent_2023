import os


HERE = os.path.dirname(os.path.abspath(__file__))
EXAMPLE = os.path.join(HERE, "../example.txt")
EXAMPLE2 = os.path.join(HERE, "../example2.txt")
INPUT = os.path.join(HERE, "../input.txt")


def get_data(the_file: str):
    with open(the_file, 'r') as it:
        return it.readlines()


def part_1(the_data):
    print("Part 1")
    max_values = {"red": 12, "green": 13, "blue": 14}
    sum_of_ids = 0

    for line in the_data:
        valid_game = True
        line = line.strip()
        game, handfuls = line.split(":")
        print(f"{game} +++ Handfuls = {handfuls}")
        _, game_id = game.split(" ")
        print(f"ID = {game_id}")
        cubesets = handfuls.split(";")
        print(f"Cubesets :: {cubesets}")
        for i_set in cubesets:
            cubes = i_set.split(",")
            for i_cube in cubes:
                # print(i_cube)
                amount, colour = i_cube.lstrip().split(" ")
                colour = colour.lower()
                amount = int(amount)
                if amount > max_values[colour]:
                    valid_game = False

        if valid_game:
            sum_of_ids += int(game_id)

    return sum_of_ids


def part_2(the_data):
    print("Part 2")
    sum_of_ids = 0
    for line in the_data:
        min_cubes = {"red": 0, "green": 0, "blue": 0}
        line = line.strip()
        game, handfuls = line.split(":")
        print(f"{game} +++ Handfuls = {handfuls}")
        _, game_id = game.split(" ")
        print(f"ID = {game_id}")
        cubesets = handfuls.split(";")
        print(f"Cubesets :: {cubesets}")
        for i_set in cubesets:
            cubes = i_set.split(",")
            for i_cube in cubes:
                # print(i_cube)
                amount, colour = i_cube.lstrip().split(" ")
                colour = colour.lower()
                amount = int(amount)
                if amount > min_cubes[colour]:
                    min_cubes[colour] = amount

        values_multiplied = min_cubes["red"] * min_cubes["blue"] * min_cubes["green"]
        sum_of_ids += values_multiplied

    return sum_of_ids


def main():
    print("Day 2")

    # example_data = get_data(EXAMPLE)
    # result = part_1(example_data)
    # print(result)
    # #
    # input_data = get_data(INPUT)
    # result = part_1(input_data)
    # print(result)

    example_2_data = get_data(EXAMPLE)
    result = part_2(example_2_data)
    print(result)

    input_data = get_data(INPUT)
    result = part_2(input_data)
    print(result)


if __name__ == "__main__":
    main()