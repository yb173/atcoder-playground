N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = (N + K - 3) // (K - 1)
print(ans)
