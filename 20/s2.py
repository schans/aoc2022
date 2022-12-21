#!/usr/bin/env python3

import fileinput

# counters
tot = 0
tot2 = 0
K = 811589153
N = []
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    N.append(int(l))


def shuffle(deck, n):
    fixed = list(deck)
    l = len(fixed)
    for _ in range(n):
        for f in fixed:
            i = deck.index(f)
            t = (i + f[1]) % (l-1)
            deck.pop(i)
            deck.insert(t, f)
    return deck


def get_score(deck):
    s = i = 0
    l = len(deck)
    for p in deck:
        if p[1] == 0:
            i = deck.index(p)
            break
    for x in range(1, 4):
        s += deck[(i+x*1000) % l][1]
    return s


# part 1
deck = list((i+1, v) for i, v in enumerate(N))
deck = shuffle(deck, 1)
tot = get_score(deck)

# part 2
deck = list((i, v*K) for i, v in enumerate(N))
deck = shuffle(deck, 10)
tot2 = get_score(deck)

print(f"Scores {tot} {tot2}")
