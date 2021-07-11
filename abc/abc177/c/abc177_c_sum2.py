MOD = 10 ** 9 + 7

N = int(input())
A = list(map(int, input().split()))

# 累積和（添え字が1ずれる）
B = [0] * (N + 1)
for i in range(N):
    B[i + 1] = (B[i] + A[i]) % MOD

ans = 0
for i in range(N):
    # 累積和を使って i + 1 からN までの累積和を求める．
    sum = B[N] - B[i + 1]
    ans += A[i] * sum
    ans %= MOD

print(ans)
