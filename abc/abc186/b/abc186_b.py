INF = 1 << 60

H, W = map(int, input().split())

m = INF
s = 0
for i in range(H):
    a = list(map(int, input().split()))
    s += sum(a)
    m = min(m, min(a))

print(s - m * H * W)
