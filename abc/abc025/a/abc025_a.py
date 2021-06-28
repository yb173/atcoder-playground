S = list(input())
S.sort()
N = int(input())
SS = []
for i in range(len(S)):
    for j in range(len(S)):
        SS.append(S[i] + S[j])
print(SS[N - 1])
