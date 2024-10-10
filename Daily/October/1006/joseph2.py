while True:
    n, p, m = map(int, input().split())
    if n == p == m == 0:
        break
    kids = list(range(1, n+1))
    res = []
    left = n
    cur = p-1
    while left:
        nex = (cur+m-1) % left
        res.append(str(kids[nex]))
        kids.pop(nex)
        cur = nex if nex < left-1 else 0
        left -= 1
    print(",".join(res))
