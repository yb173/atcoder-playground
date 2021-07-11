N = int(input())
sq = int(N ** 0.5)

s = set()
for a in range(2, sq + 1):
    x = a * a
    while x <= N:
        s.add(x)
        x *= a

print(N - len(s))
