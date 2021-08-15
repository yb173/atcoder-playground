def test(i: int) -> bool:
    s_sub = S[i: i + LT]
    for s, t in zip(s_sub, T):
        if s == '?':
            continue
        if t != s:
            return False
    return True

S = input()
T = input()

LS = len(S)
LT = len(T)

for i in reversed(range(LS - LT + 1)):
    if test(i):
        ans = S[:i].replace('?', 'a') + T + S[i + LT:]
        print(ans)
        break
else:
    print("UNRESTORABLE")
