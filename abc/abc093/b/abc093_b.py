A, B, K = map(int, input().split())

s = set()
for i in range(K):
    if A + i <= B:
        s.add(A + i)
    if B - i >= A:
        s.add(B - i)
for item in sorted(s):
    print(item)
