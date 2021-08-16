INF = 1 << 60

n = int(input())
S = [input() for _ in range(n)]

alp = [INF] * 26
for i in range(n):
    now = [0] * 26
    for s in S[i]:
        now[ord(s) - 97] += 1
    for i in range(26):
        alp[i] = min(alp[i], now[i])

ans = []
for i in range(26):
    for j in range(alp[i]):
        ans.append(chr(i + 97))

print(''.join(ans))
