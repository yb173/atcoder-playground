MOD = 10 ** 9 + 7

N = int(input())
A = list(map(int, input().split()))

# 全体の面積を求める
edge = 0
for i in range(N):
    edge = (edge + A[i]) % MOD
s = edge ** 2

# i == j の部分の面積を求める
center = 0
for i in range(N):
    center = (center + A[i] ** 2) % MOD

# 全体 - 真ん中
ans = s - center

# 半分にする（逆元をとる）
# ans /= 2 の mod をとるとこうなる
ans *= (MOD + 1) // 2
ans %= MOD

print(ans)

