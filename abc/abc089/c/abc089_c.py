from itertools import combinations
from collections import defaultdict

N = int(input())
S = [input() for _ in range(N)]

d = defaultdict(lambda: 0)
for i in range(N):
    d[S[i][0]] += 1

ans = 0
for x, y, z in combinations('MARCH', 3):
    ans += d[x] * d[y] * d[z]

print(ans)
