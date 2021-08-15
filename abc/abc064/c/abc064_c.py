N = int(input())
A = list(map(int, input().split()))

cnt = [0] * 9

for i in range(N):
    color = min(A[i] // 400, 8)
    cnt[color] += 1

d = [i for i in range(9) if cnt[i]]
l = len(d)

if 8 in d:
    mi = max(1, l - 1)
    ma = l - 1 + cnt[8]
    print(mi, ma)
else:
    print(l, l)
