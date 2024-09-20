# Assignment #1: 自主学习

Updated 0110 GMT+8 Sep 20, 2024

2024 fall, Complied by 曹以楷 物理学院

## 1. 题目

### 02733: 判断闰年

http://cs101.openjudge.cn/practice/02733/

思路：判断条件后输出即可，或调用calendar库

##### 代码

```python
y = int(input())
print("Y" if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0) else "N")

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20240920152334.png)

### 02750: 鸡兔同笼

http://cs101.openjudge.cn/practice/02750/

思路：直接输出全是鸡或全是兔的情况，注意边界情况即可

##### 代码

```python
feet = int(input())

if feet % 2 == 1:
    print(0, 0)
else:
    min_head = feet//4+(feet % 4) // 2
    max_head = feet//2
    print(min_head, max_head)

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20240920152515.png)

### 50A. Domino piling

greedy, math, 800, http://codeforces.com/problemset/problem/50/A

思路：黑白相间染色

##### 代码

```python
a, b = (int(i) for i in input().split(" "))
print(a*b//2)

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20240920152634.png)

### 1A. Theatre Square

math, 1000, https://codeforces.com/problemset/problem/1/A

思路：分别覆盖两条边

##### 代码

```python
from math import ceil
n, m, a = map(int, input().split())
print(ceil(n/a)*ceil(m/a))

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20240920152935.png)

### 112A. Petya and Strings

implementation, strings, 1000, http://codeforces.com/problemset/problem/112/A

思路：统一后大小写后比大小

##### 代码

```python
n = input().capitalize()
m = input().capitalize()

print(-1 if n < m else 0 if n == m else 1)

```
![](https://raw.githubusercontent.com/Usercyk/images/main/20240920153055.png)

### 231A. Team

bruteforce, greedy, 800, http://codeforces.com/problemset/problem/231/A

思路：求和判断是否大于2即可，这里没有使用`sum`，改用`reduce`。

##### 代码

```python
from functools import reduce

n = int(input())
count = 0
for _ in range(n):
    sol = reduce(lambda x, y: x+int(y), input().split(), 0)
    if (sol >= 2):
        count += 1

print(count)

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20240920153404.png)

## 2. 学习总结和收获

已完成9月20日及之前的所有每日选做，正在撰写一篇用于新手搭建`python`或`c++`环境的教程。

[新手搭建环境教程](https://github.com/Usercyk/cs101/blob/master/Notes/Preparation.md)
