N = int(input())
H = list(map(int, input().split()))

max_h = 0
ans = 0
for i in range(N):
    if max_h <= H[i]:
        max_h = H[i]
        ans += 1

print(ans)
