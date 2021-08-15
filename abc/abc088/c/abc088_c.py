C = [[None] * 3 for i in range(3)]
for i in range(3):
    C[i][0], C[i][1], C[i][2] = map(int, input().split())

if not C[0][0] - C[0][1] == C[1][0] - C[1][1] == C[2][0] - C[2][1]:
    print("No")
    exit()

if not C[0][1] - C[0][2] == C[1][1] - C[1][2] == C[2][1] - C[2][2]:
    print("No")
    exit()

if not C[0][2] - C[0][0] == C[1][2] - C[1][0] == C[2][2] - C[2][0]:
    print("No")
    exit()

print("Yes")
