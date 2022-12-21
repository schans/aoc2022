#!/usr/bin/env python3

import fileinput

# counters
tot = 0
tot2 = 0

M = {}
K = {}

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    w = l.split()
    if len(w) == 2:
        K[w[0][:-1]] = w[1]
    else:
        M[w[0][:-1]] = w[1:]


def solve(m):
    if m in K:
        return K[m]
    p1 = solve(M[m][0])
    op = M[m][1]
    p2 = solve(M[m][2])
    return str(int(eval(" ".join([p1, op, p2]))))


def solve_for(m):
    for t, exp in M.items():
        if exp[0] == m or exp[2] == m:
            break

    if t in K:
        te = K[t]
    else:
        te = solve_for(t)

    op = exp[1]
    if exp[0] == m:
        n = exp[2]
    else:
        n = exp[0]
    if n in K:
        ne = K[n]
    else:
        ne = solve(n)

    if exp[0] == m:
        # solve for m : te = m op ne
        if op == '-':
            eq = f"({te}) + ({ne})"
        elif op == '+':
            eq = f"({te}) - ({ne})"
        elif op == '*':
            eq = f"({te}) / ({ne})"
        elif op == '/':
            eq = f"({te}) * ({ne})"
    else:
        # solve for m : te = ne op m
        if op == '-':
            eq = f"({ne}) - ({te})"
        elif op == '+':
            eq = f"({te}) - ({ne})"
        elif op == '*':
            eq = f"({te}) / ({ne})"
        elif op == '/':
            eq = f"({ne}) / ({te}"

    return str(int(eval(eq)))


# part 1
tot = solve('root')
r = solve(M['root'][2])

# part 2
del (K['humn'])
K[M['root'][2]] = r
K[M['root'][0]] = r
tot2 = solve_for('humn')

print(f"Scores {tot} {tot2}")
