while True:
    R, n = map(int, input().split())
    if R == n == -1:
        break
    x = sorted(map(int, input().split()))
    t = -10000
    left = -10000
    res = 0
    for p in x:
        if p <= left+R:
            t = p
            continue
        if p <= t+R:
            continue
        res += 1
        left = p
        t = p
    print(res)
