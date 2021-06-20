S = input()

alphabet = "abcdefghijklmnopqrstuvwxyz"

for a in alphabet:
    if a not in S:
        print(a)
        exit()

print("None")
