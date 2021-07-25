N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

Atot = [0] * 201010
Atot[0] = 0
for i in range(N):
    Atot[i + 1] = Atot[i] + A[i]

Btot = [0] * 201010
Btot[0] = 0
for i in range(M):
    Btot[i + 1] = Btot[i] + B[i]

###  O(MN) = 10^10 だから間に合わない
# ans = 0
# for i in range(N):
#     for j in range(M):
#         tmp_ans = Atot[i + 1] + Btot[j + 1]
#         if tmp_ans <= K:
#             ans = max(ans, i + j + 2)

### 尺取法
ans = 0
ok = M
for a in range(N + 1):
    while (0 <= ok and K < Atot[a] + Btot[ok]):
        ok -= 1
    if 0 <= ok:
       ans = max(ans, a + ok) 

print(ans)
