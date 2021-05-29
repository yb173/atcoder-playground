import math

def main():
    A, B = map(int, input().split())

    kokei = A + B
    shibo = B
    
    if kokei >= 15 and shibo >= 8:
        print("1")
    elif kokei >= 10 and shibo >= 3:
        print("2")
    elif kokei >= 3:
        print("3")
    else:
        print("4")

    return

if __name__ == '__main__':
    main()
