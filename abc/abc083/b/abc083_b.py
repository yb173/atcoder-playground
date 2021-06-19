def digitSum(N: int):
    sum = 0
    while N > 0:
        q, mod = divmod(N, 10)
        sum += mod
        N = q
    return sum

N, A, B = map(int, input().split())
ans = 0
for i in range(1, N + 1):
    t = digitSum(i)
    if A <= t <= B:
        ans += i

print(ans)

