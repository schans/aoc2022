#!/usr/bin/env python3

import fileinput

# global
tot = 0
tot2 = 0

B = []
TB = ['geo', 'obs', 'clay', 'ore']

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    words = l.split()

    b = {}
    for t in TB:
        b[t] = {}

    id = int(words[1][:-1])

    b['ore']['ore'] = int(words[6])

    b['clay']['ore'] = int(words[12])

    b['obs']['ore'] = int(words[18])
    b['obs']['clay'] = int(words[21])

    b['geo']['ore'] = int(words[27])
    b['geo']['obs'] = int(words[30])

    B.append(b)


def max_geods(t, blue):
    queue = []
    seen = set()

    max_geo = [0 for _ in range(t+1)]
    max_ore_spending = max(blue['ore']['ore'], blue['clay']['ore'], blue['obs']['ore'], blue['geo']['ore'])

    queue.append((t, 0, 0, 0, 0, 1, 0, 0, 0))
    while queue:
        (t, r_ore, r_clay, r_obs, r_geo, b_ore, b_clay, b_obs, b_geo) = queue.pop()
        max_geo[t] = max(max_geo[t], r_geo)

        if t == 0:
            continue

        # add resouces
        nr_ore = r_ore + b_ore
        nr_clay = r_clay + b_clay
        nr_obs = r_obs + b_obs
        nr_geo = r_geo + b_geo

        if (t, r_ore, r_clay, r_obs, r_geo, b_ore, b_clay, b_obs, b_geo) in seen:
            continue
        seen.add((t, r_ore, r_clay, r_obs, r_geo, b_ore, b_clay, b_obs, b_geo))

        # if len(seen) % 1000000 == 0:
        #     print(t, best, len(seen))

        if r_geo < max_geo[t]-1:
            # search is too far behind, -1 offset is emperical
            continue

        # save all resources
        queue.append(((t-1, nr_ore, nr_clay, nr_obs, nr_geo, b_ore, b_clay, b_obs, b_geo)))

        # buy ore if not maxed out on spending rate
        if r_ore >= blue['ore']['ore'] and b_ore < max_ore_spending:
            queue.append(((t-1, nr_ore - blue['ore']['ore'], nr_clay, nr_obs, nr_geo, b_ore+1, b_clay, b_obs, b_geo)))

        # buy clay if not maxed out on spending rate
        if r_ore >= blue['clay']['ore'] and b_clay < blue['obs']['clay']:
            queue.append(((t-1, nr_ore - blue['clay']['ore'], nr_clay, nr_obs, nr_geo, b_ore, b_clay+1, b_obs, b_geo)))

        # buy obs
        if r_ore >= blue['obs']['ore'] and r_clay >= blue['obs']['clay']:
            queue.append(((t-1, nr_ore - blue['obs']['ore'],
                           nr_clay - blue['obs']['clay'], nr_obs, nr_geo, b_ore, b_clay, b_obs+1, b_geo)))
        # buy geo
        if r_ore >= blue['geo']['ore'] and r_obs >= blue['geo']['obs']:
            queue.append(((t-1, nr_ore - blue['geo']['ore'],
                           nr_clay, nr_obs - blue['geo']['obs'], nr_geo, b_ore, b_clay, b_obs, b_geo+1)))

    return max(max_geo)


# part 1
for i in range(len(B)):
    r = max_geods(24, B[i])
    tot += (i+1) * r

# part 2
tot2 = 1
for i in range(min(len(B), 3)):
    r = max_geods(32, B[i])
    tot2 *= r


print(f"Scores {tot} {tot2}")
