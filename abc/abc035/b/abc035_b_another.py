def dist(x, y) -> int:
    return abs(x) + abs(y)
        
S = list(input())
T = int(input())

x = 0
y = 0
unknown_cnt = 0

for i in range(len(S)):
    if S[i] == '?':
        unknown_cnt += 1
        continue
    if S[i] == 'U':
        y += 1
        continue
    if  S[i] == 'D':
        y -= 1
        continue
    if S[i] == 'R':
        x += 1
        continue
    if S[i] == 'L':
        x -= 1
        continue

if T == 1:
    print(dist(x, y) + unknown_cnt)
else:
    print(max(len(S) % 2, dist(x, y) - unknown_cnt))
