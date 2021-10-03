S = input()
T = input()

cnt = 0
a = []
b = []
for i in range(len(S)):
    if not S[i] == T[i]:
        cnt += 1
        a.append((S[i], T[i]))
        b.append(i)

if cnt == 0:
    print("Yes")
    exit()

if cnt == 2:
    if (a[0][0] == a[1][1]) and (a[0][1] == a[1][0]):
        if abs(b[0] - b[1]) == 1:
            print("Yes")
            exit()

print("No")
