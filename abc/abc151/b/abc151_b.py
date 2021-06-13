N, K, M = map(int, input().split())
A = list(map(int, input().split()))

th = N * M
total = sum(A)

if total + K < th:
    print(-1)
    exit()

print(max(0, th - total))
