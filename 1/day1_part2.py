#!/usr/bin/env python3

with open("test.txt") as f:
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


def count_number_of_depth_increases_sliding(data, window_size=3):
    sum_list = [sum(data[i:i+window_size]) for i in range(len(data)) if  i+window_size <= len(data)]
    return count_number_of_depth_increases(sum_list)

print("Answer Part 2")
print(count_number_of_depth_increases_sliding(data))

# alternative
def count_number_of_depth_increases_sliding_window(data, window_size=3):
    result = 0
    prev = sum(data[0:window_size])
    for i in range(1, len(data)):
        if i+window_size-1 >= len(data):
            return result
        new = sum(data[i:i+window_size])
        if new > prev:
            result +=1
        prev = new
    return result

print("Answer Part 2")
print(count_number_of_depth_increases_sliding_window(data))

