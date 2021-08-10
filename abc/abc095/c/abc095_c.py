a, b, c, x, y = map(int, input().split())

ans = 1 << 60

ans = min(ans, x * a + y * b)
ans = min(ans, 2 * c * max(x, y))

if x > y:
    diff = x - y
    ans = min(ans, 2 * c * y + diff * a)
else:
    diff = y - x
    ans = min(ans, 2 * c * x + diff * b)

print(ans)
