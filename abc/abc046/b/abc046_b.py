N, K = map(int, input().split())
ans = K
ans *= (K - 1) ** (N - 1)
print(ans)
