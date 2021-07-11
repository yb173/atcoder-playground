INF = 1 << 60

N = input()
digit = len(N)

ans = INF
for bit in range(1 << digit):
    total = 0
    cnt = 0
    for i in range(digit):
        if bit & (1 << i):
            total += int(N[i])
        else:
            cnt += 1
    if total % 3 == 0 and cnt < digit:
        ans = min(ans, cnt)

if ans == INF:
    print(-1)
else:
    print(ans)
