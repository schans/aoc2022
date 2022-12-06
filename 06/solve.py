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

    s = list(l)
    for i in range(0, len(s) - 3):
        q = set(s[i:i+4])
        if len(q) == 4:
            tot += i+4
            break

    for i in range(0, len(s) - 13):
        q = set(s[i:i+14])
        if len(q) == 14:
            tot2 += i+14
            break

print(f"Scores {tot} {tot2}")
