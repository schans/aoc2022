#!/usr/bin/env python3

import fileinput

# globals
tot = 0
tot2 = 0


# input layout
"""
 12
 3
45
6
"""

D = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

F = 0
P = (1, 1)

G = set()
B = set()

I = []
LH = {}

r = 1
m = True
for line in fileinput.input():
    l = line[:-1]
    if not l:
        m = False
        continue

    if not m:
        c = []
        for i in l:
            if i.isdigit():
                c.append(i)
            else:
                d = i
                n = int("".join(c))
                c = []
                I.append((n, d))
        n = int("".join(c))
        I.append((n, ''))
        continue

    lo = 10000
    hi = 0

    for c, x in enumerate(l):
        if x == '.':
            lo = min(lo, c+1)
            hi = max(hi, c+1)
            G.add((r, c+1))
        elif x == '#':
            lo = min(lo, c+1)
            hi = max(hi, c+1)
            B.add((r, c+1))
    LH[r] = (lo, hi)
    r += 1


def walk(p, f):
    for n, d in I:
        # print(f"step {n} in {D[f]} from {p}")
        # do steps
        for _ in range(n):
            (dr, dc) = D[f]
            (r, c) = p
            drr = dr + r
            dcc = dc + c

            if (drr, dcc) in G:
                p = (drr, dcc)
            elif (drr, dcc) in B:
                # print("blocked by ", drr, dcc)
                break
            else:
                # print("try wrap")
                w = p
                # track opposite
                while True:
                    (r, c) = w
                    drr = r - dr
                    dcc = c - dc
                    if not (drr, dcc) in B and not (drr, dcc) in G:
                        break
                    w = (drr, dcc)

                if w in B:
                    # print("blocked by ", w)
                    pass
                elif w in G:
                    # print(f"wrapped: {w}")
                    p = w
                else:
                    assert False, "wrap failed"

        # rotate
        if d == 'R':
            f = (f+1) % 4
        elif d == 'L':
            f = (f-1) % 4

    return p, f


