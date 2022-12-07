#!/usr/bin/env python3

import fileinput

# counters
tot = 0
space = 70_000_000
free_min = 30_000_000
D = []


# root
root = {
    'name': "",
    'parent': {},
    'children': [],
    's': 0
}
D.append(root)
cur = root

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    if l.startswith('$ cd'):
        d = l[5:]
        if d == '/':
            pass
        elif d == '..':
            cur = cur['parent']
        else:
            new = {
                'name': d,
                'parent': cur,
                'children': [],
                's': 0
            }
            D.append(new)
            cur['children'].append(new)
            cur = new
    elif l.startswith('$ ls'):
        pass
    else:
        if not l.startswith('dir'):
            cur['s'] += int(l.split()[0])


# walk the walk and calc, the subdir sums
def calc_sum(c: dict) -> None:
    global tot
    st = c['s']
    for s in c['children']:
        if 't' not in s:
            calc_sum(s)
        st += s['t']
    c['t'] = st
    if st < 100_000:
        tot += st


calc_sum(root)

# part 2
to_free = free_min + root['t'] - space
d = root
for c in D:
    if c['t'] > to_free and c['t'] < d['t']:
        d = c


print(f"1. {tot} 2. {d['t']}")
