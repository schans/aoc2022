#!/usr/bin/env python

import fileinput

# counters
tot = 0
tot2 = 0


def score(other, me):
    return (((me-other) * 3) + 4) % 9 + me


def calc(other, me):
    return (other + me - 1) % 3


for line in fileinput.input():
    other, me = [ord(x) - 65 for x in line.strip().split()]
    me -= 23
    tot += score(other, me)

    me = calc(other, me)
    tot2 += score(other, me)

print(f"Scores {tot} {tot2}")
