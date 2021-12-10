#!/usr/bin/env python3

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg
#
with open("input.txt") as f:
    data = f.read().splitlines()

data = [
    [
        list(map(set, line.split("|")[0].split())),
        list(map(set, line.split("|")[1].split())),
    ]
    for line in data
]

line_dict = {"a": set(), "b": set(), "c": set(), "d": set(), "e": set(), "f": set()}


def get_symbols_for_line(line):
    line = sorted(line, key=lambda x: len(x))

    line_dict["a"] = line[1] - line[0]

    line_dict["c"] = line[0]
    line_dict["f"] = line[0]

    line_dict["b"] = line[2] - line[0]
    line_dict["d"] = line[2] - line[0]

    all_without_g = line_dict["d"] | line_dict["c"] | line_dict["a"]

    all_six_chars = [number_words for number_words in line if len(number_words) == 6]
    number_9 = [
        six_char for six_char in all_six_chars if len(six_char - all_without_g) == 1
    ][0]

    line_dict["g"] = number_9 - all_without_g
    line_dict["e"] = {"a", "b", "c", "d", "e", "f", "g"} - number_9

    e_g_a_set = line_dict["e"] | line_dict["g"] | line_dict["a"]
    number_2 = [
        number_words
        for number_words in line
        if len(number_words) == 5 and e_g_a_set.issubset(number_words)
    ][0]

    line_dict["c"] = number_2 & line_dict["c"]
    line_dict["f"] = line_dict["f"] - line_dict["c"]
    line_dict["d"] = line_dict["d"] & number_2

    line_dict["b"] -= line_dict["d"]

    return line_dict


def create_numbers_dict(line_dict):
    return {
        "".join(
            sorted(
                line_dict["a"]
                | line_dict["b"]
                | line_dict["c"]
                | line_dict["e"]
                | line_dict["f"]
                | line_dict["g"]
            )
        ): "0",
        "".join(sorted(line_dict["c"] | line_dict["f"])): "1",
        "".join(
            sorted(
                line_dict["a"]
                | line_dict["c"]
                | line_dict["d"]
                | line_dict["e"]
                | line_dict["g"]
            )
        ): "2",
        "".join(
            sorted(
                line_dict["a"]
                | line_dict["c"]
                | line_dict["d"]
                | line_dict["f"]
                | line_dict["g"]
            )
        ): "3",
        "".join(
            sorted(line_dict["b"] | line_dict["c"] | line_dict["d"] | line_dict["f"])
        ): "4",
        "".join(
            sorted(
                line_dict["a"]
                | line_dict["b"]
                | line_dict["d"]
                | line_dict["f"]
                | line_dict["g"]
            )
        ): "5",
        "".join(
            sorted(
                line_dict["a"]
                | line_dict["b"]
                | line_dict["d"]
                | line_dict["e"]
                | line_dict["f"]
                | line_dict["g"]
            )
        ): "6",
        "".join(sorted(line_dict["a"] | line_dict["c"] | line_dict["f"])): "7",
        "".join(
            sorted(
                line_dict["a"]
                | line_dict["b"]
                | line_dict["c"]
                | line_dict["d"]
                | line_dict["e"]
                | line_dict["f"]
                | line_dict["g"]
            )
        ): "8",
        "".join(
            sorted(
                line_dict["a"]
                | line_dict["b"]
                | line_dict["c"]
                | line_dict["d"]
                | line_dict["f"]
                | line_dict["g"]
            )
        ): "9",
    }


result = 0
for line, output in data:
    line_dict = get_symbols_for_line(line)
    numbers = create_numbers_dict(line_dict)
    output = list(map(lambda segment: "".join(sorted(segment)), output))
    result += int("".join(numbers[segment] for segment in output))

print(result)
