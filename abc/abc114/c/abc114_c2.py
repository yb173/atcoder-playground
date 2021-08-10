def dfs(x):
    if x >= 10 ** 9:
        return
    xs = str(x)
    if xs.count('3') != 0 and xs.count('5') != 0 and xs.count('7') != 0:
        A.append(x)
    dfs(10 * x + 3)
    dfs(10 * x + 5)
    dfs(10 * x + 7)
    
N = int(input())

A = [0]
dfs(0)
A.sort()
A.append(10 ** 9)

for i in range(len(A) - 1):
    if A[i] <= N and N < A[i + 1]:
        print(i)
        exit()
