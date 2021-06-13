A = [int(input()) for _ in range(5)]
A.sort()
k = int(input())
if A[4] - A[0] > k:
    print(":(")
else:
    print("Yay!")
