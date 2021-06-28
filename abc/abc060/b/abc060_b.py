a, b, c = map(int, input().split())
sum = 0
for i in range(1, b + 1):
    sum += a
    if sum % b == c:
        print("YES")
        exit()

print("NO")
