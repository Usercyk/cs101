# Assignment #10: dp & bfs

Updated Nov 27, 2024

2024 fall, Complied by 曹以楷 物理学院

## 1. 题目

### LuoguP1255 数楼梯

dp, bfs, https://www.luogu.com.cn/problem/P1255

思路：斐波那契数列

代码：

```python
dp = [1, 1]
n = int(input())
for _ in range(n-1):
    dp.append(dp[-1]+dp[-2])
print(dp[n])

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241126170716.png)

### 27528: 跳台阶

dp, http://cs101.openjudge.cn/practice/27528/

思路：可以随便跳，所以每一级台阶可以选择踩不踩，直接数学求解，2的n-1次方

代码：

```python
print(1 << (int(input())-1))

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241126171000.png)

### 474D. Flowers

dp, https://codeforces.com/problemset/problem/474/D

思路：题目本身就是一个普通的“上楼梯”，但是这里不用前缀和来查询会超时

代码：

```python
MAX = 1000000007
t, k = map(int, input().split())
MOD = int(1e9+7)
MAXN = 100001
dp = [0]*MAXN
s = [0]*MAXN
dp[0] = 1
s[0] = 1
for i in range(1, MAXN):
    if i >= k:
        dp[i] = (dp[i-1]+dp[i-k]) % MOD
    else:
        dp[i] = dp[i-1] % MOD
    s[i] = (s[i-1]+dp[i]) % MOD

for _ in range(t):
    a, b = map(int, input().split())
    print((s[b]-s[a-1]+MOD) % MOD)

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241126174906.png)

### LeetCode5.最长回文子串

dp, two pointers, string, https://leetcode.cn/problems/longest-palindromic-substring/

思路：马拉车算法（Manacher）

首先一个比较基础的想法是研究以某一个位置为中心的回文串，但考虑到可能存在`aba`和`aa`这样不同奇偶性的回文串，将其补齐成类似`#a#b#a#`的形式，这样所有的回文串都是奇数。
然后，考虑某一个位置为中心的回文串，朴素的算法就是一步一步地扩大半径，直到不再回文，即这一部分代码
```python
while 0 <= i - k and i + k < n and ns[i - k] == ns[i + k]:
    k += 1
```
而马拉车算法在这一部分朴素的算法之外，进一步考虑到在我找到这个位置最长的回文串的时候，我在后面的寻找过程中可以利用这个信息。

我们维护一个最右边的回文串的边界`l, r`，如果`i`已经超出了这一部分，那么就只能直接调用后面的朴素算法；否则，我们可以利用之前的信息，考察在目前的`l, r`下对称的那个点`l+r-i`的最长回文串，将其设为我们朴素算法的起始半径来进行循环。

特别地，如果对称过来的半径太长，超出了`r`的部分事实上我们目前还没进行研究，所以最大值只能到`r-i-1`。

每次求解之后更新最右的`r`以及对应的`l`。

朴素算法，时间复杂度O(n²); Manacher，时间复杂度O(n)。（while循环每进一次r至少变大1）


代码：

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ns = f"#{'#'.join(s)}#"
        n = len(ns)
        # Manacher start
        d = [0]*n
        l, r = 0, -1
        for i in range(n):
            k = 1 if i > r else min(d[l + r - i], r - i + 1)
            while 0 <= i - k and i + k < n and ns[i - k] == ns[i + k]:
                k += 1
            d[i] = k
            k -= 1
            if i + k > r:
                l = i - k
                r = i + k
        # Manacher end
        cnt = max(d)
        idx = d.index(cnt)

        return ns[idx-cnt+1:idx+cnt].replace("#", "")

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241126181100.png)

### 12029: 水淹七军

bfs, dfs, http://cs101.openjudge.cn/practice/12029/

思路：思路上其实没有太大难点，和之前最大连通域一样。但有两个问题，第一个就是这个输入……我无话可说；第二个就是在于内存控制上，我一开始使用的`flooded`来标记，无论水多高都进行整体的dfs，但这个标记似乎回导致死循环的dfs…但它竟然通过了，只是MLE，我不理解啊。

另外……if加括号之后会有40%内存上的性能提升？？？？我不理解……这是什么奇怪的垃圾回收机制的影响吗？？？？

我的提交记录中从13开始往后就是对这里内存使用的探索……我到现在还是不太明白，而且截图有点多就不放上来了，不知道老师可不可以看到记录。

总体来说遇到的问题有：
1. 初始方法，使用`flooded`为什么会MLE？ —— 已解决，原因为会出现重复dfs的现象
2. 初始方法，使用`flooded`为什么可以MLE而不是RE？？ —— 未解决，明明重复dfs了却不会死循环？？
3. 使用`water_height`标记后，为什么if是否加括号会有超出误差的内存上的性能改变？—— 未解决，应该不太影响垃圾回收机制的吧？？
4. 添加注释会造成性能变化？ —— 已解决，大概是误差的一部分，同样代码重复提交的结果也不一样。

后面改成非递归的dfs+标记淹没高度的形式了

代码：

```python
import sys
directions = ((0, 1), (0, -1), (-1, 0), (1, 0))


def dfs_iterative(x, y, h, m, n, grid, water_height):
    stack = [(x, y)]
    water_height[x][y] = h

    while stack:
        cx, cy = stack.pop()

        for dx, dy in directions:
            nx = cx + dx
            ny = cy + dy
            if (0 <= nx < m and 0 <= ny < n and
                grid[nx][ny] < h and
                    water_height[nx][ny] < h):
                water_height[nx][ny] = h
                stack.append((nx, ny))


data = sys.stdin.read().split()
idx = 0
k = int(data[idx])
idx += 1
results = []

for _ in range(k):
    m, n = map(int, data[idx:idx + 2])
    idx += 2

    grid = []
    for i in range(m):
        grid.append(list(map(int, data[idx:idx + n])))
        idx += n

    water_height = [[0] * n for _ in range(m)]

    i, j = map(lambda x: int(x)-1, data[idx:idx + 2])
    idx += 2

    p = int(data[idx])
    idx += 1

    for _ in range(p):
        x, y = map(lambda x: int(x)-1, data[idx:idx + 2])
        idx += 2
        if grid[x][y] <= grid[i][j]:
            continue
        dfs_iterative(x, y, grid[x][y], m, n, grid, water_height)
    results.append("Yes" if water_height[i][j] > 0 else "No")

sys.stdout.write("\n".join(results) + "\n")

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241126205104.png)

### 02802: 小游戏

bfs, http://cs101.openjudge.cn/practice/02802/

思路：直接使用bfs就行，要注意的就是每次搜索要把一条线上的所有可达点都放到队列里，因为求的是`segment`最小而不是长度最小。然后考虑到可以出去，就补充一圈在外面，易得补一圈就够了。

最坑的在于题目里给的`x,y`和常见的不一样，数组取的时候要用`board[y][x]`来取，当然也可以输入的时候后先转置。

代码：

```python

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

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241127121744.png)

## 2. 学习总结和收获

这次作业……通过不难，但找到为什么错挺难的，尤其是这个水淹七军……嗯……
