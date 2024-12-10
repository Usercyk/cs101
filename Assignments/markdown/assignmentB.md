# Assignment #B: Dec Mock Exam大雪前一天

Updated Dec 10, 2024

2024 fall, Complied by 曹以楷 物理学院

AC3

## 1. 题目

### E22548: 机智的股民老张

http://cs101.openjudge.cn/practice/22548/

思路：维护前缀最大值和后缀最小值

代码（考场）：

```python
*a, = map(int, input().split())
n = len(a)
inf = 1000000
sup = -10000
res_inf = []
res_sup = []
for i in range(n):
    inf = min(a[i], inf)
    res_inf.append(inf)

    sup = max(a[n-1-i], sup)
    res_sup.append(sup)

res_sup.reverse()

money = max((res_sup[i]-res_inf[i] for i in range(n)))
print(max(money, 0))

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241210103317.png)

### M28701: 炸鸡排

greedy, http://cs101.openjudge.cn/practice/28701/

思路：考察sum(t)/k，超出这个的那些直接丢进锅里不管。考场上只想到sum(t)/k…考完才想到后半句

代码：

```python
n, k = map(int, input().split())
t = sorted(map(int, input().split()))
sum_t = sum(t)

while t[-1] > sum_t/k:
    sum_t -= t.pop()
    k -= 1

print(f"{sum_t/k:.3f}")

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241210102946.png)

### M20744: 土豪购物

dp, http://cs101.openjudge.cn/practice/20744/

思路：考场上超时了，看了一眼以为要用线段树，就没做。其实直接dp即可。嗯另外既然是顺着dp下去，一个reduce就可以了，所以只需要一行。

代码（为了阅读进行了分行）：

```python
print(__import__("functools").reduce(
    lambda x, y: (y, y, y) if x[0] is None else (max(
    x[0]+y, y), max(x[0], x[1]+y, y), max(x[2], max(x[0], x[1]+y, y))),
    map(int, input().split(',')),
    (None, None, None))[2])

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241210105137.png)


### T25561: 2022决战双十一

brute force, dfs, http://cs101.openjudge.cn/practice/25561/

思路：暴力，dfs只是用于枚举出所有情况

代码（考场）：

```python
def dfs(pur, costs):
    global n, ans, m
    if pur > n:
        zhekou = [0]*m
        for i in range(m):
            for k in shops[i].keys():
                if costs[i] >= k:
                    zhekou[i] = max(zhekou[i], shops[i][k])
        total = sum(costs)
        total -= total//300*50
        total -= sum(zhekou)
        ans = min(ans, total)
        return
    shoppable = purchase[pur]
    for shop, cost in shoppable.items():
        costs[shop-1] += cost
        dfs(pur+1, costs)
        costs[shop-1] -= cost


n, m = map(int, input().split())
shops = []
shops_keys = []
purchase = [{}]
for i in range(n):
    s = input().split()
    d = {}
    for p in s:
        a, b = map(int, p.split(":"))
        d[a] = b
    purchase.append(d)
for _ in range(m):
    s = input().split()
    d = {}
    for p in s:
        a, b = map(int, p.split("-"))
        d[a] = b
    shops.append(d)

ans = float("inf")
dfs(1, [0]*m)
print(ans)

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241210103428.png)

### T20741: 两座孤岛最短距离

dfs, bfs, http://cs101.openjudge.cn/practice/20741/

思路：dfs染色一个岛后bfs开找

代码：

```python
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

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241210110831.png)

### T28776: 国王游戏

greedy, http://cs101.openjudge.cn/practice/28776

思路：按左右手乘积排序即可，考场上直接考虑了最后一个，有反例

代码：

```python
n = int(input())
ab_max = 0
xa, xb = map(int, input().split())
p = []
for _ in range(n):
    p.append(tuple(map(int, input().split())))
p.sort(key=lambda x: x[0]*x[1])
ans = 0
amul = xa
for q in p:
    ans = max(ans, amul//q[1])
    amul *= q[0]
print(ans)

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241210103854.png)

## 2. 学习总结和收获

哇到时候应该不会是这个难度吧……感觉最难的地方在于不清楚某个题应该用什么方法，比如土豪研究了一下误以为要用线段树。
