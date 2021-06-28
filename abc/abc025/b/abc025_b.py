N, A, B = map(int, input().split())
sd = [list(input().split()) for _ in range(N)]

ans = 0
for v in sd:
    d = int(v[1])
    if d < A:
        d = A
    if B < d:
        d = B
    if v[0] == 'East':
        ans += d
    else:
        ans -= d

if ans > 0:
    print('East ' + str(ans))
elif ans < 0:
    print('West ' + str(-ans))
else:
    print(0)
        