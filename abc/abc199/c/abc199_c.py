N = int(input())
S = list(input())
Q = int(input())

flipped = False
for i in range(Q):
    T, A, B = map(int, input().split())
    A -= 1
    B -= 1
    if T == 1:
        if  flipped:
            A += N
            A %= 2 * N
            B += N
            B %= 2 * N
        S[A], S[B] = S[B], S[A]
    if T == 2:
        flipped = not flipped

if flipped:
    S = S[N:] + S[:N]

print(''.join(S))
