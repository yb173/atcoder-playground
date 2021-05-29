def main():
    a, b, c = map(int, input().split())

    if a**2 + b**2 < c**2:
        print("Yes")
    else:
        print("No")
    return

if __name__ == '__main__':
    main()
