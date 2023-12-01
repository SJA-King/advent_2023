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
    total = 0
    for line in the_data:
        print(f"Line is {line}")
        numbers = list(filter(str.isdigit, line))
        print(f"Numbers are {numbers}")
        the_number = int(f"{numbers[0]}{numbers[-1]}")
        print(f"Number is {the_number}")
        total += the_number

    print(f"Total = {total}")

    return total


def get_names_in_line(line, names):
    names_in_line = {}

    for i_name in names.keys():
        if i_name in line:
            names_in_line[i_name] = line.index(i_name)

    return names_in_line


def get_new_line(line: str):
    names = {"one": 1,
             "two": 2,
             "three": 3,
             "four": 4,
             "five": 5,
             "six": 6,
             "seven": 7,
             "eight": 8,
             "nine": 9}
    names_in_line = get_names_in_line(line, names)
    while names_in_line:
        first_name = None
        first_idx = 9999
        for i_name, i_idx in names_in_line.items():
            if i_idx < first_idx:
                first_idx = i_idx
                first_name = i_name

        line = line.replace(first_name, str(names[first_name]), 1)

        names_in_line = get_names_in_line(line, names)

    return line


def part_2(the_data):
    print("Part 2")
    total = 0
    # new_lines = []

    for line in the_data:
        line = line.strip()
        print(f"Line is {line}")
        new_line = get_new_line(line)
        # new_lines.append(new_line)
        print(f"New Line is {new_line}")

        numbers = list(filter(str.isdigit, new_line))
        print(f"Numbers are {numbers}")
        the_number = int(f"{numbers[0]}{numbers[-1]}")
        print(f"Number is {the_number}")
        total += the_number

    print(f"Total = {total}")
    # for i in new_lines:
    #     print(i)

    return total


def main():
    print("Day 1")

    # example_data = get_data(EXAMPLE)
    # part_1(example_data)
    #
    # input_data = get_data(INPUT)
    # part_1(input_data)

    # example_2_data = get_data(EXAMPLE2)
    # part_2(example_2_data)

    input_data = get_data(INPUT)
    part_2(input_data)


if __name__ == "__main__":
    main()