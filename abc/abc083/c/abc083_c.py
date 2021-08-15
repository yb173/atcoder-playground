x, y = map(int, input().split())

n = 1
while x * 2 <= y:
    x *= 2
    n += 1

print(n)
