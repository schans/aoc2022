#!/usr/bin/env python3

import fileinput

# counters
X = 1
C = 0
M = [20, 60, 100, 140, 180, 220]
T = 0


def incr(c):
    global C, X, M, T
    for _ in range(c):
        if not C % 40:
            print()

        if X-1 <= C % 40 <= X+1:
            print("#", end="")
        else:
            print('.', end="")

        C += 1
        if C in M:
            T += C*X


for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    if l == 'noop':
        incr(1)
        continue

    d = int(l.split()[1])
    incr(2)
    X += d

print(f"Scores {T}")
