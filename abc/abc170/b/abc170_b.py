X, Y = map(int, input().split())

for i in range(0, X + 1):
    t = i
    k = X - t
    y = 2 * t + 4 * k
    if y == Y:
        print("Yes")
        exit()

print("No")
