from itertools import product

S = input()

ans = 0
for o in product([False, True], repeat=len(S) - 1):
    o = o + (False,)
    formula = ''.join([s + '+' if o[i] else s for i, s in enumerate(S)])
    ans += eval(formula)

print(ans)
