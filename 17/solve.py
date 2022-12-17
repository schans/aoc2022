#!/usr/bin/env python3

import fileinput

# globals
W = 7
PM = 2022

# wind
I = []
IL = 0
IC = 0

# floor
R = set()
for i in range(W):
    R.add((i, 0))

# Pieces
P = [
    ((0, 0), (1, 0), (2, 0), (3, 0)),  # -
    ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)),  # +
    ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),  # L
    ((0, 0), (0, 1), (0, 2), (0, 3)),  # |
    ((0, 0), (0, 1), (1, 0), (1, 1))  # 8
]
PL = len(P)


for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    I = [1 if m == '>' else -1 for m in l]
    IL = len(I)


def dump(p=None):
    for h in range(RM+7, 0, -1):
        print(f"{h:4} |", end="")
        for x in range(W):
            if p and (x, h) in p:
                print('@', end="")
            elif (x, h) in R:
                print('#', end="")
            else:
                print('.', end="")
        print('|')
    print('     +-------+')


def move(p, dx, dy):
    return set((x+dx, y+dy) for (x, y) in p)


# drop the pieces
H = []
h = 0
for c in range(10_000):
    p = move(P[c % PL], 2, h+4)
    while True:
        # move wind
        dx = I[IC % IL]
        IC += 1
        np = move(p, dx, 0)
        if not np & R and all(0 <= x < W for (x, _) in np):
            p = np

        # move down
        np = move(p, 0, -1)
        if np & R:
            h = max(h, max(y for (_, y) in p))
            R |= p
            break

        p = np
    H.append(h)


# Find cycle
# oberservations :
# - tot moves is divisable by num blocks
# - cycle based on tot blocks modulo num blocks AND  tot moves module num moves
# - starting from R=X there is a cycle with DR=Y and DH=Z
#
# Formula
# - Max height =  (R // DR ) * DH + val_of( R % DR - 1)
dr = -1
dh = -1
for t in range(5, IL):
    # assume 4 points is enough..
    h1 = H[PM]
    h2 = H[PM+t]
    h3 = H[PM+t*2]
    h4 = H[PM+t*3]
    dh1 = h2 - h1
    dh2 = h3 - h2
    dh3 = h4 - h3
    if dh1 == dh2 == dh3:
        dh = dh1
        dr = t
        break

assert H[PM-1] == (PM // dr) * dh + H[PM % dr - 1]  # check formula works

tot = H[PM-1]
tot2 = (1_000_000_000_000 // dr) * dh + H[1_000_000_000_000 % dr - 1]

print(f"1: {tot}  2: {tot2}")
