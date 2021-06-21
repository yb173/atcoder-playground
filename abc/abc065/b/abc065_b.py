N = int(input())
a = [int(input()) for _ in range(N)]

count = 0
i = 0
while count < 100000:
    count += 1
    if a[i] == 2:
        print(count)
        exit()
    i = a[i] - 1

print(-1)
