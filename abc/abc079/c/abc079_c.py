from itertools import product

A, B, C, D = input()

for op in product(['+', '-'], repeat=3):
    eq = A + op[0] + B + op[1] + C + op[2] + D
    x = eval(eq)
    if x == 7:
        print(eq + '=7')
        exit()
