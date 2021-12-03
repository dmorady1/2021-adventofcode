#!/usr/bin/env python3

import re

with open("input.txt") as f:
    data = f.read()#.splitlines()



horizontal_position = 0
depth = 0
aim = 0
for command in data.splitlines():
    cmd, value = command.split()
    value = int(value)

    if cmd == "forward":
        horizontal_position += value

    elif cmd == "down":
        depth += value

    elif cmd == "up":
        depth -= value

print(depth * horizontal_position)

# alternative with regex

def calculate_depth(data):
    depth_string = re.findall(r"(?:down.*|up.*)", data)

    depth_string = [re.sub(r"up\s", "-", depth  ) for depth in depth_string]
    depth_string = [re.sub(r"down\s", "+", depth  ) for depth in depth_string]
    depth = sum(map(int, depth_string))

    return depth

def calculate_horizontal_position(data):
    horizontal_position = re.findall(r"forward.*", data)

    horizontal_position = [re.findall(r"\d+", data)[0] for data in horizontal_position]

    return sum(map(int, horizontal_position))

def solve_part1(data):
    depth = calculate_depth(data)
    horizontal_position = calculate_horizontal_position(data)
    return  depth * horizontal_position

print(solve_part1(data))
