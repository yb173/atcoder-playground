s = input()
k = int(input())
d = set()
for i in range(len(s) - k + 1):
    d.add(s[i:i + k])

print(len(d))
