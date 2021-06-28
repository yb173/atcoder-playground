def sum(T, P, X):
    ans = 0
    for i in range(len(T)):
        if i == P - 1:
            ans += X
            continue
        ans += T[i]
    return ans

N = int(input())
T = list(map(int, input().split()))
M = int(input())

for i in range(M):
    P, X = map(int, input().split())
    print(sum(T, P, X))
