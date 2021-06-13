x, y = map(int, input().split())

if x == y:
    print(x)
    exit()

s = {0, 1, 2}
s.remove(x)
s.remove(y)

for item in s:
    print(item)
