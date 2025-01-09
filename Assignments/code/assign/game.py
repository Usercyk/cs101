
from queue import Queue

directions = ((0, 1), (0, -1), (1, 0), (-1, 0))


def is_valid(x, y, w, h, board, x2, y2, visited):
    if any((x < 0, y < 0, x > w+1, y > h+1)):
        return False
    if visited[y][x]:
        return False
    if board[y][x] != "X":
        return True
    return x == x2 and y == y2


def bfs(x1, y1, x2, y2, w, h, board):
    q = Queue()
    visited = [[False]*(w+2) for _ in range(h+2)]

    visited[y1][x1] = True
    q.put((x1, y1, 0))

    while not q.empty():
        x, y, step = q.get()
        for dx, dy in directions:
            nx, ny, ns = x+dx, y+dy, step+1
            while is_valid(nx, ny, w, h, board, x2, y2, visited):
                if nx == x2 and ny == y2:
                    print(f"{ns} segments.")
                    return

                visited[ny][nx] = True
                q.put((nx, ny, ns))
                nx += dx
                ny += dy
    print("impossible.")


def main():
    n = 1
    while True:
        w, h = map(int, input().split())
        if w == h == 0:
            break
        board = [" "*(w+2)]
        for _ in range(h):
            board.append(" "+input()+" ")
        board.append(" "*(w+2))
        print(f"Board #{n}:")
        m = 1
        while True:
            x1, y1, x2, y2 = map(int, input().split())
            if x1 == y1 == x2 == y2 == 0:
                break
            print(f"Pair {m}: ", end="")

            bfs(x1, y1, x2, y2, w, h, board)

            m += 1
        n += 1
        print()


main()
