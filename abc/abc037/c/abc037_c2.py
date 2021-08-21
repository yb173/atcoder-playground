n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = [0] * (n - k + 1)
for i in range(k):
    ans[0] += a[i]

for i in range(1, n - k + 1):
    ans[i] = ans[i - 1] - a[i - 1] + a[i + k - 1]

print(sum(ans))
