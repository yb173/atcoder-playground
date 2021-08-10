N = int(input())
S = input()

# 左側にある W の数の総和
left = [0] * (N + 1)
# 右にある E の数の総和
right = [0] * (N + 1)

left[0] = 0
for i in range(N):
    w = 1 if S[i] == 'W' else 0
    left[i + 1] = left[i] + w

right[N] = 0
for i in reversed(range(N)):
    e = 1 if S[i] == 'E' else 0
    right[i] = right[i + 1] + e

ans = 1 << 60
for i in range(N):
    now = left[i] + right[i + 1]
    ans = min(ans, now)

print(ans)
