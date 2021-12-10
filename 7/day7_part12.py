#!/usr/bin/env python3

with open("input.txt") as f:
    data = f.read().split(",")

data = list(map(int, data))


costs = [sum( abs(number - i) for number in data) for i in range(min(data), max(data)+1)]
print(int(min(costs)))


costs = [sum( (1/2) * abs((number-i))*(abs(number-i)+1) for number in data) for i in range(min(data), max(data)+1)]

print(int(min(costs)))
