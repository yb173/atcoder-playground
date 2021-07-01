S = input()
T = input()

pool = 'atcoder'

for i in range(len(S)):
    if S[i] == T[i]: continue
    if S[i] != T[i] and S[i] != '@' and T[i] != '@':
        print("You will lose")
        exit()
    w = S[i] if T[i] == '@' else T[i]
    if not w in pool:
        print("You will lose")
        exit()

print("You can win")
