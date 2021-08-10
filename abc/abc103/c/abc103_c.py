N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans += A[i] - 1

print(ans)
