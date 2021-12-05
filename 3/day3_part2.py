#!/usr/bin/env python3

from typing import Callable


with open("input.txt") as f:
    data = f.read().splitlines()

def find_common_bit(data:list[str], comparison: Callable, index: int):
    counts = {"0": 0, "1": 0}
    for bits in data:
        counts[bits[index]] += 1
    return comparison(counts["0"], counts["1"])


def find_rating(data:list[str], comparison_fn: Callable):
    data = data.copy()
    rating = ""
    for index in range(len(data[0])):
        if len(data) == 1:
            return rating + data[0][index::]

        rating += find_common_bit(data, comparison_fn, index)
        data = [bits for bits in data if bits.startswith(rating)]
    return rating

most_common_fn = lambda zero_count, one_count: "1" if one_count >= zero_count else "0"
least_common_fn = lambda zero_count, one_count: "0" if zero_count <= one_count else "1"

oxygen_generator_rating = find_rating(data, most_common_fn)
co2_scrubber_rating = find_rating(data, least_common_fn)

print("Solution 2")
print(int(oxygen_generator_rating, 2) * int(co2_scrubber_rating,2))
