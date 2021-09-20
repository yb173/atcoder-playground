X = input()
N = int(input())
S = [input() for _ in range(N)]

d = {}
for i in range(26):
    d[X[i]] = i

ans = []
for i in range(N):
    name = []
    for s in S[i]:
        name.append(d[s])
    ans.append((name, S[i]))

ans.sort(key=lambda x: x[0])

for i in range(N):
    print(ans[i][1])
