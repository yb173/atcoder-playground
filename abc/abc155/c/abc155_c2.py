from collections import defaultdict

N = int(input())
S = [input() for _ in range(N)]

d = defaultdict(lambda: 0)
for s in S:
    d[s] += 1

ma = 0
for k, v in d.items():
    ma = max(ma, v)

for k, v in sorted(d.items()):
    if v == ma:
        print(k)
