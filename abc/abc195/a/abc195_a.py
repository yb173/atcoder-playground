def main():
    m, h = map(int, input().split())

    mod = h % m

    if mod == 0:
        print("Yes")
    else:
        print("No")

    return

if __name__ == '__main__':
    main()
