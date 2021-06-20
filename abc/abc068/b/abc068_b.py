def divideTimes(n: int):
    cnt = 0
    while n > 0:
        if not n % 2 == 0:
            break
        cnt += 1
        n //= 2
    return cnt

N = int(input())

index = -1
cnt = -1
for i in range(1, N + 1):
    if cnt < divideTimes(i):
        cnt = divideTimes(i)
        index = i            

print(index)
