from math import ceil, sqrt
R, X, Y = map(int, input().split())
d = sqrt(X ** 2 + Y ** 2)

if d == R:
    print(1)
elif d <= R + R:
    print(2)
else:
    print(ceil(d / R))
