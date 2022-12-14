#!/usr/bin/env python3

import fileinput

# globals
tot = 0
tot2 = 0
R = set()
S = set()
MAXY = 0
MINY = 0
MINX = 500
MAXX = 0

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

        R.add((x0, y0))
        R.add((x1, y1))

        if x0 < x1:
            for x in range(x0, x1):
                R.add((x, y0))
        elif x0 > x1:
            for x in range(x1, x0):
                R.add((x, y0))
        elif y0 < y1:
            for y in range(y0, y1):
                R.add((x0, y))
        elif y0 > y1:
            for y in range(y1, y0):
                R.add((x0, y))
        else:
            assert (False)

xs = set()
ys = set()
for (x, y) in R:
    xs.add(x)
    ys.add(y)
MINX = min(xs)
MINY = min(ys)
MAXX = max(xs)
MAXY = max(ys)


def dump():
    print("*" * 60)
    for y in range(0, MAXY + 4):
        for x in range(MINX-3, MAXX+3):
            if (x, y) in R:
                print('#', end="")
            elif (x, y) in S:
                print('o', end="")
            else:
                print('.', end="")
        print()
    print("*" * 60)


def drop(x=500, y=-1):
    rocks_y = set()
    for (rx, ry) in R:
        if rx == x and ry > y:
            rocks_y.add(ry)
    sand_y = set()
    for (sx, sy) in S:
        if sx == x and sy > y:
            sand_y.add(sy)

    if len(rocks_y) == 0 and len(sand_y) == 0:
        # fall down
        return False

    m = min(rocks_y | sand_y)

    if m == 0:
        # Reached top
        return False

    # dl = False
    if (x-1, m) not in R and (x-1, m) not in S:
        return drop(x-1, m)

    if (x+1, m) not in R and (x+1, m) not in S:
        return drop(x+1, m)

    S.add((x, m-1))
    return True


def draw(sx=500):
    S.add((sx, 0))
    for y in range(1, MAXY+3):
        for x in range(sx-y, sx+y+1):
            if (x+1, y-1) in S or (x, y-1) in S or (x-1, y-1) in S:
                if not (x, y) in R:
                    S.add((x, y))


# part 1
while drop(500):
    pass
tot = len(S)

# part 2
S = set()
for i in range(0, 550 + MAXY):
    R.add((i, MAXY+2))
draw()
tot2 = len(S)

print(f"1: {tot} 2: {tot2}")
