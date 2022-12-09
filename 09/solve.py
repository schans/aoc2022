#!/usr/bin/env python3

import fileinput

# counters
SS = 10  # 2  # snake length
T = set()
S = []
_ = [S.append((0, 0)) for _ in range(SS)]

DIRS = {
    'U': (-1, 0),
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1)
}


def dump(trail=False):
    print('-'*24)
    D = 15
    for x in range(-1*D, D):
        for y in range(-1*D, D):
            if x == 0 and y == 0:
                print("s", end="")
            elif trail and (x, y) in T:
                print("#", end="")
            else:
                for i in range(SS):
                    snake = False
                    if S[i] == (x, y):
                        print(i, end="")
                        snake = True
                        break
                if not snake:
                    print(".", end="")
        print()


for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    d, s = l.split()
    (dx, dy) = DIRS[d]
    s = int(s)

    for _ in range(s):
        # move head
        (x, y) = S[0]
        x += dx
        y += dy
        S[0] = (x, y)

        # move segments
        for i in range(1, SS):
            (hx, hy) = S[i-1]
            (tx, ty) = S[i]
            sx = hx - tx
            sy = hy - ty
            if (sx, sy) not in [(0, 0), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
                if sx != 0:
                    tx += sx//abs(sx)
                if sy != 0:
                    ty += sy//abs(sy)
            S[i] = (tx, ty)
        T.add(S[SS-1])

# dump(True)
print(f"Scores {len(T)}")
