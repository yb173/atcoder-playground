N = int(input())
X, Y = map(int, input().split())
A = [None] * N
B = [None] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

INF = 1 << 60
ans = INF

for bit in range(1 << N):
    cnt = 0
    x = 0
    y = 0
    for i in range(N):
        if not bit >> i & 1: continue
        cnt += 1
        x += A[i]
        y += B[i]
    if x >= X and y >= Y:
        ans = min(ans, cnt)

if ans == INF:
    print(-1)
    exit()

print(ans)
    