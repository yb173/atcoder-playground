N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(N):
    if A[i] < B[i]:
        B[i] -= A[i]
        ans += A[i]
        diff = min(B[i], A[i + 1])
        A[i + 1] -= diff
        ans += diff
    else:
        ans += B[i]

print(ans)
