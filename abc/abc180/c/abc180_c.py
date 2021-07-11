def divisors_list(num: int):
    """約数の配列を求める関数

    引数で与えられた整数の約数の一覧を昇順にソートされた配列型で返却します．
    計算量は O(N^0.5 * log(N)) です．

    Args:
        num (int): 約数を求める整数

    Returns:
        list<int>: 昇順にソートされた約数の配列
    """
    divisors = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)
    return sorted(list(divisors))

N = int(input())
d = divisors_list(N)
for v in d:
    print(v)
