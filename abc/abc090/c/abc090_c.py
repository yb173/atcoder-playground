N, M = map(int, input().split())

if N == 1 and M == 1:
    print(1)
    exit()

if N == 1 or M == 1:
    print(max(N - 2, M - 2))
    exit()

ans = max(N - 2, 0) * max(M - 2, 0)
print(ans)
