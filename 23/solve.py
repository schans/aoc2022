#!/usr/bin/env python3

import fileinput

# globals
tot = 0
tot2 = 0

E = []

# from North CW
A = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
# N, S, W, E
D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
FD = 0

r = 0
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    for c, x in enumerate(l):
        if x == '#':
            E.append((r, c))
    r += 1


def dump(e):
    for r in range(12):
        l = []
        for c in range(14):
            if (r, c) in e:
                l.append('#')
            else:
                l.append('.')
        print("".join(l))


for k in range(1000):
    PP = []
    for _, (r, c) in enumerate(E):
        # default propose same
        PP.append((r, c))

        neigh = False
        for (dr, dc) in A:
            if (dr + r, dc + c) in E:
                neigh = True
                continue

        if not neigh:
            continue

        for i in range(4):
            (dr, dc) = D[(i+FD) % 4]

            move = True
            if dc == 0:
                # up or down
                for d in [-1, 0, 1]:
                    if (r+dr, c+dc + d) in E:
                        move = False
                        break
            elif dr == 0:
                # left or righ
                for d in [-1, 0, 1]:
                    if (r+dr+d, c+dc) in E:
                        move = False
                        break
            else:
                assert False, "unknown dir"
                pass

            if move:
                PP[-1] = (r+dr, c+dc)
                break

    assert len(E) == len(PP), "lost an elf"

    # phase 2
    seen = set()
    dup = set()
    dup = [x for _, x in enumerate(PP) if x in seen or seen.add(x)]

    moved = False
    for i, e in enumerate(PP):
        if e not in dup:
            if E[i] != PP[i]:
                moved = True
            E[i] = PP[i]

    FD = (FD+1) % 4
    if not moved:
        break

    if k == 9:
        rmin = cmin = 1000
        rmax = cmax = 0
        for r, c in E:
            rmin = min(rmin, r)
            cmin = min(cmin, c)
            rmax = max(rmax, r)
            cmax = max(cmax, c)

        tot = (rmax-rmin+1) * (cmax-cmin+1) - len(E)

tot2 = k + 1

print(f"Scores {tot} {tot2}")
