ans = 0
for i in range(3):
    a, b = map(int, input().split())
    ans += a * b
ans //= 10

print(ans)
