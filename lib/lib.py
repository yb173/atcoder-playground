import sys
def debug_var(var):
    """デバッガ

    変数名とその値を標準エラー出力に出力します．

    Args:
        var (int, str, obj): 数値，文字列，配列
    """
    for k,v in globals().items():
        if id(v) == id(var):
            name = k
    print(name + ' = ' + str(var), file=sys.stderr)

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

def compute_divisors(num: int):
    """約数を求める関数

    引数で与えられた整数の約数の一覧をセット型で返却します．
    計算量は O(N^0.5) です．

    Args:
        num (int): 約数を求める整数

    Returns:
        set<int>: 約数のセット
    """
    divisors = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)
    return divisors



### a - z の set
alphabet = "abcdefghijklmnopqrstuvwxyz"
alp = set(alphabet)
alp = list(alphabet)
### A - Z の set
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALP = set(ALPHABET)
ALP = list(ALPHABET)
