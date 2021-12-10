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

counter = 0
for line, output in data:
    for segment in output:
        if len(segment) in (2, 3, 4, 7):
            counter += 1
print(counter)
