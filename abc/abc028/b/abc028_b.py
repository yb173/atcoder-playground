S = list(input())
ABCDEF = "ABCDEF"
ans = []
for v in ABCDEF:
    ans.append(str(S.count(v)))

print(" ".join(ans))
