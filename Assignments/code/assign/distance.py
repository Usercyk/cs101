from collections import deque
from itertools import product
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))


def dye(x, y, board, island1, color=2):
    board[x][y] = color
    island1.append((x, y))
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
            dye(nx, ny, board, island1, color)


def bfs(board, island1, color=2):
    d = 0
    queue = island1
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] == 1:
                        return d
                    if board[nx][ny] == 0:
                        board[nx][ny] = color
                        queue.append((nx, ny))
        d += 1
    return d


n = int(input())
board = [list(map(int, input())) for _ in range(n)]
island1 = deque()

for i, j in product(range(n), range(n)):
    if board[i][j] == 1:
        dye(i, j, board, island1)
        print(bfs(board, island1))
        break
