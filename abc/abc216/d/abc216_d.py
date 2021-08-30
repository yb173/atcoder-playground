from collections import defaultdict, deque

N, M = map(int, input().split())
A = [None] * M

# キューの先頭の色が key, キューの番号の配列が value（先頭にどの色がいくつあるか）
mem = [[] for i in range(N)]

for i in range(M):
    k = int(input())
    a = list(map(lambda x: int(x) - 1, input().split()))
    A[i] = deque(a)
    mem[A[i][0]].append(i)

# ２つとも先頭にある色を管理するキュー
q = deque()
for i in range(N):
    if len(mem[i]) == 2:
        q.append(i)

while len(q) > 0:
    color = q.popleft()
    for v in mem[color]: # v はキュー番号
        A[v].popleft()
        # キューを取り出してもまだ空になっていなければ，次の色を v の先頭として mem に追加する
        if len(A[v]) > 0:
            mem[A[v][0]].append(v)
            # 追加した結果ペアになったらそれもキューに追加
            if len(mem[A[v][0]]) == 2:
                q.append(A[v][0])

for a in A:
    if not len(a) == 0:
        print("No")
        exit()        

print("Yes")
