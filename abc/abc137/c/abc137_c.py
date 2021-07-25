from collections import Counter

N = int(input())
S = [''.join(sorted(input())) for _ in range(N)]
c = Counter(S)

ans = 0
for v in c.values():
    if v == 1: continue
    ans += v * (v - 1) // 2

print(ans)
