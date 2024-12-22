# Assignment #D: 十全十美

Updated GMT+8 Dec 19, 2024

2024 fall, Complied by 曹以楷 物理学院

## 1. 题目

### 02692: 假币问题

brute force, http://cs101.openjudge.cn/practice/02692

思路：这个题好像很久之前就有人在群里问了。

这题本质上是一道线性代数题，首先一个简单的理解：左边的重量-右边的重量的符号和天平往哪边倾斜一一对应。
那么我们可以用1表示放到天平左边，用-1表示放到右边，用0表示不放。则一次测量的结果便是$$\sum_{i=1}^{12}a_im_i, a_i\in\{-1,0,1\}$$
而根据题意，除了假币，所有硬币的质量一样，即
设真币：$m_i=m_0$，假币：$m_i=m_0+m_x$
$$\sum_{i=1}^{12}a_im_i=m_0\sum_{i=1}^{12}a_i+m_xa_j$$
为了保证尽快的找到假币，我们可以令$\sum_{i=1}^{12}a_i=0$，也就是题目中左右天平均放一样多的硬币。此时某一次测量的结果就是$$\sum_{i=1}^{12}a_im_i=m_xa_j$$
当然，由于我们只需要看符号来决定天平偏向，我们可以对其进行归一化，换言之，$m_x\in\{1,-1\}$。
那么$m_xa_j\in\{\pm 1,0\}$，也就是我们可以同样用$\pm 1$或$0$来标记测量偏向。也就是代码中的`balToRes`。
一次测量无法完全确定，那么多次测量的结果可以写成一个矩阵，有$$A\vec{m}=\vec{r}$$
根据我们上述的讨论，只有第$j$列假币的结果得到的矩阵乘法不为$0$，此时天平测量结果矢量满足$$\vec{r}=m_x(a_{j1},a_{j2},a_{j3})^T$$
那么代码上，我们只需要找到$\vec{r}$对应的$(a_{j1},a_{j2},a_{j3})^T$就行，这两个矢量是$m_x\in\{1,-1\}$倍，即相同或相反，分别对应不同的假币轻重。
当然我们必须要考虑到，找不到和找到多个的情况。第一种情况是有多枚假币，题目说了不会出现。第二种情况就是数据给错了，目前的信息无法确定，题目也说了不会出现。所以非常完美。

代码：

```python
balToRes = {"up": 1, "even": 0, "down": -1}

for _ in range(int(input())):
    a = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [],
         'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': []}
    res = []
    reverse_res = []

    for _ in range(3):
        left, right, bal = input().split(" ")[:3]

        for k in a:
            if k in left:
                a[k].append(1)
            elif k in right:
                a[k].append(-1)
            else:
                a[k].append(0)
        res.append(balToRes[bal])
        reverse_res.append(-balToRes[bal])

    for k, v in a.items():
        if v == res:
            print(f"{k} is the counterfeit coin and it is heavy.")
            break
        elif v == reverse_res:
            print(f"{k} is the counterfeit coin and it is light.")
            break

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241219154335.png)

### 01088: 滑雪

dp, dfs similar, http://cs101.openjudge.cn/practice/01088

思路：用dfs找到某个点的最长路径，然后存起来，最后统一取最长的就行。

代码：

```python
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

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241219162047.png)

### 25572: 螃蟹采蘑菇

bfs, dfs, http://cs101.openjudge.cn/practice/25572/

思路：这就和普通的迷宫差不多，只是记录位置的时候需要记录两个而已

代码：

```python
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

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241219173004.png)

### 27373: 最大整数

dp, http://cs101.openjudge.cn/practice/27373/

思路：首先，根据最大最小整数那题得到的排序方式进行排序；随后由于存在长度限制，导致原有的排序不一定都对，这就导致我们需要使用到dp了，提前排序是为了保证状态转移方程的正确性。利用`key=lambda x: (len(x), x)`直接比较dp结果，而不是先转`int`再转`str`这么麻烦。

注：数据中似乎没有考虑到0这种可能，导致我最后直接`print(dp[n][m])`也过了。


代码：

```python
from math import ceil
m, n, l, = int(input()), int(input()), input().split()
max_len = max(len(p) for p in l)
l.sort(key=lambda x: x*(ceil(2*max_len/len(x))), reverse=True)

weights = [len(p) for p in l]
# dp[i][j] = max weight of the first i elements with j characters
dp = [["" for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if weights[i-1] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] +
                           l[i-1], key=lambda x: (len(x), x))
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][m] if dp[n][m] else "0")

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241219175016.png)

### 02811: 熄灯问题

brute force, http://cs101.openjudge.cn/practice/02811

思路：枚举第一行的所有可能按法，每种不同的按法对应一种最后一行的情况

代码：

```python
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

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241219184805.png)

### 08210: 河中跳房子

binary search, greedy, http://cs101.openjudge.cn/practice/08210/

思路：二分查找可能的最短距离

代码：

```python
L, N, M = map(int, input().split())
stones = [0]
for _ in range(N):
    stones.append(int(input()))
stones.append(L)

left, right = 0, L
while left < right:
    mid = (left+right)//2
    cnt, pos = 0, 0
    for i in range(1, len(stones)):
        if stones[i]-stones[pos] < mid:
            cnt += 1
        else:
            pos = i
    if cnt > M:
        right = mid
    else:
        left = mid + 1

print(left-1)

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241219190007.png)

## 2. 学习总结和收获

vscode刚刚更新了之后的最新版本内置了copilot，我做半小时的题它3s就做出来了ToT

要考试了！！！！！！！
考试难度是会比这次作业难还是简单啊
