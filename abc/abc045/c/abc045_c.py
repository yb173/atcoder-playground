from itertools import product

def calc(s, opes) -> int:
    ret = []
    now = S[0]
    for i in range(len(opes)):
        if opes[i]:
            ret.append(now)
            now = S[i + 1]
        else:
           now += S[i + 1]
    if now:
        ret.append(now)

    return sum(map(int, ret))

S = input()

ans = 0
for opes in product([False, True], repeat=len(S) - 1):
    ans += calc(S, opes)

print(ans)
