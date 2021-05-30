N = input()

sum = 0
for i in range(len(N)):
    sum += int(N[i])

print("Yes" if sum % 9 == 0 else "No")
