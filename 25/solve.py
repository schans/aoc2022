#!/usr/bin/env python3

import fileinput

# globals
tot = ''
sum = 0

D = {2: "2", 1: "1", 0: "0", -1: "-", -2: "="}


def snafu2dec(s):
    n = 0
    for i, c in enumerate(reversed(s)):
        m = 5 ** i
        if c == '=':
            n -= 2*m
        elif c == '-':
            n -= m
        else:
            n += int(c) * m
    return n


def dec2snafu(dec):
    snafu = ''
    while dec > 0:
        digit = dec % 5
        dec //= 5
        if digit > 2:
            digit -= 5
            dec += 1
        snafu += D[digit]
    return snafu[::-1]


for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    sum += snafu2dec(l)


tot = dec2snafu(sum)
print(f"Scores {tot}")
