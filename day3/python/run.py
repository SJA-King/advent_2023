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

    sum_of_parts = 0

    for line_idx, line in enumerate(the_data):
        line = line.strip()
        print(f"Line is {line}")
        a_number = ""
        indexes = []
        for col_idx, i_char in enumerate(line):
            if i_char.isnumeric():
                a_number += i_char
                indexes.append(col_idx)
                # print(i_char)
            else:
                if not a_number:
                    continue

                # print(f"A Number = {a_number}")
                found_part = False
                col_first = indexes[0] - 1
                col_last = indexes[-1] + 1

                # check the column before number
                for i_row in [line_idx - 1, line_idx, line_idx + 1]:
                    try:
                        char_at_idx = the_data[i_row][col_first]
                        if not char_at_idx.isnumeric() and char_at_idx != ".":
                            # print(f"Found Special Char {char_at_idx}")
                            found_part = True
                    except IndexError:
                        pass

                # check the row above number
                for i_col in range(col_first, col_last):
                    try:
                        char_at_idx = the_data[line_idx - 1][i_col]
                        if not char_at_idx.isnumeric() and char_at_idx != ".":
                            # print(f"Found Special Char {char_at_idx}")
                            found_part = True
                    except IndexError:
                        pass

                # check row below number
                for i_col in range(col_first, col_last):
                    try:
                        char_at_idx = the_data[line_idx + 1][i_col]
                        if not char_at_idx.isnumeric() and char_at_idx != ".":
                            # print(f"Found Special Char {char_at_idx}")
                            found_part = True
                    except IndexError:
                        pass

                # check coloumn after number
                for i_row in [line_idx - 1, line_idx, line_idx + 1]:
                    try:
                        char_at_idx = the_data[i_row][col_last]
                        if not char_at_idx.isnumeric() and char_at_idx != ".":
                            # print(f"Found Special Char {char_at_idx}")
                            found_part = True
                    except IndexError:
                        pass

                if found_part:
                    print(f"A part = {a_number}")
                    sum_of_parts += int(a_number)

                a_number = ""
                indexes = []

    return sum_of_parts





def part_2(the_data):
    print("Part 2")



def main():
    print("Day 3")

    example_data = get_data(EXAMPLE)
    result = part_1(example_data)
    print(result)
    # #
    input_data = get_data(INPUT)
    result = part_1(input_data)
    print(result)

    # example_2_data = get_data(EXAMPLE)
    # result = part_2(example_2_data)
    # print(result)
    #
    # input_data = get_data(INPUT)
    # result = part_2(input_data)
    # print(result)


if __name__ == "__main__":
    main()