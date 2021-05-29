
A, B = input().split()

a_sum = int(A[0]) + int(A[1]) + int(A[2])
b_sum = int(B[0]) + int(B[1]) + int(B[2])

print(a_sum if a_sum > b_sum else b_sum)
