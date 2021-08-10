N, K = map(int, input().split())

ans = 0

m = 0
for i in range(1, N + 1):
    if i % K == 0:
        m += 1

ans += m ** 3

if K % 2 == 0:
    c = 0
    for i in range(1, N + 1):
        if i % K == K // 2:
            c += 1
    ans += c ** 3

print(ans)
