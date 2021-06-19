N = int(input())
s = [input() for _ in range(N)]
M = int(input())
t = [input() for _ in range(M)]

ans = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if s[j] == s[i]:
            cnt += 1
    for k in range(M):
        if t[k] == s[i]:
            cnt -= 1
    ans = max(ans, cnt)

print(ans)
