#!/usr/bin/env python3

import fileinput
from collections import defaultdict

# globals
tot = tot2 = 0

G = {}
B = {}
T = 30
NONZ = 0
MAXR = 0

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    words = l.split()
    v = words[1]
    r = int(words[4][5:-1])
    d = [i for i in "".join(words[9:]).split(',')]

    G[v] = {
        'd': d,
        'r': r
    }

    if r > 0:
        NONZ += 1
        MAXR += r

L = len(G.keys())


# part 1
B = defaultdict(lambda: -1)
Z = []
Z.append(('AA', 0, 0, []))
for k in range(30):
    NZ = []
    found = set()
    for (v, r,  s, opened) in Z:
        if len(opened) == NONZ:
            # all open
            NZ.append((v, r, s+r, opened))
            continue

        ns = s + r
        if v not in opened and G[v]['r'] > 0:
            # open
            nr = r + G[v]['r']
            no = opened.copy()
            no.append(v)
            NZ.append((v, nr, ns, no))

        for d in G[v]['d']:
            if ns > B[d]:
                B[d] = ns
                NZ.append((d, r, ns, opened.copy()))
    Z = NZ

tot = max([s for (v, r, s, o) in Z])

# part 2
B = defaultdict(lambda: -1)
Z = []
Z.append(('AA', 'AA', 0, 0, []))

for k in range(26):
    NZ = []

    for (v, e, r, s, opened) in Z:
        if len(opened) == NONZ:
            # all open
            NZ.append((v, e, r, s+r, opened))
            continue

        assert r < MAXR, "invalid rate"
        ns = s + r

        # 1. O & O
        if v not in opened and G[v]['r'] > 0 and e not in opened and G[e]['r'] > 0 and v != e:
            nr = r + G[v]['r'] + G[e]['r']
            no = opened.copy()
            no.append(v)
            no.append(e)
            NZ.append((v, e, nr, ns, no))

        # 2. O & M
        if v not in opened and G[v]['r'] > 0:
            nr = r + G[v]['r']
            no = opened.copy()
            no.append(v)

            for d in G[e]['d']:
                NZ.append((v, d, nr, ns, no.copy()))

        # 3 M & O
        if e not in opened and G[e]['r'] > 0:
            nr = r + G[e]['r']
            no = opened.copy()
            no.append(e)

            for d in G[v]['d']:
                NZ.append((d, e, nr, ns, no.copy()))

        # 4 M & M
        for dv in G[v]['d']:
            for de in G[e]['d']:
                if ns > B[(dv, de)]:
                    B[(dv, de)] = ns
                    NZ.append((dv, de, r, ns, opened.copy()))
        Z = NZ

tot2 = max([s for (v, e, r, s, o) in Z])

print(f"Scores {tot} {tot2}")
