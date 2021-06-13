S = list(input())
S.sort()
if (S[0] == S[1] and S[2] == S[3] and S[1] != S[2]):
    print("Yes")
else:
    print("No")
