def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]

    # 自身の H 座標
    OX = X - 1
    # 自身の W 座標
    OY = Y - 1

    if S[OX][OY] == "#":
        print("0")
        return

    ans = 1

    # H マイナス方向の探索
    for x in range(OX - 1, -1, -1):
        if S[x][OY] == "#":
            break
        ans += 1

    # H プラス方向の探索
    for x in range(OX + 1, H):
        if S[x][OY] == "#":
            break
        ans += 1

    # W マイナス方向の探索
    for y in range(OY - 1, -1, -1):
        if S[OX][y] == "#":
            break
        ans += 1

    # W プラス方向の探索
    for y in range(OY + 1, W):
        if S[OX][y] == "#":
            break
        ans += 1

    print(ans)
    return

if __name__ == '__main__':
    main()

