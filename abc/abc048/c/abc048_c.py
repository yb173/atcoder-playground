N, x = map(int, input().split())
a = list(map(int, input().split()))
total = sum(a)

if x < a[0]:
    a[0] = x

for i in range(N - 1):
    t = a[i] + a[i + 1]
    if x < t:
        a[i + 1] -= t - x

ans = total - sum(a)

print(ans)
