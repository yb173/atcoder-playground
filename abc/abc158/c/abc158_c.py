A, B = map(int, input().split())

for i in range(1, 12000):
    if i * 8 // 100 == A and i * 10 // 100 == B:
        print(i)
        exit()

print(-1)
