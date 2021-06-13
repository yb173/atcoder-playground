N = int(input())
S = input()

if N % 2 == 1:
    print("No")
    exit()

print("Yes" if S[:N // 2] == S[N // 2:] else "No")
