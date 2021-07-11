from math import factorial

L = int(input())
l = L - 1
print(factorial(l) // (factorial(11) * factorial(l - 11)))
