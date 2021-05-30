N = int(input())
A = list(map(int, input().split()))
A.sort()

max_cnt = 0
ans = 0
for i in range(2, A[N - 1] + 1):
    cnt = 0
    for j in range(N):
        if A[j] % i == 0:
            cnt += 1
    if max_cnt <= cnt: ## < でもok
        max_cnt = cnt
        ans = i

print(ans)
