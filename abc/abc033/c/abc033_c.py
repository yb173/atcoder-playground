import sys
sys.setrecursionlimit(10 ** 9)

s = input()
t = s.split('+')

ans = 0
for v in t:
    result = eval(v)
    if result != 0:
        ans += 1

print(ans)
