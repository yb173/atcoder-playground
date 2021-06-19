def digitSum(N):
    sum = 0
    while N > 0:
        q, mod = divmod(N, 10)
        sum += mod
        N = q
    return sum

N = int(input())
S = digitSum(N)
print("Yes" if N % S == 0 else "No")
