#!/usr/bin/env python3

import fileinput

# counters
tot = 0
tot2 = 0
N = []
K = 811589153

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    N.append(int(l))

L = len(N)


def get_list(k):
    m = []
    h = None
    for n in N:
        m.append({'v': n * k})
        if n == 0:
            h = m[-1]

    for i in range(1, L):
        m[i]['p'] = m[i-1]
    for i in range(0, L-1):
        m[i]['n'] = m[i+1]
    m[0]['p'] = m[L-1]
    m[L-1]['n'] = m[0]
    return m, h


def dump(c):
    l = []
    pv = c['p']['v']
    for _ in range(L):
        l.append(c['v'])
        c = c['n']
    print(pv, l, c['v'])
    print()


def move_after(c, a):
    # remove c:  p - c - n => p - n
    p = c['p']
    n = c['n']
    p['n'] = n
    n['p'] = p

    # insert c: a - b => a - c - b
    b = a['n']
    a['n'] = c
    c['n'] = b
    b['p'] = c
    c['p'] = a


def shuffle(M, x):
    for _ in range(x):
        for c in M:
            m = c['v']
            n = c
            if m > 0:
                for _ in range(m % (L-1)):
                    n = n['n']
                move_after(c, n)
            elif m < 0:
                for _ in range(-m % (L-1)):
                    n = n['p']
                move_after(c, n['p'])


def get_score(h):
    s = 0
    n = h
    for i in range(1, 3001):
        n = n['n']
        if i and not i % 1000:
            s += n['v']
    return s


# part 1
m, h = get_list(1)
shuffle(m, 1)
tot = get_score(h)

# part 2
m, h = get_list(K)
shuffle(m, 10)
tot2 = get_score(h)

print(f"Scores {tot} {tot2}")
