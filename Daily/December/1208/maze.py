from collections import deque
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))


def bfs(sx, sy, ex, ey):
    global R, C, K, maze
    q = deque([(sx, sy, 0)])
    visited = [[[False]*K for _ in range(C)] for _ in range(R)]
    visited[sx][sy][0] = True
    while q:
        x, y, t = q.popleft()
        if x == ex and y == ey:
            return t
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            nt = t+1
            if 0 <= nx < R and 0 <= ny < C:
                if maze[nx][ny] == "E":
                    return nt
                if maze[nx][ny] == "." or maze[nx][ny] == "S" or (maze[nx][ny] == "#" and nt % K == 0):
                    if not visited[nx][ny][nt % K]:
                        visited[nx][ny][nt % K] = True
                        q.append((nx, ny, nt))
    return "Oop!"


for _ in range(int(input())):
    R, C, K = map(int, input().split())
    maze = []
    for i in range(R):
        p = input()
        if "S" in p:
            sx = i
            sy = p.index("S")
        if "E" in p:
            ex = i
            ey = p.index("E")
        maze.append(p)
    print(bfs(sx, sy, ex, ey))
