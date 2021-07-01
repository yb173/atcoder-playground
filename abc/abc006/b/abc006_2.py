n = int(input())

a = [0] * 1000001
a[2] = 1

for i in range(3, n):
    a[i] = (a[i - 1] + a[i - 2] + a[i - 3]) % 10007

print(a[n - 1])
