N = int(input())
A = list(map(int, input().split()))

for item in A:
    if item % 2 != 0:
        continue
    if item % 3 != 0 and item % 5 != 0:
        print("DENIED")
        exit()

print("APPROVED")
