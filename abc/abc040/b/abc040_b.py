n = int(input())

min_diff = 1 << 60
for i in range(1, n + 1):
    for j in range(1, n // i + 1):
        s = i * j
        if n < s: continue
        diff = n - s + abs(i - j)
        min_diff = min(min_diff, diff)

print(min_diff)
