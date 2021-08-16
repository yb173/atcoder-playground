S = input()
S = S[::-1]

test = []
test.append('dream'[::-1])
test.append('dreamer'[::-1])
test.append('erase'[::-1])
test.append('eraser'[::-1])

while len(S):
    ok = False
    for v in test:
        if S.startswith(v):
            S = S[len(v):]
            ok = True
            break
    if not ok:
        print("NO")
        exit()

print("YES")
