N = int(input())

cnt = 0
for i in range(1, N + 1):
    if not '7' in str(i) and not '7' in str(oct(i)):
        cnt += 1

print(cnt)
