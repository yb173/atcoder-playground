A, B, C, K = map(int, input().split())
S, T = map(int, input().split())
ans = S * A + T * B
if S + T >= K:
    ans -= (S + T) * C

print(ans)
