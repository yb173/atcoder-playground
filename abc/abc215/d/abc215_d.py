N, M = map(int, input().split())
A = list(map(int, input().split()))

L = 10 ** 5 + 1
x = [False] * L

# Ai があるところのフラグを立てる
for i in range(N):
    x[A[i]] = True

# Ai の約数の一覧を求める
divisor = []
for i in range(2, L):
    for j in range(i, L, i):
        if x[j]:
            divisor.append(i)
            break

# 約数とその倍数に×印をつけていく
ok = [True] * (M + 1)
for d in divisor:
    for j in range(d, M + 1, d):
        ok[j] = False

cnt = sum(ok) -1
print(cnt)
for i in range(1, M + 1):
    if ok[i]:
        print(i)
