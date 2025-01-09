while True:
    n = int(input())
    if n == 0:
        break
    tian = sorted(map(int, input().split()))
    king = sorted(map(int, input().split()))
    res = 0
    lt, rt = 0, n-1
    lk, rk = 0, n-1
    while n:
        if tian[rt] > king[rk]:
            res += 200
            rt -= 1
            rk -= 1
        elif tian[rt] < king[rk]:
            res -= 200
            lt += 1
            rk -= 1
        else:
            if tian[lt] > king[lk]:
                res += 200
                lt += 1
                lk += 1
            else:
                if tian[lt] < king[rk]:
                    res -= 200
                lt += 1
                rk -= 1
        n -= 1
    print(res)
