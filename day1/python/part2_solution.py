import re
import os
HERE = os.path.dirname(os.path.abspath(__file__))
EXAMPLE = os.path.join(HERE, "../example.txt")
EXAMPLE2 = os.path.join(HERE, "../example2.txt")
INPUT = os.path.join(HERE, "../input.txt")

with open(INPUT, "r") as input:
    lines = input.readlines()
    total = 0
    number_words = (
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    )
    digits = (
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    )
    words_to_digits = dict(zip(number_words, digits))
    all_matches = []
    for line in lines:
        orig_line = line
        pattern = r"(?=(" + "|".join(number_words + digits) + "))"
        matches = re.findall(pattern, line)
        found = []
        for match in matches:
            found.append(
                words_to_digits.get(match) if match in words_to_digits.keys() else match
            )
        all_matches.append(''.join(matches))
        first_digit = found[0]
        last_digit = found[-1]
        line_value = int(first_digit + last_digit)
        print(
            f"Brought Forward: {total}\n Original: {line} Just Numbers: {''.join(matches)}\n Found: {found}\n Number: {line_value}\n"
        )
        total += line_value

print(f"Final Total: {total}")

# for i_match in all_matches:
#     print(i_match)