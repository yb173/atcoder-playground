N = int(input())
A = list(map(int, input().split()))
B = [None] * N
for i in range(N):
    B[i] = A[i] - (i + 1)
B.sort()

if N % 2 == 1:
    b = B[N // 2]
else:
    b = (B[N // 2 - 1] + B[N // 2]) // 2

ans = 0
for i in range(N):
    ans += abs(B[i] - b)

print(ans)
