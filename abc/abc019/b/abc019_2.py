s = input()

prev = None
ans = []
cnt = 1
for v in s:
    if prev is None:
        prev = v
        continue

    if prev == v:
        cnt += 1
    else:
        ans.append(prev + str(cnt))
        cnt = 1

    prev = v

ans.append(prev + str(cnt))

print(''.join(ans))
