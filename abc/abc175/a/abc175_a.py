S = input()

ans = 1
if S[0] == "R" and S[1] == "R" and S[2] == "R":
    ans = 3
elif (S[0] == "R" and S[1] == "R" and S[2] == "S") or (S[0] == "S" and S[1] == "R" and S[2] == "R"):
    ans = 2
elif S[0] == "S" and S[1] == "S" and S[2] == "S":
    ans = 0

print(ans)
