N, A, B = map(int, input().split())

ans = 0

q, mod = divmod(N, A + B)
ans += q * A

if mod <= A:
    ans += mod
else:
    ans += A

print(ans)
