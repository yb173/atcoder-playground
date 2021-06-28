s = input()

for i in range(len(s)):
    if s[i] == 'A':
        start = i
        break

for j in reversed(range(len(s))):
    if s[j] == 'Z':
        end = j
        break

print(end - start + 1)
