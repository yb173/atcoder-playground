a, b, c, d = map(int, input().split())

if c > b or a > d:
    print(0)
    exit()

print(min(b, d) - max(a, c))
