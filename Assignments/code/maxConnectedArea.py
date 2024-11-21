directions = ((0, 1), (0, -1), (-1, 0), (1, 0),
              (1, -1), (1, 1), (-1, -1), (-1, 1))


def dfs(x, y):
    global n, m, color, board
    board[x][y] = color
    area = 1
    for d in directions:
        nx = x+d[0]
        ny = y+d[1]
        if any((nx < 0, ny < 0, nx >= n, ny >= m)):
            continue
        if board[nx][ny] == "W":
            area += dfs(nx, ny)
    return area


for _ in range(int(input())):
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(input()))
    color = 1
    res = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == "W":
                res = max(res, dfs(i, j))
                color += 1
    print(res)
