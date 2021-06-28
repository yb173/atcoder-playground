A = int(input())
ans = -1
for x in range(1, A):
    y = A - x
    ans = max(ans, x * y)
print(ans)
