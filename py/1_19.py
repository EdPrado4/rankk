from itertools import permutations

def su(p, i):
    return sum(int(p[k]) for k in range(i, i + 3))

def s(p, i1, i2, i3):
    return sum(int(p[k]) for k in [i1, i2, i3]  )

for p in permutations('123456789'):
    if su(p, 0) == su(p, 3) == su(p, 6) == s(p, 0, 3, 6) == s(p, 1, 4, 7) == s(p, 2, 5, 8) == s(p, 2, 4, 6) == s(p, 0, 4, 8):
        print(p)

