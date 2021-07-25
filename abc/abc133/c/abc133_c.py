L, R = map(int, input().split())

ans = 1 << 60
R = min(R, L + 4038)
for i in range(L, R):
    for j in range(i + 1, R + 1):
        now = i % 2019 * j % 2019
        ans = min(ans, now)
        if now == 0:
            print(ans)
            exit()

print(ans)
