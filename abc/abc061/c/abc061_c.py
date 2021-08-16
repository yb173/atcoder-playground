from collections import defaultdict

N, K = map(int, input().split())

d = defaultdict(lambda: 0)
for i in range(N):
    a, b = map(int, input().split())
    d[a] += b

d = sorted(d.items(), key=lambda x: x[0])

t = 0
for k, v in d:
    t += v
    if K <= t:
        print(k)
        exit()
