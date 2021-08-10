S = input()
l = len(S)

A = [0 if i % 2 == 0 else 1 for i in range(l)]
B = [0 if i % 2 == 1 else 1 for i in range(l)]

cnt1 = 0
for s, a in zip(S, A):
    if not int(s) == a:
        cnt1 += 1

cnt2 = 0
for s, b in zip(S, B):
    if not int(s) == b:
        cnt2 += 1

print(min(cnt1, cnt2))