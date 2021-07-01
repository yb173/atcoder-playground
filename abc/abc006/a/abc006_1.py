N = input()

if '3' in N:
    print("YES")
    exit()

if int(N) % 3 == 0:
    print("YES")
    exit()

print("NO")
