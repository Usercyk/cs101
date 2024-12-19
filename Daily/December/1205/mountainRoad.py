from heapq import heappop, heappush


directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
INF = float("inf")


def dijkstra(start_x, start_y, end_x, end_y):
    global m, n, terrian
    if terrian[start_x][start_y] == "#" or terrian[end_x][end_y] == "#":
        return "NO"
    pq = [(0, start_x, start_y)]
    distance = [[INF]*n for _ in range(m)]
    distance[start_x][start_y] = 0

    while pq:
        d, x, y = heappop(pq)
        if x == end_x and y == end_y:
            return d
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < m and 0 <= ny < n and terrian[nx][ny] != "#":
                nd = d+abs(terrian[nx][ny]-terrian[x][y])
                if nd < distance[nx][ny]:
                    distance[nx][ny] = nd
                    heappush(pq, (nd, nx, ny))
    return "NO"


m, n, p = map(int, input().split())
terrian = [list(map(lambda x: x if x == "#" else int(x), input().split()))
           for _ in range(m)]
for _ in range(p):
    sx, sy, ex, ey = map(int, input().split())
    print(dijkstra(sx, sy, ex, ey))
