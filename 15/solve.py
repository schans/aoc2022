#!/usr/bin/env python3

import fileinput

# globals
y = 2_000_000

S = dict()
B = set()

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    p = l.split(':')
    sc = p[0].split(' at ')[1].split(', ')
    bc = p[1].split(' at ')[1].split(', ')

    sx = int(sc[0].split('=')[1])
    sy = int(sc[1].split('=')[1])
    bx = int(bc[0].split('=')[1])
    by = int(bc[1].split('=')[1])

    S[(sx, sy)] = (bx, by)


def range_merge(ranges, range):
    nr = []
    for r in ranges:
        if r[1] < range[0] - 1:
            nr.append(r)
        elif r[0] > range[1] + 1:
            nr.append(r)
        else:
            range = (min(r[0], range[0]), max(r[1], range[1]))
    nr.append(range)
    return nr


def get_ranges(y):
    ranges = []
    for s, b in S.items():
        dx, dy = abs(b[0] - s[0]), abs(b[1]-s[1])
        mhd = dx+dy
        ddy = abs(s[1] - y)

        if ddy > mhd:
            continue

        minx = s[0] - (mhd - ddy)
        maxx = s[0] + (mhd - ddy)
        ranges = range_merge(ranges, (minx, maxx))
    return ranges


def get_occupied(ranges, y):
    occ = set()
    for item in S.items():
        for (sx, sy) in item:
            if sy != y:
                continue
            for r in ranges:
                if r[0] <= sx <= r[1]:
                    occ.add(sx)
                    break
    return len(occ)


# part 1
ranges = get_ranges(y)
occ = get_occupied(ranges, y)
tot = sum([r[1]-r[0]+1 for r in ranges])

# part 2
freq = 0
for y in range(y * 2 + 1):
    ranges = get_ranges(y)
    # there is only 1 possible spot
    if len(ranges) == 2:
        x = max(ranges[0][0], ranges[1][0] - 1)
        freq = 4_000_000 * x + y
        break


print(f"Scores {tot-occ} {freq}")
