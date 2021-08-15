N = int(input())
A = list(map(int, input().split()))

total = sum(A)

diff_min = 1 << 60
snuke = 0
arai = total

for i in range(N - 1):
    snuke += A[i]
    arai -= A[i]
    diff = abs(snuke - arai)
    diff_min = min(diff_min, diff)

print(diff_min)
