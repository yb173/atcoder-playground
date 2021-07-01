N = int(input())
A = [int(input()) for _ in range(N)]
A.sort(reverse = True)
d = list(dict.fromkeys(A))
print(d[1])
