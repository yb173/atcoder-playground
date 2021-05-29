import math

def main():
    N = int(input())
    A, B = [], []

    for i in range(N):
        s, t = map(int, input().split())
        A.append(s)
        B.append(t)

    ans = 1 << 60
    for i in range(N):
        for j in range(N):
            ans = min(ans, A[i] + B[j] if i == j else max(A[i], B[j]))

    print(ans)
    return

if __name__ == '__main__':
    main()
