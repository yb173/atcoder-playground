# TLE

from itertools import permutations

N = input()
a = []
for i in range(len(N)):
    n = N[i]
    a.append(n)

a.append('x')

ans = 0
for v in permutations(a):
    s = ''.join(v)
    ss = s.split('x')
    first = ss[0]
    second = ss[1]
    if len(first) == 0 or len(second) == 0:
        continue
    tmp = int(first) * int(second)
    ans = max(tmp, ans)

print(ans)