def walk3d(p, f):
    for n, d in I:
        # print(f"step {n} in {D[f]} from {p}")
        # do steps
        for _ in range(n):
            (dr, dc) = D[f]
            (r, c) = p
            drr = dr + r
            dcc = dc + c

            if (drr, dcc) in G:
                p = (drr, dcc)
            elif (drr, dcc) in B:
                # print("blocked by ", drr, dcc)
                break
            else:
                # print("try face swap")
                (r, c) = p
                nf = None

                # Input layout
                if D[f] == (-1, 0):
                    # up
                    q = (c-1)//DIM  # grid starts at 1

                    relc = c - q * DIM
                    relc_f = DIM - relc + 1

                    if q == 0:
                        drr = relc + DIM
                        dcc = DIM + 1
                        nf = (0, 1)
                    elif q == 1:
                        drr = relc + 3 * DIM
                        dcc = 1
                        nf = (0, 1)
                    elif q == 2:
                        drr = 4 * DIM
                        dcc = relc
                        nf = (-1, 0)

                elif D[f] == (1, 0):
                    # down
                    q = (c-1)//DIM  # grid starts at 1

                    relc = c - q * DIM
                    relc_f = DIM - relc + 1

                    if q == 0:
                        drr = 1
                        dcc = relc + 2 * DIM
                        nf = (1, 0)
                    elif q == 1:
                        drr = relc + 3 * DIM
                        dcc = DIM
                        nf = (0, -1)
                    elif q == 2:
                        drr = relc + DIM
                        dcc = 2 * DIM
                        nf = (0, -1)

                elif D[f] == (0, 1):
                    # right
                    q = (r-1)//DIM  # grid starts at 1

                    relr = r - q * DIM
                    relr_f = DIM - relr + 1

                    if q == 0:
                        drr = relr_f + 2 * DIM
                        dcc = 2 * DIM
                        nf = (0, -1)
                    elif q == 1:
                        drr = DIM
                        dcc = relr + 2 * DIM
                        nf = (-1, 0)
                    elif q == 2:
                        drr = relr_f
                        dcc = 3 * DIM
                        nf = (0, -1)
                    elif q == 3:
                        drr = 3 * DIM
                        dcc = relr + DIM
                        nf = (-1, 0)

                elif D[f] == (0, -1):

                    # left
                    q = (r-1)//DIM  # grid starts at 1

                    relr = r - q * DIM
                    relr_f = DIM - relr + 1

                    if q == 0:
                        drr = relr_f + 2 * DIM
                        dcc = 1
                        nf = (0, 1)
                    elif q == 1:
                        drr = 2 * DIM + 1
                        dcc = relr
                        nf = (1, 0)
                    elif q == 2:
                        drr = relr_f
                        dcc = DIM + 1
                        nf = (0, 1)
                    elif q == 3:
                        drr = 1
                        dcc = relr + DIM
                        nf = (1, 0)

                # Example layout
                # if D[f] == (-1, 0):
                #     # up
                #     print("wrap up")
                #     q = (c-1)//DIM  # grid starts at 1

                #     relc = c - q * DIM
                #     relc_f = DIM - relc + 1

                #     if q == 0:
                #         drr = 1
                #         dcc = relc_f + 2 * DIM
                #         nf = (1, 0)
                #     elif q == 1:
                #         drr = relc
                #         dcc = 2 * DIM + 1
                #         nf = (0, 1)
                #     elif q == 2:
                #         drr = DIM + 1
                #         dcc = relc_f
                #         nf = (1, 0)
                #     elif q == 3:
                #         drr = relc_f + DIM
                #         dcc = 3 * DIM
                #         nf = (-1, 0)

                # elif D[f] == (1, 0):
                #     # down
                #     print("wrap down")
                #     q = (c-1)//DIM  # grid starts at 1

                #     relc = c - q * DIM
                #     relc_f = DIM - relc + 1

                #     if q == 0:
                #         drr = 3 * DIM
                #         dcc = relc_f + 2 * DIM
                #         nf = (0, -1)
                #     elif q == 1:
                #         drr = relc_f + 2 * DIM
                #         dcc = 2 * DIM + 1
                #         nf = (1, 0)
                #     elif q == 2:
                #         drr = 2 * DIM
                #         dcc = relc_f
                #         nf = (-1, 0)
                #     elif q == 3:
                #         drr = relc_f + DIM
                #         dcc = 1
                #         nf = (0, 1)

                # elif D[f] == (0, 1):
                #     # right
                #     print("wrap right")
                #     q = (r-1)//DIM  # grid starts at 1

                #     relr = r - q * DIM
                #     relr_f = DIM - relr + 1

                #     if q == 0:
                #         drr = relr_f + 2 * DIM
                #         dcc = 4 * DIM
                #         nf = (0, -1)
                #     elif q == 1:
                #         drr = 2 * DIM + 1
                #         dcc = relr_f + 3 * DIM
                #         nf = (1, 0)
                #     elif q == 2:
                #         drr = relr_f
                #         dcc = 3 * DIM
                #         nf = (0, -1)

                # elif D[f] == (0, -1):
                #     # left
                #     print("wrap left")
                #     q = (r-1)//DIM  # grid starts at 1

                #     relr = r - q * DIM
                #     relr_f = DIM - relr + 1

                #     if q == 0:
                #         print("q0")
                #         drr = DIM + 1
                #         dcc = relr_f + DIM
                #         nf = (1, 0)
                #     elif q == 1:
                #         print("q1", p)
                #         drr = 3 * DIM
                #         dcc = relr_f + 3 * DIM
                #         nf = (-1, 0)
                #     elif q == 2:
                #         print("q2")
                #         drr = 2 * DIM
                #         dcc = relr_f + DIM
                #         nf = (-1, 0)

                if (drr, dcc) in B:
                    # print("wrapped blocked by", (drr, dcc))
                    pass
                elif (drr, dcc) in G:
                    # print(f"wrapper: {p} to {(drr, dcc)}, {D[f]} to {nf}")
                    p = (drr, dcc)
                    f = D.index(nf)
                else:
                    assert False, "swap failed"

        # rotate
        if d == 'R':
            f = (f+1) % 4
        elif d == 'L':
            f = (f-1) % 4

    return p, f


P = (1, LH[1][0])
DIM = LH[1][1]//3

# part 1
p, f = walk(P, F)
tot = 1000 * p[0] + 4 * p[1] + f

# part 2
p, f = walk3d(P, F)
tot2 = 1000 * p[0] + 4 * p[1] + f

print(f"Scores {tot} {tot2}")
