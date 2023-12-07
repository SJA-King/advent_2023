from run import part_1, part_2


def test_part_1():
    example_data = [
        "32T3K 765",
        "T55J5 684",
        "KK677 28",
        "KTJJT 220",
        "QQQJA 483"]

    assert 6440 == part_1(example_data)


def test_part_2():
    pass
    # example_data = [
    #     "Time:      7  15   30",
    #     "Distance:  9  40  200"]
    #
    # assert 71503 == part_2(example_data)
