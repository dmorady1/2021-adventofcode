#!/usr/bin/env python3

import re
from collections import defaultdict

with open("input.txt") as f:
    data = f.read().splitlines()


diagram = defaultdict(int)

for line in data:
    x1, y1, x2, y2 = map(int, re.findall(r"\d+", line))

    step_x = int((x2-x1)/abs(x2-x1)) if x2-x1 != 0 else 0
    step_y= int((y2-y1)/abs(y2-y1)) if y2-y1 != 0 else 0
    diagram[(x1,y1)] += 1
    diagram[(x2,y2)] += 1

    point = x1+step_x, y1+step_y
    while(point != (x2,y2)):
        diagram[point] += 1
        point = point[0] + step_x , point[1] + step_y


print(len([x for x in diagram.values() if x >=2]))
