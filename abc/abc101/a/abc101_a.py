S = input()
ans = 0
for i in range(4):
    ans += 1 if S[i] == '+' else -1
print(ans)
