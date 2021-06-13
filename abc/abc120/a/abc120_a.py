a, b, c = map(int, input().split())

if b - a * c >= 0:
    print(c)
else:
    print(b // a)
