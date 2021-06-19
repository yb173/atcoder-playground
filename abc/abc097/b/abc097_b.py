X = int(input())
c = [1]
for i in range(2, 32):
    p = 2
    while i ** p <= X:
        c.append(i ** p)
        p += 1

print(max(c))
