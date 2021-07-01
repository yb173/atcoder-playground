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
N = int(input())
debug(S)
for i in range(N):
    l, r = map(int, input().split())
    debug(l)
    debug(r)
    debug(S[:l - 1])
    debug(S[r:])
    debug(S[l - 1:r])
    debug(S[l - 1:r][::-1])
    S = S[:l - 1] + S[l - 1:r][::-1] + S[r:]
    debug(S)
print(S)
