from math import gcd

N, X = map(int, input().split())
x = list(map(int, input().split()))

absx = [abs(X - v) for v in x]

ans = absx[0]
for i in range(N):
    if i == 0:
        continue
    ans = gcd(ans, absx[i])

print(ans)
