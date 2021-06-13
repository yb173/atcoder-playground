N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    if A[i] <= 10:
        continue
    ans += A[i] - 10

print(ans)
