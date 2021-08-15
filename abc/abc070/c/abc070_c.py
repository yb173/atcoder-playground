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

N = int(input())
T = [int(input()) for _ in range(N)]

ans = 1
for i in range(N):
    ans = lcm(ans, T[i])

print(ans)
