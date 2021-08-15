from itertools import combinations
from collections import defaultdict

N = int(input())
S = [input() for _ in range(N)]

d = defaultdict(lambda: 0)
for i in range(N):
    d[S[i][0]] += 1

march = 'MARCH'
ans = 0
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            x = march[i]
            y = march[j]
            z = march[k]
            ans += d[x] * d[y] * d[z]

print(ans)
