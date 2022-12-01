#!/usr/bin/env python

import fileinput

# counters
cals = list()

# store prev values
for line in fileinput.input():
    l = line.strip()
    if not l:
        cals.append(cur)
        cur = 0
        continue

    cur += int(line.strip())

cals.sort()
print(f"Most first: {cals[-1]}, second: {cals[-1]+cals[-2]+cals[-3]}")
