def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    max_a = max(a)
    min_b = min(b)

    ans = 0
    if min_b - max_a < 0:
        ans = 0
    else:
        ans = min_b - max_a + 1

    print(ans)

    return

if __name__ == '__main__':
    main()
