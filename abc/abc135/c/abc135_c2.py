N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(N):
    lft = min(B[i], A[i])
    ans += lft
    B[i] -= lft
    A[i] -= lft
    
    rht = min(B[i], A[i + 1])
    ans += rht
    B[i] -= rht
    A[i + 1] -= rht

print(ans)
