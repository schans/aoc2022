#!/usr/bin/env python

import fileinput

# counters
tot = 0
tot2 = 0


def score(other, me):
    d = me - other
    if d == 0:
        return 4 + me
    elif d == 1 or d == -2:
        return 7 + me
    else:
        return 1 + me


def calc(other, me):
    if me == 0:
        # lose
        me = other - 1
    elif me == 1:
        # draw
        me = other
    else:
        # win
        me = other + 1
    return me % 3


for line in fileinput.input():
    l = line.strip()
    other, me = [ord(x) - 65 for x in l.split()]
    if me > 4:
        me -= 23
    tot += score(other, me)

    me = calc(other, me)
    tot2 += score(other, me)

print(f"Scores {tot} {tot2}")
