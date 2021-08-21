from itertools import product

N, A = map(int, input().split())
x = list(map(int, input().split()))

ans = 0
for v in product([0, 1], repeat=N):
    if sum(v) == 0: continue
    m = sum([v[i] * x[i] for i in range(N)])
    if sum(v) * A == m:
        ans += 1

print(ans)
