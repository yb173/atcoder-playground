S = input()

ans = 0
now = S[0]
for i in range(1, len(S)):
    if now == S[i]: continue
    now = S[i]
    ans += 1

print(ans)
