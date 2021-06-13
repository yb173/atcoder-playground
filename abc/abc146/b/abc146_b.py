N = int(input())
S = input()

ans = ''
for i in range(len(S)):
    m = ord(S[i]) + N
    if m > 90: m -= 26
    ans += chr(m)

print(ans)
