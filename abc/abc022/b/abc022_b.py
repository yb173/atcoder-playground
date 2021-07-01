N = int(input())
A = [int(input()) for _ in range(N)]

ans = 0
used = set()
for i in range(N):
    if A[i] in used:
        ans += 1
    used.add(A[i])

print(ans)
