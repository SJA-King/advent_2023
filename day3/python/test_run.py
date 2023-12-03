from run import part_1, part_2
import random
import pytest


def replace_str_index(text, index=0, replacement=''):
    return f'{text[:index]}{replacement}{text[index + 1:]}'


@pytest.mark.parametrize('index', [0, 1, 2, 3, 4])
def test_part_1_above(index: int):
    random_number = random.randint(100, 999)
    test_string = '.....'
    test_string = replace_str_index(test_string, index, '+')

    test_data = [
        test_string,
        f".{random_number}.",
        "....."]

    assert random_number == part_1(test_data)


@pytest.mark.parametrize('index', [0, 1, 2, 3])
def test_part_1_above_two_digit(index: int):
    random_number = random.randint(10, 99)
    test_string = '.....'
    test_string = replace_str_index(test_string, index, '+')

    test_data = [
        test_string,
        f".{random_number}..",
        "....."]

    assert random_number == part_1(test_data)


@pytest.mark.parametrize('index', [1, 2, 3])
def test_part_1_above_one_digit(index: int):
    random_number = random.randint(1, 9)
    test_string = '.....'
    test_string = replace_str_index(test_string, index, '+')

    test_data = [
        test_string,
        f"..{random_number}..",
        "....."]

    assert random_number == part_1(test_data)


def test_part_1_aside():
    random_number = random.randint(100, 999)
    test_data = [
        '.....',
        f'-{random_number}.',
        '.....']

    assert random_number == part_1(test_data)

    test_data = [
        '.....',
        f'.{random_number}-',
        '.....']

    assert random_number == part_1(test_data)


@pytest.mark.parametrize('index', [0, 1, 2, 3, 4])
def test_part_1_below(index: int):
    random_number = random.randint(100, 999)
    test_string = '.....'
    test_string = replace_str_index(test_string, index, '%')

    test_data = [
        '.....',
        f'.{random_number}.',
        test_string]

    assert random_number == part_1(test_data)


@pytest.mark.parametrize('index', [0, 1, 2, 3])
def test_part_1_below_two_digit(index: int):
    random_number = random.randint(10, 99)
    test_string = '.....'
    test_string = replace_str_index(test_string, index, '+')

    test_data = [
        ".....",
        f".{random_number}..",
        test_string]

    assert random_number == part_1(test_data)


@pytest.mark.parametrize('index', [1, 2, 3])
def test_part_1_below_one_digit(index: int):
    random_number = random.randint(1, 9)
    test_string = '.....'
    test_string = replace_str_index(test_string, index, '+')

    test_data = [
        ".....",
        f"..{random_number}..",
        test_string]

    assert random_number == part_1(test_data)


@pytest.mark.parametrize('a_char', ['*', '@', '+', '-', '/', '=', '%', '$', '&'])
def test_part_1_all_special_chars_above(a_char: str):
    random_number = random.randint(100, 999)
    random_col = random.randint(0, 4)
    test_string = replace_str_index('.....', random_col, a_char)
    test_data = [
        test_string,
        f'.{random_number}.',
        '.....']

    assert random_number == part_1(test_data)


@pytest.mark.parametrize('a_char', ['*', '@', '+', '-', '/', '=', '%', '$', '&'])
def test_part_1_all_special_chars_below(a_char: str):
    random_number = random.randint(100, 999)
    random_col = random.randint(0, 4)
    test_string = replace_str_index('.....', random_col, a_char)
    test_data = [
        '.....',
        f'.{random_number}.',
        test_string]

    assert random_number == part_1(test_data)


def test_part_1_example():
    example_data = ["467..114..",
                    "...*......",
                    "..35..633.",
                    "......#...",
                    "617*......",
                    ".....+.58.",
                    "..592.....",
                    "......755.",
                    "...$.*....",
                    "664.598.."]

    assert 4361 == part_1(example_data)
