INF = 1 << 60

def sol_A(H: int, W: int) -> int:
    """
    H を 3 分割する
    """
    if H < 3:
        return INF

    q, mod = divmod(H, 3)
    return 0 if mod == 0 else W

def sol_B(H: int, W: int) -> int:
    """
    W を 3 分割する
    """
    if W < 3:
        return INF

    q, mod = divmod(W, 3)
    return 0 if mod == 0 else H

def sol_C(H: int, W: int) -> int:
    """
    H を半分に切り，上下のどちらかを縦に切る
    """
    ans = INF
    for h in range(1, H):
        oh = H - h
        w = W // 2
        ow = W - w
        ma = max(oh * W, h * ow)
        mi = min(oh * W, h * w)
        diff = ma - mi
        ans = min(ans, diff)
    return ans

def sol_D(H: int, W: int) -> int:
    """
    W を半分に切り，左右のどちらかを横に切る
    """
    ans = INF
    for w in range(1, W):
        ow = W - w
        h = H // 2
        oh = H - h
        ma = max(ow * H, w * oh)
        mi = min(ow * H, w * h)
        diff = ma - mi
        ans = min(ans, diff)
    return ans

H, W = map(int, input().split())
ans = min(sol_A(H, W), sol_B(H, W), sol_C(H, W), sol_D(H, W))
print(ans)
