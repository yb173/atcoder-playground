N = int(input())
C = [list(input().split()) for _ in range(N)] # s, p

s = 0
n = 'atcoder'
for x in C:
    s += int(x[1])

for x in C:
    if s / 2 < int(x[1]):
        n = x[0]
        break

print(n)
