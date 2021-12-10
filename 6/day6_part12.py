#!/usr/bin/env python3

with open("input.txt") as f:
    data = f.read().split(",")

data = list(map(int, data))

state = {number: data.count(number) for number in range(9)}


def step(state):
    number_of_zeros = 0
    for key, value in state.items():
        if key == 0:
            number_of_zeros = value
            continue
        state[key - 1] = value

    state[8] = number_of_zeros
    state[6] += number_of_zeros
    return state


for day in range(1, 257):
    state = step(state)
print(sum(state.values()))
