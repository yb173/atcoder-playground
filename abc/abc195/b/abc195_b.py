INF = 1 << 60

import math

def main():
    A, B, W = map(int, input().split())
    W *= 1000
    l = INF
    r = -INF

    for i in range(1, W + 1):
        # この条件を満たす i はちょうど W キログラムにできる
        if A * i <= W and W <= B * i:
            l = min(l, i)
            r = max(r, i)

    if l == INF:
        print("UNSATISFIABLE")
    else:
        print(str(l) + " " + str(r))

    return

if __name__ == '__main__':
    main()
