# Assignment #8: 田忌赛马来了

Updated GMT+8 Nov 14, 2024

2024 fall, Complied by 曹以楷 物理学院

## 1. 题目

### 12558: 岛屿周⻓

matices, http://cs101.openjudge.cn/practice/12558/

思路：外面补一圈，懒得判断了，用了5分钟

代码：

```python
n, m = map(int, input().split())
islands = [[0]*(m+2)]

for i in range(n):
    s = list(map(int, input().split()))
    islands.append([0, *s, 0])

islands.append([0]*(m+2))
p = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if islands[i][j] != 0:
            p += 4-islands[i][j-1]-islands[i][j+1] - \
                islands[i-1][j]-islands[i+1][j]

print(p)

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241114081614.png)

### LeetCode54.螺旋矩阵

matrice, https://leetcode.cn/problems/spiral-matrix/

与OJ这个题目一样的 18106: 螺旋矩阵，http://cs101.openjudge.cn/practice/18106

思路：不是很想一圈一圈解决，直接定义了方向来步进，用时20分钟

代码：

```python
class Solution:
    class Position:
        def __init__(self, x, y) -> None:
            self.x = x
            self.y = y

        def __add__(self, other: "Solution.Position"):
            return Solution.Position(self.x+other.x, self.y+other.y)

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        if n == 0:
            return []
        m = len(matrix[0])

        direction = [self.Position(0, 1), self.Position(
            1, 0), self.Position(0, -1), self.Position(-1, 0)]
        result = []
        border = [0, m-1, n-1, 0]
        pos = self.Position(0, 0)
        d = 0
        for _ in range(n*m):
            result.append(matrix[pos.x][pos.y])
            np = pos+direction[d]
            if not (border[0] <= np.x <= border[2] and border[1] >= np.y >= border[3]):
                if d == 1 or d == 2:
                    border[d] -= 1
                else:
                    border[d] += 1
                d = (d+1) % 4
                np = pos+direction[d]
            pos = np
        return result

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241114084942.png)

### 04133:垃圾炸弹

matrices, http://cs101.openjudge.cn/practice/04133/

思路：暴力，用时10分钟

代码：

```python
from itertools import product


def solve():
    d = int(input())
    r = []
    for _ in range(int(input())):
        x, y, rb = map(int, input().split())
        r.append((x, y, rb))

    ans = -1
    cnt = 0
    for i, j in product(range(1025), range(1025)):
        tem = 0
        for p in r:
            if i-d <= p[0] <= i+d and j-d <= p[1] <= j+d:
                tem += p[2]
        if tem > ans:
            ans = tem
            cnt = 1
        elif tem == ans:
            cnt += 1

    print(cnt, ans)


solve()

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241114085456.png)

### LeetCode376.摆动序列

greedy, dp, https://leetcode.cn/problems/wiggle-subsequence/

与OJ这个题目一样的，26976:摆动序列, http://cs101.openjudge.cn/routine/26976/

思路：dp，时间O(n)，空间O(1)，用时20分钟

代码：

```python
# dp[i][1]表示i前摆动序列上升结尾中最长的
# dp[i][0]表示i后摆动序列下降结尾中最长的
# nums[i-1]<num[i]: dp[i][0]=dp[i-1][0];dp[i][1]=max(dp[i-1][1],dp[i-1][0]+1)
# nums[i-1]>num[i]: dp[i][1]=dp[i-1][1];dp[i][0]=max(dp[i-1][0],dp[i-1][1]+1)
# dp[0][0]=dp[0][1]=1
# ans=max(dp[n-1][0], dp[n-1][1])


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        dp = [1, 1]
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                continue
            s = nums[i] > nums[i-1]
            dp[1-s] = max(dp[1-s], dp[s]+1)
        return max(dp)

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241114091422.png)

### CF455A: Boredom

dp, 1500, https://codeforces.com/contest/455/problem/A

思路：对$a_k$进行dp而非对k

代码：

```python
MAXN = int(1e5+7)
dp = [0]*MAXN
input()
for p in map(int, input().split()):
    dp[p] += p
for i in range(2, MAXN):
    dp[i] = max(dp[i-1], dp[i]+dp[i-2])
print(dp[i])

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241114092351.png)

### 02287: Tian Ji -- The Horse Racing

greedy, dfs http://cs101.openjudge.cn/practice/02287

思路：和田忌想法一样就行，策略不变，直接贪心

代码：

```python
while True:
    n = int(input())
    if n == 0:
        break
    tian = sorted(map(int, input().split()))
    king = sorted(map(int, input().split()))
    res = 0
    lt, rt = 0, n-1
    lk, rk = 0, n-1
    while n:
        if tian[rt] > king[rk]:
            res += 200
            rt -= 1
            rk -= 1
        elif tian[rt] < king[rk]:
            res -= 200
            lt += 1
            rk -= 1
        else:
            if tian[lt] > king[lk]:
                res += 200
                lt += 1
                lk += 1
            else:
                if tian[lt] < king[rk]:
                    res -= 200
                lt += 1
                rk -= 1
        n -= 1
    print(res)

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241114093636.png)

## 2. 学习总结和收获

期中考这段时间是真忙……看了看桶/堆/栈/树。
