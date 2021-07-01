# TLE
n = int(input())
a = 0
b = 0
c = 1

if n == 1:
    print(a)
    exit()

if n == 2:
    print(b)
    exit()

if n == 3:
    print(c)
    exit()

for i in range(3, n):
    d = c + b + a
    c, b, a = d, c, b

print(d % 10007)
