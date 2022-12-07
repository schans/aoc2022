#!/usr/bin/env python3

import fileinput

# counters
tot = 0
space = 70_000_000
free_min = 30_000_000
pwd = [""]
D = {}

path = ""
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    if l.startswith('$ cd'):
        d = l[5:]
        if d == '/':
            pwd = [""]
        elif d == '..':
            pwd.pop()
        else:
            pwd.append(d)

        path = "/".join(pwd)
        if not path in D:
            D[path] = 0

    elif l.startswith('$ ls'):
        pass
    else:
        if not l.startswith('dir'):
            s = int(l.split()[0])
            D[path] += s
            d = pwd.copy()
            d.pop()
            while d:
                D["/".join(d)] += s
                d.pop()


to_free = free_min + D[""] - space
c = D[""]
for d, s in D.items():
    if s < 100_000:
        tot += s
    if s > to_free and s < c:
        c = s

print(f"1. {tot} 2. {c}")
