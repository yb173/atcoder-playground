N = int(input())
A = list(map(int, input().split()))

c = [0] * 10 ** 5
for a in A:
    c[a] += 1

ans = 0
for i in range(1, len(c) - 1):
    now = c[i - 1] + c[i] + c[i + 1]
    ans = max(ans, now)
print(ans)
