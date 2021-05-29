def main():
    N = int(input())
    data = []
    for i in range(N):
        S, T = map(str, input().split())
        T = int(T)
        data.append([T, S])

    sorted_data = sorted(data, key=lambda x: x[0], reverse=True)
    print(sorted_data[1][1])
    return

if __name__ == '__main__':
    main()

