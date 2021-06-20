x, y, z = map(int, input().split())
total = z
cnt = 0
while True:
    total += z + y
    if total > x:
        break
    cnt += 1

print(cnt)
