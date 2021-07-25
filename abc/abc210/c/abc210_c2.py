
from collections import defaultdict

N, K = map(int, input().split())
c = list(map(int, input().split()))

d = defaultdict(lambda: 0)

for i in range(K):
    d[c[i]] += 1
ans = len(d)

for i in range(N - K + 1):
    if i == 0: continue
    d[c[i + K - 1]] += 1
    d[c[i - 1]] -= 1
    if d[c[i - 1]] == 0:
        d.pop(c[i - 1])
    ans = max(ans, len(d))

print(ans)
