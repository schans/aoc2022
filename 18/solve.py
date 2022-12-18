#!/usr/bin/env python3

import fileinput
from heapq import heappop, heappush

# globals
tot = 0
tot2 = 0

C = set()
A = set()
D = set()

min_x = 10
max_x = 0
min_y = 10
max_y = 0
min_z = 10
max_z = 0

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    (x, y, z) = tuple(map(int, l.split(",")))
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)
    min_z = min(min_z, z)
    max_z = max(max_z, z)
    C.add((x, y, z))

for (x, y, z) in C:
    tot += 6
    n = 0
    for (dx, dy, dz) in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
        if (x+dx, y+dy, z+dz) in C:
            n += 1
            tot -= 1
            if n == 6:
                # fully enclosed
                break
        else:
            # don't add edges to airs
            if min_x <= x+dx <= max_x and min_y <= y+dy <= max_y and min_z <= z+dz <= max_z:
                A.add((x+dx, y+dy, z+dz))


def enclosed(start, G):
    queue = []
    seen = set()
    queue.append((0, start))

    while queue:
        d, (x, y, z) = heappop(queue)
        if (x, y, z) in seen:
            continue
        seen.add((x, y, z))

        # path to outside, not eclosed volume
        if not (min_x <= x <= max_x and min_y <= y <= max_y and min_z <= z <= max_z):
            return False

        for (dx, dy, dz) in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            if not (x+dx, y+dy, z+dz) in G:
                heappush(queue, (d+1, (x+dx, y+dy, z+dz)))

    return seen


E = set()
for a in A:
    if a not in E:
        encl = enclosed(a, C)
        if encl:
            E |= encl

# remove side touching enclosed
tot2 = tot
for (x, y, z) in E:
    for (dx, dy, dz) in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
        if (x+dx, y+dy, z+dz) in C:
            tot2 -= 1

print(f"Scores {tot} {tot2}")
