A, B, C = map(int, input().split())
wa = A + B
sa = A - B
if wa == sa == C:
    print("?")
elif wa == C:
    print("+")
elif sa == C:
    print("-")
else:
    print("!")
