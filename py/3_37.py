def avalue(a):
    val = 0
    for s in a:
        val += ord(s) - ord('a') + 1
    return val


names = sorted(open('names').readline().rstrip().split(','))
total, i = 0, 1
for i, name in enumerate(names):
    total += avalue(name) * (i + 1)
print(total)