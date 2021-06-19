a, b = map(int, input().split())
diff = b - a
sum = 0
for i in range(1, diff + 1):
    sum += i
print(sum - b)
