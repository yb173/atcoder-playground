N, K = map(int, input().split())
a = list(map(int, input().split()))

tmp = K // N
c = []
for i in range(N):
    c.append([a[i], i, tmp])

c.sort(key=lambda x: x[0])

tmp2  = K % N

for i in range(tmp2):
    c[i][2] += 1

c.sort(key=lambda x: x[1])

for v in c:
    print(v[2])
