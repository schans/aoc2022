#!/usr/bin/env python3

import fileinput
from functools import cmp_to_key

# globals
tot = 0
L = []


def comp(f, s):
    if isinstance(f, int) and isinstance(s, int):
        if f < s:
            return True
        elif f > s:
            return False
        else:
            return 'unknown'
    elif isinstance(f, int):
        return comp([f], s)
    elif isinstance(s, int):
        return comp(f, [s])
    else:
        for i, fe in enumerate(f):
            if i >= len(s):
                # out or right
                return False
            se = s[i]
            res = comp(fe, se)
            if res == 'unknown':
                continue
            else:
                return res
        if len(f) == len(s):
            # undecided
            return 'unknown'
        else:
            # out of left
            return True


def compare(f, s):
    if comp(f, s):
        return -1
    else:
        return 1


for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    L.append(eval(l))


# part 1
for i in range(len(L)//2):
    if comp(L[2*i], L[2*i+1]):
        tot += i + 1

# part 2
L.append([[6]])
L.append([[2]])
S = sorted(L, key=cmp_to_key(compare))
f = s = 0
for i, x in enumerate(S):
    if x == [[2]]:
        f = i + 1
    elif x == [[6]]:
        s = i + 1
        break

print(f"Scores {tot} {f*s}")


# Scores 5390 19261
