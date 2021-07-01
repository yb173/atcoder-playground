d = []
for i in range(4):
    d.append(list(input().split()))

T = [[None] * 4 for i in range(4)]

for i in range(4):
    for j in range(4):
        T[3 - i][3 - j] = d[i][j]

for t in T:
    print(' '.join(t))
