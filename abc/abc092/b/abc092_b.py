N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = 0
for i in range(N):
    j = 0
    while j * A[i] + 1 <= D:
        j += 1
    ans += j

print(ans + X)
