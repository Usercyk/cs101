# Assignment #C: 五味杂陈

Updated Dec 14, 2024

2024 fall, Complied by 曹以楷 物理学院

## 1. 题目

### 1115. 取石子游戏

dfs, https://www.acwing.com/problem/content/description/1117/

思路：2倍及以上必胜，注意需要特判一些情况

代码：

```python
def check(a, b):
    a, b = max(a, b), min(a, b)
    return b == 0 or a == b or a/b >= 2 or not check(b, a-b)


while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    print("win" if check(a, b) else "lose")

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241214235007.png)

### 25570: 洋葱

Matrices, http://cs101.openjudge.cn/practice/25570

思路：离四条边中最近的那个就是层数

代码：

```python
from itertools import product


def get_layer(x, y, n):
    return min(x, y, n-x-1, n-y-1)


res = [0]*100
n = int(input())
onion = [list(map(int, input().split())) for _ in range(n)]
for i, j in product(range(n), range(n)):
    res[get_layer(i, j, n)] += onion[i][j]

print(max(res))

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241214235733.png)

### 1526C1. Potions(Easy Version)

greedy, dp, data structures, brute force, *1500, https://codeforces.com/problemset/problem/1526/C1

思路：能喝就喝，喝不了反悔，将优先队列里扣血最多的丢掉。

其实本来还以为是`勇士救公主`类型的（只能向右向下走，但是格子可能会扣血），其实greedy就行。

代码：

```python
from queue import PriorityQueue
n = int(input())
*a, = map(int, input().split())
hp = 0
cnt = 0
q = PriorityQueue()
for i in range(n):
    hp += a[i]
    cnt += 1
    if a[i] >= 0:
        continue
    q.put(a[i])
    if hp < 0:
        hp -= q.get()
        cnt -= 1
print(cnt)

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241215001148.png)

### 22067: 快速堆猪

辅助栈，http://cs101.openjudge.cn/practice/22067/

思路：用辅助栈存最小值

代码：

```python
import sys


class PigStack:
    def __init__(self):
        self.pigs = []
        self.min_pigs = []

    def push(self, pig):
        self.pigs.append(pig)
        if not self.min_pigs or self.min_pigs[-1] >= pig:
            self.min_pigs.append(pig)

    def pop(self):
        if self.pigs:
            if self.pigs[-1] == self.min_pigs[-1]:
                self.min_pigs.pop()
            self.pigs.pop()

    def get(self):
        if self.min_pigs:
            return self.min_pigs[-1]

    def __getitem__(self, name):
        if name == "pop":
            self.pop()
            return
        if name == "min":
            cnt = self.get()
            if cnt is not None:
                print(cnt)
            return
        self.push(int(name.split()[1]))


pig_stack = PigStack()
data = sys.stdin.read().splitlines()
for d in data:
    pig_stack[d]

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241215002750.png)

### 20106: 走山路

Dijkstra, http://cs101.openjudge.cn/practice/20106/

思路：Dijkstra就行，注意特判一下出发点到不了

代码：

```python
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

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241215004758.png)

### 04129: 变换的迷宫

bfs, http://cs101.openjudge.cn/practice/04129/

思路：添加一个时间维度即可，视为某种意义上的三维迷宫就行。当然时间维是循环的，也就是visited应该存t%K。

代码：

```python
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

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241215011311.png)

## 2. 学习总结和收获

考试的时候考这个难度真做不完/(ㄒoㄒ)/~~
捞捞，感觉要挂科哩
