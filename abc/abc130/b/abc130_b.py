N, X = map(int, input().split())
L = list(map(int, input().split()))

d = 0
cnt = 1
for i in range(N):
    d += L[i]
    if d > X:
        break
    cnt += 1

print(cnt)
