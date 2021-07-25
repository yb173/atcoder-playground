N = int(input())
A = [int(input()) for _ in range(N)]
B = sorted(A)

fir = B[-1]
sec = B[-2]

for a in A:
    if a == fir:
        print(sec)
    else:
        print(fir)
