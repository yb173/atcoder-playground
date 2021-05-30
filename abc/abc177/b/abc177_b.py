S = input()
T = input()

ans = len(T)
for i in range(len(S) - len(T) + 1):
    diff = len(T)
    for j in range(len(T)):
        if S[i + j] == T[j]:
            diff -= 1
        else:
            continue
    ans = min(ans, diff)
        
print(ans)
