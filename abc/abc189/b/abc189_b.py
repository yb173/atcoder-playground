N, X = map(int, input().split())
X *= 100

alco = 0
for i in range(N):
    v, p = map(int, input().split())
    alco += v * p
    if X < alco:
        print(i + 1)
        exit()

print(-1)
