from itertools import product


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

print(max((a[i][j]*(1000*a[0][j]+100*a[i][m-1]+10*a[m-1][j]+a[i][0])
      for i, j in product(range(n), range(m)))))
