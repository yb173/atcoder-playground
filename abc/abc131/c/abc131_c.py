from math import gcd
def lcm(a: int, b: int):
    """最小公倍数求める関数

    a と b の最小公倍数を求めます．

    Args:
        a (int): 一つ目の値
        b (int): 二つ目の値

    Returns:
        int: a と b の最小公倍数
    """
    return a * b // gcd(a, b)

def f(x: int):
    return x - (x // C + x // D - x // lcm(C, D))

A, B, C, D = map(int, input().split())
b = f(B)
a = f(A - 1)
print(b - a)
