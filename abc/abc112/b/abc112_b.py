N, T = map(int, input().split())

min_cost = 1 << 60
for i in range(N):
    c, t = map(int, input().split())
    if t > T: continue
    min_cost = min(min_cost, c)

if min_cost == 1 << 60:
    print("TLE")
else:
    print(min_cost)
