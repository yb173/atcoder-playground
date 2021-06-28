N = int(input())
S = input()
x = 0
x_max = 0
for i in range(N):
    x += 1 if S[i] == 'I' else -1
    x_max = max(x_max, x)

print(x_max)
