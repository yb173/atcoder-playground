N = int(input())
ans = 0
for i in range(N):
    x, u = input().split()
    x = float(x)
    if u == 'BTC':
        x = 380000 * x
    ans += x
print(ans)
