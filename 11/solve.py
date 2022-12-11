#!/usr/bin/env python3

from collections import deque
import fileinput

from copy import deepcopy

# counters
M = []
M2 = []


def play(mks, n, div, red):
    for _ in range(n):
        for m in mks:
            while len(m['it']):
                m['in'] += 1
                old = m['it'].popleft()
                new = (eval(m['op'])//div) % red
                if new % m['div']:
                    mks[m['f']]['it'].append(new)
                else:
                    mks[m['t']]['it'].append(new)


def score(mks):
    p1s = []
    for m in mks:
        p1s.append(m['in'])
    p1s = sorted(p1s)
    return p1s[-1]*p1s[-2]


for line in fileinput.input():
    l = line.strip()
    if l.startswith("Monkey"):
        M.append({
            'it': deque(),
            'op': '',
            'div': -1,
            't': -1,
            'f': -1,
            'in': 0
        })
    elif l.startswith("Starting"):
        p = l.split(':')
        for n in p[1].split(','):
            M[-1]['it'].append(int(n.strip()))
    elif l.startswith('Operation'):
        M[-1]['op'] = l.split('=')[1].strip()
    elif l.startswith('Test'):
        M[-1]['div'] = int(l.split('by')[1].strip())
    elif l.startswith('If true'):
        M[-1]['t'] = int(l.split('monkey')[1].strip())
    elif l.startswith('If false'):
        M[-1]['f'] = int(l.split('monkey')[1].strip())

M2 = deepcopy(M)
div = 1
for m in M:
    div *= m['div']


play(M, 20, 3, div)
play(M2, 10_000, 1, div)

print(f"Scores {score(M)} {score(M2)}")
