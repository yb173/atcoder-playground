S = input()
first = int(S[:2])
second = int(S[2:])

first_mm = False
second_mm = False

if 0 < first < 13:
    first_mm = True

if 0 < second < 13:
    second_mm = True

if first_mm and not second_mm:
    print("MMYY")
elif not first_mm and second_mm:
    print("YYMM")
elif first_mm and second_mm:
    print("AMBIGUOUS")
else:
    print("NA")
