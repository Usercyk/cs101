# Assignment #7: Nov Mock Exam立冬

Updated GMT+8 Nov 7, 2024

2024 fall, Complied by 曹以楷 物理学院

AC6

## 1. 题目

### E07618: 病人排队

sorttings, http://cs101.openjudge.cn/practice/07618/

思路：其实我本来想着直接sort几遍就可以了，但是我不太清楚3.8的排序是否有稳定性，于是干脆写`cmp_to_key`了。
> 当然其实3.8的排序是有稳定性的
> 这里的稳定性具体就是指同一个年龄的是否能保持输入顺序不变

代码：

```python
from functools import cmp_to_key


def cmp(x, y):
    if x[0] >= 60 and y[0] >= 60:
        return x[0]-y[0]
    if x[0] >= 60 and y[0] < 60:
        return 1
    if x[0] < 60 and y[0] >= 60:
        return -1
    return 0


n = int(input())
p = []
for _ in range(n):
    i, a = input().split()
    a = int(a)
    p.append((a, i))

p.sort(key=cmp_to_key(cmp), reverse=True)
for x in p:
    print(x[1])

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241107185721.png)

### E23555: 节省存储的矩阵乘法

implementation, matrices, http://cs101.openjudge.cn/practice/23555/

思路：用字典来存储矩阵即可，这主要是利用`dict.get()`函数可以设置默认值。当然我并没有仔细考虑使用字典是否会有效率问题，毕竟矩阵乘法的效率大头肯定是后面的三个`for`循环。

代码：

```python
n, m1, m2 = map(int, input().split())
A = {}
B = {}
C = {}
for _ in range(m1):
    x, y, v = map(int, input().split())
    A[(x, y)] = v
for _ in range(m2):
    x, y, v = map(int, input().split())
    B[(x, y)] = v

# AijBjk=Cik
for i in range(n):
    for k in range(n):
        s = sum(A.get((i, j), 0)*B.get((j, k), 0) for j in range(n))
        if s != 0:
            C[(i, k)] = s

ans = sorted(((k[0], k[1], v) for k, v in C.items()))
for x in ans:
    print(*x)

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241107185955.png)

### M18182: 打怪兽

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/

思路：取同一时间最大的m个技能就行了

代码：

```python
for _ in range(int(input())):
    n, m, b = map(int, input().split())
    s = {}
    ts = []
    for _ in range(n):
        t, x = map(int, input().split())
        if t in s:
            s[t].append(x)
        else:
            s[t] = [x]
            ts.append(t)
    ts.sort()
    for t in ts:
        d = sum(sorted(s[t], reverse=True)[:m])
        b -= d
        if b <= 0:
            print(t)
            break
    if b > 0:
        print("alive")

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241107190135.png)

### M28780: 零钱兑换3

dp, http://cs101.openjudge.cn/practice/28780/

思路：要求装满的完全背包，但卡常数！代码中特判`n==1`的部分如果不加入就会超时，事实上这里主要是因为默认值设置了`-1`，这个值并不好，导致多了一些无用的`if-else`，应该设一个最大值（比如`1e9+7`），再在最后进行处理。
> AC截图里注释的思路和代码里的不太一样，主要是把负硬币数量最大值换成了正硬币数量最小值

代码：

```python
def solve():
    n, W = map(int, input().split())
    *w, = map(int, input().split())
    if n == 1:
        if W % w[0] != 0:
            return -1
        else:
            return W//w[0]
    dp = [-1]*(W+1)
    dp[0] = 0
    for i in range(n):
        for j in range(w[i], W+1):
            if dp[j-w[i]] != -1:
                if dp[j] == -1:
                    dp[j] = dp[j-w[i]]+1
                else:
                    dp[j] = min(dp[j], dp[j-w[i]]+1)
    return dp[W]


print(solve())

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241107190242.png)

### T12757: 阿尔法星人翻译官

implementation, http://cs101.openjudge.cn/practice/12757

思路：分段处理即可

代码：

```python
nums = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
    "hundred": 100,
    "thousand": 1000,
    "million": 1000000
}


def transform_small(q):
    r = 0
    for v in q:
        if v == "hundred":
            r *= 100
        else:
            r += nums[v]
    return r


def transform(p):
    res = 0
    q = []
    for v in p:
        if v == "million" or v == "thousand":
            tem = transform_small(q)
            res += tem*nums[v]
            q = []
        else:
            q.append(v)
    res += transform_small(q)
    return res


s = input().split()
if s[0] == "negative":
    print(-transform(s[1:]))
else:
    print(transform(s))

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241107190559.png)

### T16528: 充实的寒假生活

greedy/dp, cs10117 Final Exam, http://cs101.openjudge.cn/practice/16528/

思路：本来用`dp`来做，结果超时了，再仔细一看，贪心就可以了。但是脑子有点转不过来了，最后只能写排除所有重复活动的代码，一时间翻不过来了。

代码：

```python
def solve(act):
    if n == 0 or not act:
        return 0
    act.sort()
    tem = 0
    cnt = 0
    for i in range(1, n):
        if act[tem][1] >= act[i][0]:
            cnt += 1
            if act[tem][1] > act[i][1]:
                tem = i
        else:
            tem = i
    return n-cnt


n = int(input())
activities = []
for _ in range(n):
    activities.append(tuple(map(int, input().split())))
print(solve(activities))

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241107190653.png)

## 2. 学习总结和收获

其实个人感觉阿尔法星人那题应该是`Easy`的，因为这题是在问英文数字。然后如果写过中文与数字转换就会发现，中文的处理繁琐很多。当然主要思想肯定是首先分段（英文三个一段，中文四个一段），每一段内部处理都是一样的，然后再拼起来就行了。中文数字比英文数字难点在于`零`，比如`1010`和`一千零一十`。但阿尔法星人给样例里面其实没有出现过`zero`，或者说，出现`zero`的地方只有`0`这一个数据。

哦对，阿尔法星人这题中`nums`这个字典可以不用手打这么多的，可以使用正则表达式匹配所有的单词，然后利用替换对这些单词统一加上引号；然后匹配逗号前面，利用查找将光标自动移过去，输入数字即可。这可比手动一个一个打快多了。

两个`dp`题刚开始都超时了，搞得我怀疑我模板都背错了……结果一个卡常数，一个应该贪心……

其它题都还挺简单的。
