N = int(input())
A = list(map(int, input().split()))

ans = 1 << 60
for bit in range(1 << (N - 1)):
    XOR = 0
    OR = 0
    for i in range(N):
        OR |= A[i]
        if bit >> i & 1:
            XOR ^= OR
            OR = 0
    XOR ^= OR
    ans = min(ans, XOR)

print(ans)
