INF = 1 << 60

n = int(input())
a = list(map(int, input().split()))

ans = INF
for x in range(-100, 101):
    now = sum([abs(a[i] - x) ** 2 for i in range(n)])
    ans = min(ans, now)

print(ans)
