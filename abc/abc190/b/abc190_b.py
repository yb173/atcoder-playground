N, S, D = map(int, input().split())

ok = False
for i in range(N):
    x, y = map(int, input().split())
    if x < S and y > D:
        ok = True
        break

if ok:
    print("Yes")
else:
    print("No")
