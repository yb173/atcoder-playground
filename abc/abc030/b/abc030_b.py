n, m = map(int, input().split())
n %= 12
t = 30 * n + m / 2
p = 6 * m
diff = abs(t - p)
if diff > 180:
    diff = 360 - diff

print(diff)
 