N = int(input())
A = list(map(int, input().split()))
A.sort()

if A[0] == 0:
    print(0)
    exit()

ans = 1
for a in A:
    ans *= a
    if ans > 10**18:
        print(-1)
        exit()

print(ans)
    