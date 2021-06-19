A, B, C = map(int, input().split())

even = C % 2 == 0

if not even:
    if A < B:
        print("<")
    elif A > B:
        print(">")
    else:
        print("=")
else:
    A = abs(A)
    B = abs(B)
    if A < B:
        print("<")
    elif A > B:
        print(">")
    else:
        print("=")
