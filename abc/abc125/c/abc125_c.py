from math import gcd
N = int(input())
A = list(map(int, input().split()))

ltot = [None] * N
rtot = [None] * N

for i in range(N):
    if i == 0:
        ltot[i] = A[i]
    else:
        ltot[i] = gcd(A[i], ltot[i - 1])

for i in reversed(range(N)):
    if i == N - 1:
        rtot[i] = A[i]
    else:
        rtot[i] = gcd(A[i], rtot[i + 1])

ans = -1
for i in range(N):
    if i == 0:
        now = rtot[i + 1]
    elif i == N - 1:
        now = ltot[i - 1]
    else:
        now = gcd(ltot[i - 1], rtot[i + 1])
    ans = max(ans, now)

print(ans)
