def countDivide2(x: int):
    cnt = 0
    while x > 0:
        if x % 2 != 0:
            return cnt
        cnt += 1
        x //= 2
    return cnt

N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(N):
    ans += countDivide2(A[i])
print(ans)
