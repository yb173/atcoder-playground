S = input()
l = len(S)

if not S[0] == 'A':
    print("WA")
    exit()

if not S[1].islower():
    print("WA")
    exit()

if not S[l - 1].islower():
    print("WA")
    exit()
    
cnt = 0
for i in range(2, l - 1):
    if S[i] == 'C':
        cnt += 1
    else:
        if not S[i].islower():
            print("WA")
            exit()
if not cnt == 1:
    print("WA")
    exit()

print("AC")
