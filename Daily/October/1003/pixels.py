n, m, k = map(int, input().split())
a = [[0 for _ in range(m)] for _ in range(n)]
flag = False
for p in range(k):
    s = input()
    if flag:
        continue
    i, j = map(int, s.split())
    if a[i-1][j-1]:
        continue
    a[i-1][j-1] = 1
    if i >= 2 and j >= 2:
        if a[i-2][j-2] == a[i-2][j-1] == a[i-1][j-2] == 1:
            print(p+1)
            flag = True
            continue
    if i >= 2 and j <= m-1:
        if a[i-2][j-1] == a[i-1][j] == a[i-2][j] == 1:
            print(p+1)
            flag = True
            continue
    if i <= n-1 and j >= 2:
        if a[i-1][j-2] == a[i][j-1] == a[i][j-2] == 1:
            print(p+1)
            flag = True
            continue
    if i <= n-1 and j <= m-1:
        if a[i][j] == a[i-1][j] == a[i][j-1] == 1:
            print(p+1)
            flag = True
            continue
if not flag:
    print(0)
