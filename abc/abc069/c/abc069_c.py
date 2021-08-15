N = int(input())
A = list(map(int, input().split()))

odd = [A[i] for i in range(N) if not A[i] % 2 == 0]
four = [A[i] for i in range(N) if A[i] % 4 == 0]

if not len(A) % 2 == 0:
    print("Yes" if len(odd) <= len(four) + 1 else "No")
else:
    print("Yes" if len(odd) <= len(four) else "No")
