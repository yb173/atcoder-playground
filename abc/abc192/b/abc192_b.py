from collections import defaultdict
import math

INF = 1 << 60
MOD = 10**9 + 7

S = input()

unreadable = True
for i in range(len(S)):
    if (i + 1) % 2 == 0:
        # 偶数の場合
        if S[i].islower():
            unreadable = False
            break
    else:
        # 偶数の場合
        if S[i].isupper():
            unreadable = False
            break

if unreadable:
    print("Yes")
else:
    print("No")
