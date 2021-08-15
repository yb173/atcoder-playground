N, M = map(int, input().split())

E1 = set()
E2 = set()

for i in range(M):
    a, b = map(int, input().split())
    if a == 1:
        E1.add(b)
    if b == N:
        E2.add(a)

if E1 & E2:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
