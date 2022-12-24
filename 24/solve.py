#!/usr/bin/env python3

import fileinput

from heapq import heappop, heappush

# counters
tot = 0
tot2 = 0

# 0 = empty
# u = 1, 1<<0
# r = 2, 1<<1
# d = 4  1<<2
# l = 8  1<<3
# wall = 16 1<<4

D = [(-1, 0), (0, 1), (1, 0), (0, -1)]
G = []
S = []


for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    r = []
    for c in l:
        if c == '.':
            r.append(0)
        elif c == '^':
            r.append(1 << 0)
        elif c == '>':
            r.append(1 << 1)
        elif c == 'v':
            r.append(1 << 2)
        elif c == '<':
            r.append(1 << 3)
        elif c == '#':
            r.append(1 << 4)
        else:
            assert False, f'unkown type: {c}'

    G.append(r)

C = len(G[0])
R = len(G)
CY = (R-2)*(C-2)
start = (0, 1)
end = (R-1, C-2)


def nextG(g):
    ng = []
    for r in range(R):
        ng.append([0] * C)

    for r in range(R):
        for c in range(C):
            t = g[r][c]

            if t == 16:
                # walls
                ng[r][c] = 16
            if t & 1 << 0:
                # up
                ng[1+(r - 2) % (R-2)][c] += 1 << 0
            if t & 1 << 1:
                # right
                ng[r][1+c % (C-2)] += 1 << 1
            if t & 1 << 2:
                # down
                ng[1+r % (R-2)][c] += 1 << 2
            if t & 1 << 3:
                # left
                ng[r][1+(c - 2) % (C-2)] += 1 << 3
    return ng


def dijkstra(start, end, offset):
    queue = []
    seen = set()
    queue.append((0, start))
    while queue:
        d, (r, c) = heappop(queue)
        if (r, c, d) in seen:
            continue
        seen.add((r, c, d))

        if (r, c) == end:
            return d

        for (dr, dc) in D:
            rr = r + dr
            cc = c + dc
            if 0 <= rr < R and S[(d+1+offset) % CY][rr][cc] == 0:
                heappush(queue, (d+1, (rr, cc)))
            # stay
            if S[(d+1+offset) % CY][r][c] == 0:
                heappush(queue, (d+1, (r, c)))

    raise ValueError("end not found?", d, r, c)


g = G.copy()
for i in range(CY):
    S.append(g)
    g = nextG(g)

for r in range(R):
    for c in range(C):
        assert G[r][c] == g[r][c], "create cycle failed"

tot = dijkstra(start, end, 0)
back = dijkstra(end, start, tot)
again = dijkstra(start, end, back+tot)
tot2 = tot + again + back
print(f"Scores {tot} {tot2}")
