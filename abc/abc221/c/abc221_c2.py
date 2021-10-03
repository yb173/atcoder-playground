N = input()
L = len(N)

A = []
for i in range(L):
    A.append(N[i])

A.sort(reverse=True)

ans = 0
for bit in range(1 << L):
    f = []
    s = []
    for i in range(L):
        if bit & (1 << i):
            f.append(A[i])
        else:
            s.append(A[i])
    
    if len(f) == 0 or len(s) == 0:
        continue
    
    now = int(''.join(f)) * int(''.join(s))
    ans = max(ans, now)

print(ans)
