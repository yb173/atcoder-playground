N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
pre_dish = -1
for i in range(N):
    dish = A[i] # 料理番号
    ans += B[dish - 1]
    if dish - 1 == pre_dish:
        ans += C[dish - 2]
    pre_dish = dish

print(ans)
