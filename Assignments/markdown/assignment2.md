# Assignment #2: 语法练习

Updated Sep 26, 2024

2024 fall, Complied by 曹以楷 物理学院

## 1. 题目

### 263A. Beautiful Matrix

https://codeforces.com/problemset/problem/263/A

思路：找1

##### 代码

```python
for i in range(5):
    s = input().split(" ")
    try:
        j = s.index("1")
        print(abs(i-2)+abs(j-2))
    except:
        continue

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20240926154314.png)

### 1328A. Divisibility Problem

https://codeforces.com/problemset/problem/1328/A

思路：判断能否整除

##### 代码

```python
n = int(input())

for _ in range(n):
    a, b = map(int, input().split(" "))
    print(b-a % b if a % b else 0)

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20240926154427.png)

### 427A. Police Recruits

https://codeforces.com/problemset/problem/427/A

思路：用`reduce`遍历一遍，模拟抓捕即可

##### 代码

```python
from functools import reduce

criminal = 0


def func(cur, y):
    global criminal
    left = cur+int(y)
    if left < 0:
        criminal += 1
        return 0
    else:
        return left


n = input()
reduce(func, input().split(" "), 0)

print(criminal)

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20240926154619.png)

### 02808: 校门外的树

http://cs101.openjudge.cn/practice/02808/

思路：线段树

##### 代码

```python
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sum = 0
        self.left = None
        self.right = None
        self.mark = False


class Tree:
    def __init__(self, maxCord):
        self.root = Tree.build([1]*(maxCord+1), 0, maxCord)

    @staticmethod
    def build(nums, start, end):
        if start > end:
            return None

        root = Node(start, end)

        if start == end:
            root.sum = nums[start]
            return root

        mid = (start+end)//2
        root.left = Tree.build(nums, start, mid)
        root.right = Tree.build(nums, mid+1, end)
        root.sum = root.left.sum+root.right.sum

        return root

    @staticmethod
    def update(root, start, end):
        if start > root.end or end < root.start:
            return
        if root.start >= start and end >= root.end:
            root.mark = True
            root.sum = 0
            return

        root.left.mark |= root.mark
        root.right.mark |= root.mark
        if root.left.mark:
            root.left.sum = 0
        if root.right.mark:
            root.right.sum = 0
        Tree.update(root.left, start, end)
        Tree.update(root.right, start, end)
        root.sum = root.left.sum+root.right.sum

    @staticmethod
    def query(root, start, end):
        if start > root.end or end < root.start:
            return 0
        if root.start >= start and end >= root.end:
            return root.sum

        root.left.mark |= root.mark
        root.right.mark |= root.mark
        if root.left.mark:
            root.left.sum = 0
        if root.right.mark:
            root.right.sum = 0

        return Tree.query(root.left, start, end)+Tree.query(root.right, start, end)


l, m = map(int, input().split())
tr = Tree(l)
for _ in range(m):
    u, v = map(int, input().split())
    Tree.update(tr.root, u, v)

print(Tree.query(tr.root, 0, l))

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20240926154851.png)

### sy60: 水仙花数II

https://sunnywhy.com/sfbj/3/1/60

思路：数学上可得只有153, 370, 371, 407是三位水仙花数

##### 代码

```python
nar = (153, 370, 371, 407)
a, b = map(int, input().split())
res = []
for n in nar:
    if a <= n <= b:
        res.append(n)
if res:
    print(*res)
else:
    print("NO")

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20240926155022.png)

### 01922: Ride to School

http://cs101.openjudge.cn/practice/01922/

思路：一定和在之后出发的第一个到的人同时到

##### 代码

```python
from math import ceil, inf


while True:
    N = int(input())
    if N == 0:
        break
    ans = +inf
    for _ in range(N):
        v, t = map(int, input().split())
        if t >= 0:
            reachTime = t+16200/v
            if reachTime < ans:
                ans = reachTime
    print(ceil(ans))

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20240926160227.png)

## 2. 学习总结和收获

完成了9月26日前所有每日选做，学会了datetime库





