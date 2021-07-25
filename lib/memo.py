### 累積和
Atot = [0] * (N + 1)
Atot[0] = 0
for i in range(N):
    Atot[i + 1] = Atot[i] + A[i]

### a - z の set
alphabet = "abcdefghijklmnopqrstuvwxyz"
alp = set(alphabet)
alp = list(alphabet)

### A - Z の set
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALP = set(ALPHABET)
ALP = list(ALPHABET)
