from run import part_1, part_2


def test_part_1():
    example_data = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet"]

    assert 142 == part_1(example_data)


def test_part_2():
    example_data = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen"]

    assert 281 == part_2(example_data)
