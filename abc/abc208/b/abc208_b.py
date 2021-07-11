from math import factorial

a = [0] * 10
for i in range(10):
    a[i] = factorial(i + 1)

P = int(input())

cnt = 0
for i in reversed(range(10)):
    s = P // a[i]
    cnt += s
    P %= a[i]
    if P == 0:
        break

print(cnt)
