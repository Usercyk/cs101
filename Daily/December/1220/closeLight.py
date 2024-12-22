def toggle(grid, x, y):
    if 0 <= x < 5 and 0 <= y < 6:
        grid[x][y] = 1 - grid[x][y]


def press_button(grid, x, y):
    toggle(grid, x, y)
    toggle(grid, x - 1, y)
    toggle(grid, x + 1, y)
    toggle(grid, x, y - 1)
    toggle(grid, x, y + 1)


def solve_lights(grid):
    for i in range(64):
        temp_grid = [row[:] for row in grid]
        first_press = list(map(int, bin(i)[2:].zfill(6)))
        res = [[0]*6 for _ in range(5)]
        res[0] = first_press
        for j in range(6):
            if first_press[j] == 1:
                press_button(temp_grid, 0, j)
        for j in range(1, 5):
            for k in range(6):
                if temp_grid[j - 1][k] == 1:
                    press_button(temp_grid, j, k)
                    res[j][k] = 1
        if not any(temp_grid[4]):
            return res
    return []


grid = []
for _ in range(5):
    grid.append(list(map(int, input().split())))
result = solve_lights(grid)
for row in result:
    print(" ".join(map(str, row)))
