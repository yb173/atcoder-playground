P = list(map(int, input().split()))

ans = []
for i in range(26):
    ans.append(chr(P[i] + 96))
print(''.join(ans))
