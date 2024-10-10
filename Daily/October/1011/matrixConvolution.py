m, n, p, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
b = [list(map(int, input().split())) for _ in range(p)]

for i in range(m+1-p):
    resi = []
    for j in range(n+1-q):
        res = 0
        for k in range(p):
            for l in range(q):
                res += a[i+k][j+l]*b[k][l]
        resi.append(res)
    print(*resi)
