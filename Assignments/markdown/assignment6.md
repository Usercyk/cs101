# Assignment #6: Recursion and DP

Updated Nov 1, 2024

2024 fall, Complied by 曹以楷 物理学院


## 1. 题目

### sy119: 汉诺塔

recursion, https://sunnywhy.com/sfbj/4/3/119

思路：三柱，初态简单，直接递归

代码：

```python
names = ["A", "B", "C"]


def hanoi(n, p, q):
    if n == 1:
        print(f"{names[p]}->{names[q]}")
        return
    hanoi(n-1, p, 3-p-q)
    print(f"{names[p]}->{names[q]}")
    hanoi(n-1, 3-p-q, q)


n = int(input())
print(2**n-1)
hanoi(n, 0, 2)

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241031084647.png)

### sy132: 全排列I

recursion, https://sunnywhy.com/sfbj/4/3/132

思路：额……这题……算了直接上代码吧

代码：

```python
from itertools import permutations

n = int(input())

for p in permutations(range(1, n+1)):
    print(*p)

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241031085106.png)

### 02945: 拦截导弹

dp, http://cs101.openjudge.cn/2024fallroutine/02945

思路：直接求最长递减子序列的长度，写状态转移方程

代码：

```python
# dp[H][i] 表示在H限制下，从i到n-1中可以拦下最多多少个
# if H<h[i]: dp[H][i]=dp[H][i+1]
# if H>=h[i]: dp[H][i]=max(dp[h[i]][i+1]+1, dp[H][i+1])
# 初态：dp[H][n-1]=1 if H>h[n-1] else 0
# 问题：dp[MAXH][0]
def dp(H, i):
    global h, n
    if i == n-1:
        return 1 if H >= h[n-1] else 0
    if H < h[i]:
        return dp(H, i+1)
    return max(dp(h[i], i+1)+1, dp(H, i+1))


n = int(input())
*h, = map(int, input().split())
print(dp(max(h), 0))

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241031090545.png)

### 23421: 小偷背包

dp, http://cs101.openjudge.cn/practice/23421

思路：0-1背包模板？

代码：

```python
# dp[M][i]表示在背包空间还剩M时从i到n-1中可以拿到的最大价值
# M<m[i]: dp[M][i]=dp[M][i+1]
# M>=m[i]: dp[M][i]=max(dp[M-m[i]][i+1]+v[i],dp[M][i+1])
# 初态dp[M][n-1]=v[n-1] if M>=m[n-1] else 0
# 待求dp[B][0]
def dp(M, i):
    global m, v, n
    if i == n-1:
        return v[n-1] if M >= m[n-1] else 0
    if M < m[i]:
        return dp(M, i+1)
    return max(dp(M-m[i], i+1)+v[i], dp(M, i+1))


n, B = map(int, input().split())
*v, = map(int, input().split())
*m, = map(int, input().split())

print(dp(B, 0))

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241031091431.png)

### 02754: 八皇后

dfs and similar, http://cs101.openjudge.cn/practice/02754

思路：其实只要想到每次不是判断而是直接使用数组记录斜线和列是否能放置就应该不会超时了，这里用的dfs

代码：

```python
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

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241031093105.png)

### 189A. Cut Ribbon

brute force, dp 1300 https://codeforces.com/problemset/problem/189/A

思路：一个必须装满的完全背包模板题

代码：

```python
# dp[i][j]表示考虑前i件物品，长度为j的丝带可以分多少段
# dp[i-1][j]=max(dp[i-1][j],dp[i][j-w[i]]+1)
# 初态dp[i][0]=0, dp[0][j]=0
# 待求dp[3][n]
# 要求必须装满背包

dp = [-1]*4100
dp[0] = 0
n, *w = map(int, input().split())

for i in range(3):
    for j in range(w[i], n+1):
        if dp[j-w[i]] != -1:
            dp[j] = max(dp[j], dp[j-w[i]]+1)

print(dp[n])

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241101111719.png)

## 2. 学习总结和收获

正在完成每日选做…正在补正在补





