import math

def main():
    s = input()
    
    d = {}
    aaa = 0
    d['0'] = '0'
    d['1'] = '1'
    d['6'] = '9'
    d['8'] = '8'
    d['9'] = '6'

    ans = ""
    for i in range(len(s)):
        ans = d[s[i]] + ans
    print(ans)

    return

if __name__ == '__main__':
    main()
