import sys
directions = ((0, 1), (0, -1), (-1, 0), (1, 0))


def dfs_iterative(x, y, h, m, n, grid, water_height):
    stack = [(x, y)]
    water_height[x][y] = h

    while stack:
        cx, cy = stack.pop()

        for dx, dy in directions:
            nx = cx + dx
            ny = cy + dy
            if (0 <= nx < m and 0 <= ny < n and
                grid[nx][ny] < h and
                    water_height[nx][ny] < h):
                water_height[nx][ny] = h
                stack.append((nx, ny))


data = sys.stdin.read().split()
idx = 0
k = int(data[idx])
idx += 1
results = []

for _ in range(k):
    m, n = map(int, data[idx:idx + 2])
    idx += 2

    grid = []
    for i in range(m):
        grid.append(list(map(int, data[idx:idx + n])))
        idx += n

    water_height = [[0] * n for _ in range(m)]

    i, j = map(lambda x: int(x)-1, data[idx:idx + 2])
    idx += 2

    p = int(data[idx])
    idx += 1

    for _ in range(p):
        x, y = map(lambda x: int(x)-1, data[idx:idx + 2])
        idx += 2
        if grid[x][y] <= grid[i][j]:
            continue
        dfs_iterative(x, y, grid[x][y], m, n, grid, water_height)
    results.append("Yes" if water_height[i][j] > 0 else "No")

sys.stdout.write("\n".join(results) + "\n")
