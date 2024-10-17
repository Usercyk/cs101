# Assignment #4: T-primes + 贪心

Updated Oct 17, 2024

2024 fall, Complied by <mark>曹以楷 物理学院</mark>

## 1. 题目

### 34B. Sale

greedy, sorting, 900, https://codeforces.com/problemset/problem/34/B

思路：排序，用时20分钟


代码

```python
n, m = map(int, input().split())
b = sorted(map(lambda x: -int(x), input().split()), reverse=True)
print(sum((i for i in b[:m] if i > 0)))

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241017163646.png)

### 160A. Twins

greedy, sortings, 900, https://codeforces.com/problemset/problem/160/A

思路：取最大，追踪前缀和与后缀和，用时15分钟

代码

```python
input()
coins = sorted(map(int, input().split()),reverse=True)
curr = 0
left = sum(coins)
for i, c in enumerate(coins):
    curr += c
    left -= c
    if curr > left:
        print(i+1)
        break

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241017163931.png)

### 1879B. Chips on the Board

constructive algorithms, greedy, 900, https://codeforces.com/problemset/problem/1879/B

思路：行和列必有一个全部都涉及到了，那另一边直接填最小值就行，用时20分钟

代码

```python
from functools import reduce


t = int(input())
for _ in range(t):
    n = int(input())
    la = map(int, input().split(" "))
    lb = map(int, input().split(" "))
    sum_a, min_a = reduce(lambda x, y: (
        x[0]+y, x[1] if x[1] < y else y), la, (0, 1e10))
    sum_b, min_b = reduce(lambda x, y: (
        x[0]+y, x[1] if x[1] < y else y), lb, (0, 1e10))
    print(min(sum_a+n*min_b, n*min_a+sum_b))

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241017164327.png)

### 158B. Taxi

*special problem, greedy, implementation, 1100, https://codeforces.com/problemset/problem/158/B

思路：和box packing一样，用时15分钟

代码

```python
input()
kids = {1: 0, 2: 0, 3: 0, 4: 0}
for p in input().split():
    kids[int(p)] += 1
res = kids[4]+kids[3]+(kids[2]+1)//2 + \
    (max(kids[1]-(kids[3]+(kids[2]+1)//2*4-kids[2]*2), 0)+3)//4
print(res)

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241017164447.png)

### *230B. T-primes（选做）

binary search, implementation, math, number theory, 1300, http://codeforces.com/problemset/problem/230/B

思路：动态启动欧拉筛+缓存

代码

```python
from math import sqrt


cache = {}


def eulerSieve(maxN):
    is_prime = [True] * (maxN + 1)
    is_prime[0] = is_prime[1] = False
    primes = set()
    for i in range(2, maxN + 1):
        if is_prime[i]:
            primes.add(i)
            for j in range(i * i, maxN + 1, i):
                is_prime[j] = False
    return primes


def isTPrime(n):
    if n in cache:
        return cache[n]
    if n == 1 or n == 0:
        cache[n] = False
        return False
    p = int(sqrt(n))
    if p*p != n:
        cache[n] = False
        return False
    for i in range(2, int(sqrt(p))+1):
        if p % i == 0:
            cache[n] = False
            return False
    cache[n] = True
    return True


def isSieveTPrime(n, primes):
    if n in cache:
        return cache[n]
    if n == 1 or n == 0:
        cache[n] = False
        return False
    p = int(sqrt(n))
    if p*p != n:
        cache[n] = False
        return False
    if p not in primes:
        cache[n] = False
        return False
    cache[n] = True
    return True


n = int(input())
if n < 10000:
    for i in map(int, input().split()):
        print("YES" if isTPrime(i) else "NO")
else:
    primes = eulerSieve(1000000)
    for i in map(int, input().split()):
        print("YES" if isSieveTPrime(i, primes) else "NO")

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241017164628.png)

### *12559: 最大最小整数 （选做）

greedy, strings, sortings, http://cs101.openjudge.cn/practice/12559

思路：补齐两倍长度比较
>PS: 我自认我这个四行压缩可读性还是相对比较高的

代码

```python
_, s, = input(), input().split()
max_len = max(len(p) for p in s)
s.sort(key=lambda x: x*(__import__("math").ceil(2*max_len/len(x))), reverse=True)
print("".join(s), "".join(reversed(s)))

```
![](https://raw.githubusercontent.com/Usercyk/images/main/20241017165820.png)

## 2. 学习总结和收获

已经完成10月18日及之前的每日选做

&emsp;
&emsp;

说起来，`assignment1`的时候，我记得要写笔记来着🤔。结果现在发现所有人的环境基本都已经搭建好了…
后来我受到了群里`testing code`文件的启发，想着干脆把这个再修改一下加点东西上去。
技术栈（虽然这里似乎还算不上栈）最后选择了`PySide6`，主要是`qfluentwidget`的设计实在是太符合windows那种感觉，用其他的基本上都需要自己想设计…（写tailwindcss/sass也挺累的）这个只写了三天就写完设置界面哩。照着设计“抄”就很舒服。（GPLv3许可证）
哦，不用C++的Qt来写是因为`qfluentwidget`的C++部分没有开源，有bug的话改不了。
现在已经开始写主要功能的代码了，`testing code`文件似乎没有考虑到除了WA之外的其它错误，以及如果传入一个死循环可能会有一定的问题…所以感觉还需要想想怎么设计和优化。
这似乎就是自己写一个评测机，额…刚好是本地不联网的小应用，应该不会有和OJ作用重复的地方吧……？
算了…∩(︶︿︶)∩就当丰富一下repo吧，贴一下网站，截图和预计的features在这里

<https://github.com/Usercyk/OJPlus>

![](https://raw.githubusercontent.com/Usercyk/images/main/20241017170752.png)

### Features

1. Help check your program. When the online judge machine did not give you why your code could not work, you can use `OJ Plus` to help you check your program.
2. If the question you are doing right now already has a solution, `OJ Plus` can aotomatically show you the standard (mostly better for beginner) solution and help you learn it.
3. For beginners, `OJ Plus` has various tutorials, including how to build an environment, the basic programming skills or high-level algorithm.
4. Internationalization supported.
