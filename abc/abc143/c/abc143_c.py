N = int(input())
S = input()

ans = [S[0]]
for i in range(1, N):
    if S[i - 1] == S[i]: continue
    ans.append(S[i])

print(len(ans))
