#!/usr/bin/env python3

import fileinput

# globals
tot = 0
tot2 = 0

W = 7
I = []
IL = 0
IC = 0

PC = 0
PM = 2022


R = set()
# floor
for i in range(W):
    R.add((i, 0))

RM = 0
SC = 0


for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    I = list(l)
    IL = len(I)

# Pieces
RT = []
RT.append(((0, 0), (1, 0), (2, 0), (3, 0)))  # -
RT.append(((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)))  # +
RT.append(((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)))  # L
RT.append(((0, 0), (0, 1), (0, 2), (0, 3)))  # |
RT.append(((0, 0), (0, 1), (1, 0), (1, 1)))  # 8


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


def move(P, dx, dy):
    moved = set()
    for (x, y) in P:
        moved.add((x+dx, y+dy))
    return moved


# helper set for finding modulo
F = set()

while PC < PM:
    t = PC % len(RT)
    PC += 1
    p = move(RT[t], 2, RM+4)

    # print to find cycle
    print(PC, RM, IC, t, IC % IL, (t, IC % IL) in F)
    F.add((t, IC % IL))

    down = False  # move first then down
    stopped = False
    while not stopped:
        if down:
            down = False
            for (x, y) in p:
                if (x, y-1) in R:
                    stopped = True
                    break

            if stopped:
                for (x, y) in p:
                    R.add((x, y))
                    RM = max(RM, y)
                p = set()
                break

            # move down
            p = move(p, 0, -1)
        else:
            # move wind
            down = True
            dx = 0

            d = I[IC % IL]
            if d == '<':
                dx = -1
            elif d == '>':
                dx = 1
            else:
                assert False, f"dir? {d}"

            IC += 1
            np = move(p, dx, 0)
            blocked = False
            for (x, y) in np:
                if (x, y) in R or x < 0 or x >= W:
                    blocked = True
                    break

            if not blocked:
                p = np


# oberservations :
# - tot moves is divisable by num blocks
# - cycle based on tot blocks modulo num blocks AND  tot moves module num moves
# - starting from R=X there is a cycle with DR=Y and DH=Z
#
# - Max height =  (R // DR ) * DH + val_of( R % DR + 1)

print("Example")
DR = 35
DH = 53
R = 2022
P1 = R % DR + 1  # 28 rocks
P1_VAL = 47  # 28 rock height
print("Example1", (R//DR) * DH + P1_VAL)
R = 1_000_000_000_000
P1 = R % DR + 1  # 16 rocks
P1_VAL = 25  # 16 rocks height
print("Example2", (R//DR) * DH + P1_VAL)


DR = 1740
DH = 2681
R = 2022
P1 = R % DR + 1  # 283 rocks
P1_VAL = 433  # 283 rock height
print("part1", (R//DR) * DH + P1_VAL)
R = 1_000_000_000_000
P1 = R % DR + 1  # 1181 rocks
P1_VAL = 1799  # 1181 rocks height
print("part2", (R//DR) * DH + P1_VAL)
