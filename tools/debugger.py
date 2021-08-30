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



import inspect
import re
import sys
def debug(var):
    cf = inspect.currentframe()
    cfc = cf.f_code
    bf = cf.f_back
    bfi = inspect.getframeinfo(bf)
    code_context_0 = bfi.code_context[0]

    # 引数の名前を取得
    matched = re.match(r'.*{0}\((.+)\)[^)]*'.format(cfc.co_name), code_context_0)
    arg_name = matched.group(1) # 例) A, S, len(S)...

    print(arg_name + ' = ' + str(var), file=sys.stderr)
