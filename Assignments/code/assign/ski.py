from itertools import product

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))


def dfs(x, y):
    global dp, grid, R, C
    if dp[x][y] != -1:
        return dp[x][y]

    max_length = 1
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] < grid[x][y]:
            max_length = max(max_length, 1+dfs(nx, ny))
    dp[x][y] = max_length
    return dp[x][y]


def solve():
    global dp, grid, R, C
    if not grid or not grid[0]:
        return 0

    ans = 0
    for i, j in product(range(R), range(C)):
        ans = max(ans, dfs(i, j))

    return ans


R, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]
dp = [[-1]*C for _ in range(R)]

print(solve())
