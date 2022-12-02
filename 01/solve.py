#!/usr/bin/env python

import fileinput

# counters
cur = 0
cals = list()

for line in fileinput.input():
    l = line.strip()
    if not l:
        cals.append(cur)
        cur = 0
        continue

    cur += int(line.strip())

cals.sort()
print(f"Most cals {cals[-1]} {cals[-1]+cals[-2]+cals[-3]}")
