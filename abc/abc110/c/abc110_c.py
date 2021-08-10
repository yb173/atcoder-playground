S = list(input())
T = list(input())

start = [-1] * 26
end = [-1] * 26

ok = True
for i in range(len(S)):
    sn = ord(S[i]) - 97
    tn = ord(T[i]) - 97
    if start[sn] == -1 and end[tn] == -1:
        start[sn] = tn
        end[tn] = sn
    else:
        if start[sn] != tn or end[tn] != sn:
            ok = False
            break

print("Yes" if ok else "No")
