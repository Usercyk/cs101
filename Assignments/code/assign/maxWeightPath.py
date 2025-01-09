directions = ((0, 1), (0, -1), (-1, 0), (1, 0))


def dfs(x, y, val, path):
    global weight, n, m, ans
    if x == n-1 and y == m-1:
        if val > weight:
            weight = val
            ans = path
        return
    visited[x][y] = True
    for d in directions:
        nx = x+d[0]
        ny = y+d[1]
        if any((nx < 0, ny < 0, nx >= n, ny >= m)):
            continue
        if visited[nx][ny]:
            continue
        nv = val+mat[nx][ny]
        dfs(nx, ny, nv, path+[(nx, ny)])
    visited[x][y] = False


n, m = map(int, input().split())
mat = []
visited = [[False]*m for _ in range(n)]
for _ in range(n):
    mat.append(list(map(int, input().split())))
weight = -500000
ans = []
dfs(0, 0, mat[0][0], [(0, 0)])
for x, y in ans:
    print(x+1, y+1)
