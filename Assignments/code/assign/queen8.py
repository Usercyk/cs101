def solve():
    col = [True for _ in range(10)]
    l = [True for _ in range(20)]
    r = [True for _ in range(20)]

    sol = []
    pos = ["0" for _ in range(8)]

    def dfs(step):
        nonlocal sol
        if step > 8:
            sol.append("".join(pos))
            return
        for i in range(1, 9):
            if col[i] and l[i-step+8] and r[i+step]:
                col[i], l[i-step+8], r[i+step] = False, False, False
                pos[step-1] = str(i)
                dfs(step+1)
                col[i], l[i-step+8], r[i+step] = True, True, True

    dfs(1)
    return sol


solutions = solve()
for _ in range(int(input())):
    print(solutions[int(input())-1])
