# Assignment #9: dfs, bfs, & dp

Updated Nov 21, 2024

2024 fall, Complied by <mark>曹以楷 物理学院</mark>

## 1. 题目

### 18160: 最大连通域面积

dfs similar, http://cs101.openjudge.cn/practice/18160

思路：dfs找连通图，不使用visited额外开空间了，直接修改原来的数组。不过就是想着时间复杂度上可能可以少一些常数，对连通的区域进行上色，每次遇到上色的就不重复dfs了。

代码：

```python
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

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241121192427.png)

### 19930: 寻宝

bfs, http://cs101.openjudge.cn/practice/19930

思路：标记每一步可以到达的地方，本来想着可以继续优化…但是由于`NO`打错成`No`调了半天，没这个心力继续优化了，优化方向就是没必要用visited，直接把步数标记到那个坐标上；step的遍历上限也可以改……总之林林总总的可以优化但算了……

代码：

```python
directions = ((0, 1), (0, -1), (-1, 0), (1, 0))


def bfs():
    if grid[0][0] == 1:
        return 0
    visited[0][0] = True
    steps = [[(0, 0)]]
    step = 1
    global n, m
    while step < 2500:
        last = steps[-1]
        new = []
        for x, y in last:
            for d in directions:
                nx = x+d[0]
                ny = y+d[1]
                if any((nx < 0, ny < 0, nx >= n, ny >= m)):
                    continue
                if grid[nx][ny] == 1:
                    return step
                if grid[nx][ny] == 2:
                    continue
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    new.append((nx, ny))
        steps.append(new)
        step += 1
    return "NO"


n, m = map(int, input().split())
grid = []
visited = [[False]*m for _ in range(n)]
for _ in range(n):
    grid.append(list(map(int, input().split())))
print(bfs())

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241121195753.png)

### 04123: 马走日

dfs, http://cs101.openjudge.cn/practice/04123

思路：回溯

代码：

```python
# pylint: disable=all
directions = ((1, 2), (1, -2), (-1, 2), (-1, -2),
              (2, 1), (2, -1), (-2, 1), (-2, -1))


def dfs(x, y, step):
    global ans, n, m
    if step == n*m:
        ans += 1
        return
    for d in directions:
        nx = x+d[0]
        ny = y+d[1]
        if any((nx < 0, ny < 0, nx >= n, ny >= m)):
            continue
        if visited[nx][ny]:
            continue
        visited[nx][ny] = True
        dfs(nx, ny, step+1)
        visited[nx][ny] = False


for _ in range(int(input())):
    n, m, x, y = map(int, input().split())
    ans = 0
    visited = [[False]*m for _ in range(n)]
    visited[x][y] = True
    dfs(x, y, 1)
    print(ans)

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241121200754.png)

### sy316: 矩阵最大权值路径

dfs, https://sunnywhy.com/sfbj/8/1/316

思路：没有无后效性，不能dp，直接dfs

代码：

```python
directions = ((0, 1), (0, -1), (-1, 0), (1, 0))


def dfs(x, y, val, path):
    global weight, n, m, ans
    if x == n-1 and y == m-1:
        if val > weight:
            weight = val
            ans = path
        return
    visited[x][y] = True
    for d in directions:
        nx = x+d[0]
        ny = y+d[1]
        if any((nx < 0, ny < 0, nx >= n, ny >= m)):
            continue
        if visited[nx][ny]:
            continue
        nv = val+mat[nx][ny]
        dfs(nx, ny, nv, path+[(nx, ny)])
    visited[x][y] = False


n, m = map(int, input().split())
mat = []
visited = [[False]*m for _ in range(n)]
for _ in range(n):
    mat.append(list(map(int, input().split())))
weight = -500000
ans = []
dfs(0, 0, mat[0][0], [(0, 0)])
for x, y in ans:
    print(x+1, y+1)

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241121202130.png)

### LeetCode62.不同路径

dp, https://leetcode.cn/problems/unique-paths/

思路：dp，小学奥数题，太经典了。小奥做法：标记第一行与第一列为1，随后标记每个点的数是左边和上边相加

代码：

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        p = [1]*n
        for _ in range(m-1):
            for i in range(1, n):
                p[i] = p[i]+p[i-1]
        return p[-1]

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241121202855.png)

### sy358: 受到祝福的平方

dfs, dp, https://sunnywhy.com/sfbj/8/3/539

思路：回溯上次找到的平方数，继续往后找新的平方数

代码：

```python
from math import isqrt


def isSquare(x):
    x = int(x)
    return x != 0 and isqrt(x)**2 == x


def dfs(x):
    global n, flag, s
    if x >= n-1:
        flag = True
    v = ""
    for j in range(x+1, n):
        v = v+s[j]
        if isSquare(v):
            dfs(j)


s = input()
n = len(s)
flag = False
dfs(-1)
print("Yes" if flag else "No")

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241121205342.png)

## 2. 学习总结和收获

难度一上来，码风都变了……这次大量使用了`global`，属于是c++的全局变量用多了，下意识就这么写了。

其实可以从代码里看到，模板的感觉还是挺强的，几乎就是`directions`一给，递归的部分差不多，具体只在到达递归边界后的特殊处理。




