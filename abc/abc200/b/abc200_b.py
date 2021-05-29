def main():
    N, K = map(int, input().split())

    for i in range(K):
        q, mod = divmod(N, 200)
        ans = 0
        if mod == 0:
            N = q
        else:
            tmp = str(N) + '200'
            N = int(tmp)
    print(N)

    return

if __name__ == '__main__':
    main()
