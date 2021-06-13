S = input()
ans = 0
tmp = 0
for i in range(len(S)):
    if S[i] == 'A' or S[i] == 'C' or S[i] == 'G' or S[i] == 'T':
        tmp += 1
    else:
        tmp = 0
    ans = max(ans, tmp)

print(ans)
