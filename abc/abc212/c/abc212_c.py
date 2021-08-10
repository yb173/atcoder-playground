N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
B = list(map(int, input().split()))
B.sort()

ans = 1 << 60
i, j = 0, 0
while i < N and j < M:
    ans = min(ans, abs(A[i] - B[j]))
    if A[i] > B[j]:
        j += 1
    else:
        i += 1

print(ans)
