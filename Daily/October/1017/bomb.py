a, b, k = map(int, input().split())
bombs = [[1 for _ in range(b)] for _ in range(a)]
for _ in range(k):
    r, s, p, t = map(int, input().split())
    imin = max(r-(p-1)//2, 1)-1
    imax = min(r+(p-1)//2, a)-1
    jmin = max(s-(p-1)//2, 1)-1
    jmax = min(s+(p-1)//2, b)-1
    for i in range(a):
        for j in range(b):
            if imin <= i <= imax and jmin <= j <= jmax:
                bombs[i][j] &= t
            else:
                bombs[i][j] &= 1-t
print(sum((sum(x) for x in bombs)))
