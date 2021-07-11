N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    if i == 0: continue
    diff = A[i - 1] - A[i]
    if diff > 0:    
        ans +=  diff
        A[i] += diff

print(ans)
