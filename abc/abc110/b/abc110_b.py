N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
x_max = max(x)
y = list(map(int, input().split()))
y_min = min(y)

ok = False
for Z in range(-99, 101):
    if not X < Z <= Y: continue
    if not x_max < Z: continue
    if not y_min >= Z: continue
    ok = True
    break

print("No War" if ok else "War")
