#!/usr/bin/env python3

import re

with open("input.txt") as f:
    data = f.read().splitlines()

horizontal_position = 0
depth = 0
aim = 0
for command in data:
    cmd, value = command.split()
    value = int(value)

    if cmd == "forward":
        horizontal_position += value
        depth += aim * value

    elif cmd == "down":
        aim += value

    elif cmd == "up":
        aim -= value

print(depth * horizontal_position)
