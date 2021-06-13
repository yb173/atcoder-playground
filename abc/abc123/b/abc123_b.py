max_rest = 0
d = []
for i in range(5):
    n = int(input())
    d.append(n)
    mod = n % 10
    rest = 0 if mod == 0 else 10 - mod
    max_rest = max(max_rest, rest)

ans = 0
for i in range(5):
    ans += ((d[i] + 9) // 10) * 10

print(ans - max_rest)
