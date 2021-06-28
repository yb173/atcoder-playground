N = int(input())
a = list(map(int, input().split()))

s = sum(a)

if not s % N == 0:
    print(-1)
    exit()

ave = s // N

t = 0
it = 0
ans = 0
for i in range(N):
    t += a[i]
    it += ave
    if t == it: continue
    ans += 1

print(ans)
    