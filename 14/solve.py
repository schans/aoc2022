#!/usr/bin/env python3

import fileinput

# globals
tot = 0
tot2 = 0
R = set()
S = set()
MAXY = 0

# parse
for line in fileinput.input():
    l = line
    if not l:
        continue

    ps = [p.strip() for p in l.split('->')]
    r = []
    for p in ps:
        x, y = p.split(',')
        r.append((int(x), int(y)))

    for i in range(len(r)-1):
        (x0, y0) = r[i]
        (x1, y1) = r[i+1]

        x0, x1 = sorted([x0, x1])
        y0, y1 = sorted([y0, y1])

        MAXY = max(MAXY, y0, y1)

        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                R.add((x, y))


def drop():
    b = R.copy()
    t = 0
    while True:
        x = 500
        y = 0
        while True:
            if y >= MAXY:
                # fell down
                return t
            if (x, y+1) not in b:
                y += 1
                continue
            if (x-1, y+1) not in b:
                x -= 1
                y += 1
                continue
            if (x+1, y+1) not in b:
                x += 1
                y += 1
                continue

            b.add((x, y))
            t += 1
            break


def draw():
    sx = 500
    S.add((sx, 0))
    for y in range(1, MAXY+3):
        for x in range(sx-y, sx+y+1):
            if (x+1, y-1) in S or (x, y-1) in S or (x-1, y-1) in S:
                if not (x, y) in R:
                    S.add((x, y))
    return len(S)


# part 1
tot = drop()

# part 2
S = set()
for i in range(0, 550 + MAXY):
    R.add((i, MAXY+2))
tot2 = draw()

print(f"1: {tot} 2: {tot2}")
