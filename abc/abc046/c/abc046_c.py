N = int(input())
T = [None] * N
A = [None] * N

for i in range(N):
    t, a = map(int, input().split())
    T[i] = t
    A[i] = a

t_num = 1
a_num = 1
for i in range(N):
    tn = (t_num + T[i] - 1) // T[i]
    an = (a_num + A[i] - 1) // A[i]
    n = max(tn, an)
    t_num = T[i] * n
    a_num = A[i] * n

print(t_num + a_num)
