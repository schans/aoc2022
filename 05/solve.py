#!/usr/bin/env python3

import fileinput
from copy import deepcopy

N = 0
si = []
mi = []


def tops(s):
    r = []
    for i in range(0, N):
        r.append(s[i].pop())
    return "".join(r)


# parse
for line in fileinput.input():
    l = line
    if not l:
        continue
    if l.startswith("  ") or l.startswith('['):
        si.append(l[0:-1])
    elif l.startswith(" 1"):
        N = int(l.strip()[-1])
    elif l.startswith('move'):
        mi.append(l.strip())

# gen stacks
S = [[] for _ in range(N)]
for s in reversed(si):
    for i in range(0, N):
        p = 1 + i*4
        if s[p] != " ":
            S[i].append(s[p])
S2 = deepcopy(S)

# exec moves
for m in mi:
    _, n, _, f, _, t = m.split()
    f = int(f) - 1
    t = int(t) - 1
    n = int(n)
    tmp = []
    for i in range(0, n):
        S[t].append(S[f].pop())
        tmp.append(S2[f].pop())

    for i in range(0, n):
        S2[t].append(tmp.pop())

print("1:", tops(S), "2:", tops(S2))
