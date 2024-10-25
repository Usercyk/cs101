# Assignment #5: Greedy穷举Implementation

Updated Oct 25, 2024

2024 fall, Complied by <mark>曹以楷 物理学院</mark>

## 1. 题目

### 04148: 生理周期

brute force, http://cs101.openjudge.cn/practice/04148

思路：中国剩余定理，直接数学求解

代码：

```python
n = 1
while True:
    p, e, i, d = map(int, input().split())
    if p == e == i == d == -1:
        break
    # x == p+23x == e+28y == i+33z
    # (23*28)^(-1) = 2  mod 33
    # (28*33)^(-1) = 6  mod 23
    # (23*33)^(-1) = 19 mod 28
    x = (p*28*33*6+e*23*33*19+i*23*28*2) % 21252
    x = x if x else 21252
    s = x-d if x-d > 0 else x-d+21252
    print(f"Case {n}: the next triple peak occurs in {s} days.")
    n += 1

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241025174622.png)

### 18211: 军备竞赛

greedy, two pointers, http://cs101.openjudge.cn/practice/18211

思路：两边扫一遍

代码：

```python
p = int(input())
s = sorted(map(int, input().split()))
arm = 0
oarm = 0
i = 0
j = len(s)-1

while i <= j:
    if p >= s[i]:
        p -= s[i]
        arm += 1
        i += 1
        continue
    if arm > oarm and i < j:
        p += s[j]
        oarm += 1
        j -= 1
        continue
    break

print(arm-oarm)

```
![](https://raw.githubusercontent.com/Usercyk/images/main/20241025174825.png)

### 21554: 排队做实验

greedy, http://cs101.openjudge.cn/practice/21554

思路：~~小学奥数题~~ 贪心，越快的放越前面

代码：

```python
n = int(input())
t = sorted(((v, i) for i, v in enumerate(map(int, input().split()))))
print(*(p[1]+1 for p in t))
wait = sum((p[0]*(n-1-i) for i, p in enumerate(t)))
print("{:.2f}".format(wait/n))

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241025175712.png)

### 01008: Maya Calendar

implementation, http://cs101.openjudge.cn/practice/01008/

思路：直接计算

代码：

```python
haab = {'pop': 0, 'no': 1, 'zip': 2, 'zotz': 3, 'tzec': 4, 'xul': 5, 'yoxkin': 6, 'mol': 7, 'chen': 8, 'yax': 9,
        'zac': 10, 'ceh': 11, 'mac': 12, 'kankin': 13, 'muan': 14, 'pax': 15, 'koyab': 16, 'cumhu': 17, 'uayet': 18}
tzolkin = {0: 'imix', 1: 'ik', 2: 'akbal', 3: 'kan', 4: 'chicchan', 5: 'cimi', 6: 'manik', 7: 'lamat', 8: 'muluk', 9: 'ok',
           10: 'chuen', 11: 'eb', 12: 'ben', 13: 'ix', 14: 'mem', 15: 'cib', 16: 'caban', 17: 'eznab', 18: 'canac', 19: 'ahau'}

n=int(input())
print(n)
for _ in range(n):
    hd, hm, hy = input().split()
    hd = int(hd[:-1])
    hm = haab[hm]
    hy = int(hy)
    d = hy*365+hm*20+hd
    ty = d//260
    td = d % 260 % 13+1
    tm = tzolkin[d % 260 % 20]
    print(td, tm, ty)

```
![](https://raw.githubusercontent.com/Usercyk/images/main/20241025183938.png)

### 545C. Woodcutters

dp, greedy, 1500, https://codeforces.com/problemset/problem/545/C

思路：能倒就倒，扫一遍

代码：

```python
n = int(input())
trees = []
for _ in range(n):
    trees.append(tuple(map(int, input().split())))

r = 0
oc = -int(1e9+7)
for i in range(n):
    if trees[i][0]-trees[i][1] > oc:
        r += 1
        oc = trees[i][0]
        continue
    if i == n-1 or trees[i+1][0] > trees[i][0]+trees[i][1]:
        r += 1
        oc = trees[i][0]+trees[i][1]
        continue
    oc = trees[i][0]

print(r)

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241025185244.png)

### 01328: Radar Installation

greedy, http://cs101.openjudge.cn/practice/01328/

思路：和进程管理那题一样

代码：

```python
from decimal import Decimal


case = 1


def solve(d, islands):
    if d < 0:
        return -1
    r = []
    for x, y in islands:
        if y > d:
            return -1
        r.append((Decimal(x)+Decimal(d*d-y*y).sqrt(),
                 Decimal(x)-Decimal(d*d-y*y).sqrt()))

    r.sort()

    cnt = 1
    t = r[0][0]
    for p in r[1:]:
        if p[1] > t:
            t = p[0]
            cnt += 1

    return cnt


while True:
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        break
    islands = []
    for _ in range(n):
        islands.append(map(int, input().split()))
    input()
    res = solve(d, islands)
    print(f"Case {case}: {res}")
    case += 1

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241025193457.png)

## 2. 学习总结和收获

嗯……没来得及做每日选做，不过评测机的v1.0.0版本已经可用了

<https://github.com/Usercyk/OJPlus/releases>

下周写一下每日选做，然后重构一下代码+添加一些配置项（比如TLE的时间限制）
关于收获，我对python的引用和垃圾回收机制学习了一下，因为我开子进程去处理代码的时候，如果我不保持对该进程的引用，该进程会被立刻销毁。所以这里是一个比较典型的弱引用，可以防止不断开新的进程后造成的内存泄漏问题。
另外，windows自带的wsl虚拟机允许我打包一个linux版本，至于macOS，我正在找同学借电脑来打包，下个版本会有的。
