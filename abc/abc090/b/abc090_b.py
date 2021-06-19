a, b = map(int, input().split())
ans = 0
for i in range(a, b + 1):
    ir = int(str(i)[::-1])
    if i == ir:
        ans += 1
print(ans)

