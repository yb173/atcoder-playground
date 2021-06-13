n = int(input())
p = list(map(int, input().split()))

ans = 0
for i in range(n):
    if i == 0 or i == n - 1: continue
    if (p[i - 1] < p[i] and p[i] < p[i + 1]) or (p[i - 1] > p[i] and p[i] > p[i + 1]): ans += 1

print(ans)
