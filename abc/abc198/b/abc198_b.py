def main():
    n = str(input())
    
    ok = False
    for i in range(len(n)):
        # 文字列反転
        rn = n[::-1] 
        if n == rn:
            ok = True
            break
        n = '0' + n    

    if ok:
        print("Yes")
    else:
        print("No")

    return

if __name__ == '__main__':
    main()
