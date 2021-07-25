import math

N = int(input())

ans = 1 << 60
m = math.floor(N ** .5) + 1
for i in range(1, m):
    if N % i == 0:
        c = N // i
        ans = min(ans, c + i - 2)

print(ans)
