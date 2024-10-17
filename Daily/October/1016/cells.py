def update(a, n, m):
    b = [[0 for _ in range(m+2)] for _ in range(n+2)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            r = a[i-1][j-1]+a[i-1][j]+a[i-1][j+1]+a[i][j-1] + \
                a[i][j+1]+a[i+1][j-1]+a[i+1][j]+a[i+1][j+1]
            if r == 3 or (r == 2 and a[i][j] == 1):
                b[i][j] = 1

    for x in b[1:n+1]:
        print(*x[1:m+1])


n, m = map(int, input().split())
a = [[0 for _ in range(m+2)]]
for _ in range(n):
    a.append([0, *map(int, input().split()), 0])

a.append([0 for _ in range(m+2)])

update(a, n, m)
