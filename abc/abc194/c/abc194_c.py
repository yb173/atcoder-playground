N = int(input())
A = list(map(int, input().split()))

M = 200
cnt = [0 for i in range(2 * M + 1)]

for a in A:
    # 添え字がマイナスにならないように M をプラスする
    cnt[a + M] += 1

ans = 0
for i in range(2 * M + 1):
    for j in range(i + 1, 2 * M + 1):
        ans += cnt[i] * cnt[j] * (i - j) ** 2

print(ans)
