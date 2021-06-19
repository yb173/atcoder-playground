S = input()

min_diff = 1000
for i in range(len(S) - 2):
    target = int(S[i:i + 3])
    diff = abs(753 - target)
    min_diff = min(min_diff, diff)
print(min_diff)
