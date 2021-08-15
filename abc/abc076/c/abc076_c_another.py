import re

S = input()
T = input()

LS = len(S)
LT = len(T)

S = S.replace('?', '.')[::-1]
T = T[::-1]

for i in range(LS - LT + 1):
    if re.match(S[i:i + LT], T):
        ans = S[:i].replace('.', 'a') + T + S[i + LT:].replace('.', 'a')
        print(ans[::-1])
        break
else:
    print("UNRESTORABLE")
