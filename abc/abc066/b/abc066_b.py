import inspect
import re
import sys

def debug(var):
    cf = inspect.currentframe()
    cfc = cf.f_code
    bf = cf.f_back
    bfi = inspect.getframeinfo(bf)
    e_0 = bfi.code_context[0]
    matched = re.match(r'.*{0}\((.+)\)[^)]*'.format(cfc.co_name), e_0)
    arg_name = matched.group(1)
    print(arg_name + ' = ' + str(var), file=sys.stderr)

S = input()
debug(S)
debug(len(S))

while len(S) > 1:
    S = S[:-2]
    debug(S)
    l = len(S)
    if S[:l // 2] == S[l // 2:]:
        print(l)
        exit()
