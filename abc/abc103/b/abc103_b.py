def rot(S: str):
    l = len(S)
    return S[l - 1] + S[:l - 1]

S = input()
T = input()

for i in range(len(S)):
    if rot(S) == T:
        print("Yes")
        exit()
    S = rot(S)

print("No")
