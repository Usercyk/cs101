# pylint: disable=all
directions = ((1, 2), (1, -2), (-1, 2), (-1, -2),
              (2, 1), (2, -1), (-2, 1), (-2, -1))


def dfs(x, y, step):
    global ans, n, m
    if step == n*m:
        ans += 1
        return
    for d in directions:
        nx = x+d[0]
        ny = y+d[1]
        if any((nx < 0, ny < 0, nx >= n, ny >= m)):
            continue
        if visited[nx][ny]:
            continue
        visited[nx][ny] = True
        dfs(nx, ny, step+1)
        visited[nx][ny] = False


for _ in range(int(input())):
    n, m, x, y = map(int, input().split())
    ans = 0
    visited = [[False]*m for _ in range(n)]
    visited[x][y] = True
    dfs(x, y, 1)
    print(ans)
