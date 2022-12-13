#!/usr/bin/env python3

import fileinput
from functools import cmp_to_key

# globals
tot = 0
L = []


def comp(f, s):
    if isinstance(f, int) and isinstance(s, int):
        if f < s:
            return -1
        elif f > s:
            return 1
        else:
            return 0
    elif isinstance(f, int):
        return comp([f], s)
    elif isinstance(s, int):
        return comp(f, [s])
    else:
        for i, fe in enumerate(f):
            if i >= len(s):
                # out or right
                return 1
            se = s[i]
            res = comp(fe, se)
            if res == 0:
                continue
            else:
                return res
        if len(f) == len(s):
            return 0
        else:
            # out of left
            return -1


for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    L.append(eval(l))


# part 1
for i in range(len(L)//2):
    if comp(L[2*i], L[2*i+1]) == -1:
        tot += i + 1

# part 2
L.append([[6]])
L.append([[2]])
S = sorted(L, key=cmp_to_key(comp))
tot2 = 1
for i, x in enumerate(S):
    if x == [[2]] or x == [[6]]:
        tot2 *= i+1

print(f"Scores {tot} {tot2}")


# Scores 5390 19261
