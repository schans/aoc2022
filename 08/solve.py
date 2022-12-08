#!/usr/bin/env python3

import fileinput
from pprint import pprint

# counters
tot = 0
max = 0
data = []
R = C = 0
S = set()
DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))


for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    data.append([int(n) for n in l])
    R += 1

C = len(data[0])


def get_dist(s, d):
    (r, c) = s
    (dx, dy) = d
    x = r + dx
    y = c + dy
    dist = 1
    while x > 0 and y > 0 and x < R-1 and y < C-1:
        if data[x][y] < data[r][c]:
            x += dx
            y += dy
            dist += 1
        else:
            break
    return dist


def dump():
    CYAN = '\033[1m'
    ENDC = '\033[0m'
    print('-'*12)
    for r in range(0, R):
        for c in range(0, C):
            if (r, c) in S:
                print(f"{CYAN}{data[r][c]}{ENDC}", end=" ")
            else:
                print(data[r][c], end=" ")
        print()
    print('-'*12)


for r in range(0, R):
    m = -1
    for c in range(0, C):
        # print("cons", (r, c), data[r][c])
        if data[r][c] > m:
            m = data[r][c]
            S.add((r, c))
            # print("L", (r, c), m)
            if m == 9:
                break

    m = -1
    for c in range(C-1, -1, -1):
        if data[r][c] > m:
            m = data[r][c]
            S.add((r, c))
            # print("R", (r, c), m)
            if m == 9:
                break

for c in range(0, C):
    m = -1
    for r in range(0, R):
        # print("cons", (r, c), data[r][c])
        if data[r][c] > m:
            m = data[r][c]
            S.add((r, c))
            # print("T", (r, c), m)
            if m == 9:
                break

    m = -1
    for r in range(R-1, -1, -1):
        # print("cons", (r, c), data[r][c])
        if data[r][c] > m:
            m = data[r][c]
            S.add((r, c))
            # print("B", (r, c), )
            if m == 9:
                break
tot = len(S)


for s in S:
    (r, c) = s
    if r == 0 or r == R-1 or c == 0 or c == C-1:
        continue
    v = 1
    for d in DIRS:
        v *= get_dist(s, d)
    if v > max:
        max = v
        # print("max", max, "loc", s)


print(f"Scores {tot} {max}")
