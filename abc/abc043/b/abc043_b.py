s = input()
ans = []
for item in s:
    if item == '0' or item == '1':
        ans.append(item)
    if item == 'B' and len(ans) > 0:
        ans.pop()
print(''.join(ans))
