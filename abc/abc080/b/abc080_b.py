def digitSum(N: int):
    """各桁の和を求める関数

    引数で与えられた整数の和を返却します．
    計算量は O(len(N))) です．

    Args:
        num (int): 整数

    Returns:
        int: 各桁の和
    """
    sum = 0
    while N > 0:
        q, mod = divmod(N, 10)
        sum += mod
        N = q
    return sum

N = int(input())
total = digitSum(N)
print("Yes" if N % total == 0 else "No")
