N = int(input())
p = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if p[i] != i + 1:
        cnt += 1

if cnt == 0 or cnt == 2:
    print("YES")
else:
    print("NO")
