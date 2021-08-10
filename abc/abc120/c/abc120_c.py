S = input()
d = {'0':0, '1':0}
for s in S:
    d[s] += 1

print(min(d['0'], d['1']) * 2)
