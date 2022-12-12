#!/usr/bin/env python3
import fileinput
from heapq import heappop, heappush

# globals
S = ((0, 0))
E = ((0, 0))
G = []

r = 0
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    G.append([ord(x) - 96 for x in l])
    for c in range(len(G[r])):
        if G[r][c] == -13:
            G[r][c] = 1
            S = ((r, c))
        elif G[r][c] == -27:
            G[r][c] = 26
            E = ((r, c))
    r += 1


def dijkstra(starts, end, G):
    queue = []
    seen = set()
    R = len(G)
    C = len(G[0])

    for start in starts:
        queue.append((0, start))

    while queue:
        d, (r, c) = heappop(queue)
        if (r, c) in seen:
            continue

        seen.add((r, c))
        if (r, c) == end:
            return d

        for (dr, dc) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            rr = r + dr
            cc = c + dc
            if 0 <= rr < R and 0 <= cc < C and G[rr][cc] - G[r][c] <= 1:
                heappush(queue, (d+1, (rr, cc)))

    raise ValueError("end not found?")


starts = []
for r in range(len(G)):
    for c in range(len(G[0])):
        if G[r][c] == 1:
            starts.append((r, c))


p1 = dijkstra([S], E, G)
p2 = dijkstra(starts, E, G)

print(f"Scores {p1} {p2}")
