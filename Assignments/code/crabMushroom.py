from collections import deque
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))


def solve(n, grid):
    start, end = find_start_end(n, grid)
    q = deque([start])
    visited = set()
    visited.add(tuple(start))
    flag = False
    while q:
        if flag:
            break
        current = q.popleft()
        if end in current:
            flag = True
            break
        for dx, dy in directions:
            nx1, ny1 = current[0][0]+dx, current[0][1]+dy
            nx2, ny2 = current[1][0]+dx, current[1][1]+dy
            if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= nx2 < n and 0 <= ny2 < n:
                if grid[nx1][ny1] != 1 and grid[nx2][ny2] != 1:
                    next_state = [(nx1, ny1), (nx2, ny2)]
                    if tuple(next_state) not in visited:
                        visited.add(tuple(next_state))
                        q.append(next_state)
    return flag


def find_start_end(n, grid):
    start = []
    end = (-1, -1)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 5:
                start.append((i, j))
            elif grid[i][j] == 9:
                end = (i, j)
    return start, end


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
print("yes" if solve(n, grid) else "no")
