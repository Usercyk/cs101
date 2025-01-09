directions = ((0, 1), (0, -1), (-1, 0), (1, 0))


def bfs():
    if grid[0][0] == 1:
        return 0
    visited[0][0] = True
    steps = [[(0, 0)]]
    step = 1
    global n, m
    while step < 2500:
        last = steps[-1]
        new = []
        for x, y in last:
            for d in directions:
                nx = x+d[0]
                ny = y+d[1]
                if any((nx < 0, ny < 0, nx >= n, ny >= m)):
                    continue
                if grid[nx][ny] == 1:
                    return step
                if grid[nx][ny] == 2:
                    continue
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    new.append((nx, ny))
        steps.append(new)
        step += 1
    return "NO"


n, m = map(int, input().split())
grid = []
visited = [[False]*m for _ in range(n)]
for _ in range(n):
    grid.append(list(map(int, input().split())))
print(bfs())
