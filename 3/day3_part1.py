#!/usr/bin/env python3

with open("input.txt") as f:
    data = f.read().splitlines()


def find_most_common_bits(binarys):
    result = ""
    for column in range(len(binarys[0])):
        counts = {"0": 0, "1": 0}
        for row in range(len(binarys)):
            counts[binarys[row][column]] += 1

        result = result + "1" if counts["1"] > counts["0"] else result + "0"
    return result


gamma_rate = find_most_common_bits(data)
epsilon_rate = "".join("1" if x == "0" else "0" for x in gamma_rate)

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)
print("Solution part 1")
print(gamma_rate * epsilon_rate)
