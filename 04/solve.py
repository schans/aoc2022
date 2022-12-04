#!/usr/bin/env python3

import fileinput

# counters
tot = 0
tot2 = 0


def setify(s):
    b, e = [int(x) for x in s.split('-')]
    return set(range(b, e + 1))


for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    l, r = l.split(',')
    l = setify(l)
    r = setify(r)

    if len(r-l) == 0 or len(l-r) == 0:
        tot += 1

    if not len(r-l) + len(l) == len(r) + len(l):
        tot2 += 1

print(f"Scores {tot} {tot2}")
