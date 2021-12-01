#!/usr/bin/env python3

with open("input.txt") as f:
    data = f.read().splitlines()

data = list(map(int, data))


def count_number_of_depth_increases(data):
    result = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            result += 1
    return result

print("Answer Part 1")
print(count_number_of_depth_increases(data))
