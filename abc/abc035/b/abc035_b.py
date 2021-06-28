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
    if 0 <= x:
        x += unknown_cnt
    else:
        x -= unknown_cnt
    print(dist(x, y))
else:
    for i in range(unknown_cnt):
        if 0 < x:
            x -= 1
        elif x < 0:
            x += 1
        elif 0 < y:
            y -= 1
        elif y < 0:
            y += 1
        else:
            x += 1
    
    print(dist(x, y))
