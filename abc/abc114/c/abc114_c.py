from itertools import product

N = int(input())

L = ['3', '5', '7']
nlen = len(str(N))
    
A = []
for i in range(3, nlen + 1):
    for j in product(L, repeat=i):
        s = ''.join(j)
        if s.count('3') == 0 or s.count('5') == 0 or s.count('7') == 0:
            continue
        A.append(int(s))

ok = -1
ng = len(A)
while abs(ng - ok) > 1:
    mid = (ng + ok) // 2
    if A[mid] <= N:
        ok = mid
    else:
        ng = mid

print(ok + 1)
