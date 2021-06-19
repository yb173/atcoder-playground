N, X = map(int, input().split())
m = [int(input()) for _ in range(N)]
m.sort()
sum_1 = sum(m)
diff = X - sum_1
rest = diff // m[0]
print(N + rest)
