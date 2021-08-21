n, q = map(int, input().split())

# 最後の値は使わない
imosu = [0] * (n + 1)

for i in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    imosu[l] += 1
    imosu[r + 1] -= 1

cum = [0] * n
for i in range(n):
    if i == 0:
        cum[i] = imosu[i]
    else:
        cum[i] = cum[i - 1] + imosu[i]

ans = ['0' if cum[i] % 2 == 0 else '1' for i in range(n)]

print(''.join(ans))
