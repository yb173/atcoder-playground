a, b = map(int, input().split())
if a % 3 == 0:
    print("Possible")
    exit()
if b % 3 == 0:
    print("Possible")
    exit()
if (a + b) % 3 == 0:
    print("Possible")
    exit()

print("Impossible")
