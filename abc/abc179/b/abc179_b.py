N = int(input())

D = []
for i in range(N):
    a, b = map(int, input().split())
    D.append([a, b])

found = False
for i in range(N):
    if i > 1:
        if D[i][0] == D[i][1] and D[i - 1][0] == D[i - 1][1] and D[i - 2][0] == D[i - 2][1]:
            found = True
            break

print("Yes" if found else "No")
