a, b, c, x, y = map(int, input().split())

ans = 1 << 60
for k in range(10 ** 5 + 1):
    now = 2 * c * k + max(x - k, 0) * a + max(y - k, 0) * b
    ans = min(ans, now)

print(ans)
