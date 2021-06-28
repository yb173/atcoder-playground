from collections import defaultdict

S = input()
d = defaultdict(lambda: 0)
for item in S:
    d[item] += 1

for v in d.values():
    if not v % 2 == 0:
        print("No")
        exit()

print("Yes")
