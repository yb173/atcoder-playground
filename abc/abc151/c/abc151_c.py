N, M = map(int, input().split())
G = [[] for i in range(N)]

for i in range(M):
    p, s = input().split()
    p = int(p) - 1
    G[p].append(s)

ans_ac = 0
ans_wa = 0
for i in range(N):
    if not 'AC' in G[i]: continue
    ans_ac += 1
    for j in range(len(G[i])):
        if G[i][j] == 'AC':
            ans_wa += j
            break

print('{} {}'.format(ans_ac, ans_wa))
