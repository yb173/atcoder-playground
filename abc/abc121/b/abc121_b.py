N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    sum = C
    for j in range(M):
        sum += B[j] * A[i][j]
    if sum > 0:
        ans += 1

print(ans)
