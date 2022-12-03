#!/usr/bin/env python

import fileinput

# counters
tot = 0
tot2 = 0
p = pp = None


def score(c) -> int:
    e = ord(c)
    if e > 96:
        return e - 96
    else:
        return e - 38


for line in fileinput.input():

    l = line.strip()
    if not l:
        continue
    # part1
    mid = int(len(l)/2)
    f = set(l[0:mid])
    s = set(l[mid:])
    e = (f & s).pop()
    tot += score(e)

    # part2
    if p and pp:
        c = (p & pp & set(l)).pop()
        tot2 += score(c)
        p = pp = None
    else:
        pp = p
        p = set(l)

print(f"Scores {tot} {tot2}")
