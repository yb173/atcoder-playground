A, B = map(int, input().split())

if A == B:
    print(2 * A)
else:
    print(2 * max(A, B) - 1)
