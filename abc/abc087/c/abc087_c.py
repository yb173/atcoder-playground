N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for x in range(N):
    now = 0
    for i in range(x + 1):
        now += A[i]
    for j in range(x, N):
        now += B[j]
    ans = max(ans, now)

print(ans)
