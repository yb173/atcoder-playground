K, X = map(int, input().split())

ans = []
for i in range(X - K + 1, X + K):
    if i < -1000000 or 1000000 < i:
        continue
    ans.append(str(i))

print(" ".join(ans))
