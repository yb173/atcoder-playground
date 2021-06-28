N, T = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = 0
for i in range(N):
    t = T
    if not i == N - 1:
        diff = A[i + 1] - A[i]
        if diff < T:
            t = diff
    ans += t

print(ans)
