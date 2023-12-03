import os


HERE = os.path.dirname(os.path.abspath(__file__))
EXAMPLE = os.path.join(HERE, "../example.txt")
INPUT = os.path.join(HERE, "../input.txt")


def get_data(the_file: str):
    data = []
    with open(the_file, 'r') as it:
        for line in it.readlines():
            data.append(line.strip())

    return data


def part_1(the_data):
    print("Part 1")

    parts = []

    for line_idx, line in enumerate(the_data):
        print(f"Line is {line}")
        a_number = ""
        indexes = []
        # if the number is '.....111' we lose it!
        for col_idx, i_char in enumerate(line):
            if i_char.isnumeric():
                a_number += i_char
                indexes.append(col_idx)
            else:
                if not a_number:
                    continue

                found_part = False
                col_first = indexes[0] - 1
                col_last = indexes[-1] + 1
                col = 0
                row = 0
                char_at_idx = 0

                # check the column before and after number
                for i_col in [col_first, col_last]:
                    for i_row in [line_idx - 1, line_idx, line_idx + 1]:
                        try:
                            char_at_idx = the_data[i_row][i_col]
                            if not char_at_idx.isnumeric() and char_at_idx != ".":
                                row = i_row
                                col = i_col
                                found_part = True
                                break
                        except IndexError:
                            pass

                if not found_part:
                    for i_row in [-1, 1]:
                        # check the rows above and below number
                        for i_col in range(col_first, col_last):
                            try:
                                char_at_idx = the_data[line_idx + i_row][i_col]
                                if not char_at_idx.isnumeric() and char_at_idx != ".":
                                    row = line_idx + i_row
                                    col = i_col
                                    found_part = True
                                    break
                            except IndexError:
                                pass

                if found_part:
                    print(f"A part = {a_number}, with Special: '{char_at_idx}' at ({row},{col})")
                    parts.append(int(a_number))

                a_number = ""
                indexes = []

    print(f"All Parts = {parts}")
    return sum(parts)
    # 540374 is too high apparently
    # 537832 is my actual answer





def part_2(the_data):
    print("Part 2")



def main():
    print("Day 3")

    # example_data = get_data(EXAMPLE)
    # result = part_1(example_data)
    # print(result)
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