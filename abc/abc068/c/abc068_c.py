N, M = map(int, input().split())

E = set()

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    E.add((a, b))

for i in range(len(E)):
    if (0, i) in E and (i, N - 1) in E:
        print("POSSIBLE")
        break
else:
    print("IMPOSSIBLE")
