# Assign #3: Oct Mock Exam暨选做题目满百

Updated Oct 11, 2024

2024 fall, Complied by 曹以楷 物理学院

**AC5**

## 1. 题目

### E28674:《黑神话：悟空》之加密

http://cs101.openjudge.cn/practice/28674/

思路：简单的ascii码应用

代码

```python
k = int(input()) % 26
s = input()
res = ""
for c in s:
    if c.islower():
        res += chr(ord("a")+(ord(c)-ord("a")-k) % 26)
    else:
        res += chr(ord("A")+(ord(c)-ord("A")-k) % 26)
print(res)

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241011092823.png)

### E28691: 字符串中的整数求和

http://cs101.openjudge.cn/practice/28691/

思路：一行直接写啊

代码

```python
print(sum(map(lambda x: int(x[:-1]), input().split())))

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241011093109.png)

### M28664: 验证身份证号

http://cs101.openjudge.cn/practice/28664/

思路：模拟，注意到最后一个对应的权重为1，总和为1 mod 11

代码

```python
weight = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 1)
for _ in range(int(input())):
    s = tuple(map(lambda x: 10 if x == "X" else int(x), input()))
    r = sum((s[i]*weight[i] for i in range(18)))
    print("YES" if r % 11 == 1 else "NO")

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241011094443.png)

### M28678: 角谷猜想

http://cs101.openjudge.cn/practice/28678/

思路：每日一练题，模拟

代码

```python
n = int(input())
while True:
    if n == 1:
        print("End")
        break
    if n % 2 == 0:
        print(f"{n}/2={n//2}")
        n //= 2
    else:
        print(f"{n}*3+1={n*3+1}")
        n = n*3+1

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241011094531.png)

### M28700: 罗马数字与整数的转换

http://cs101.openjudge.cn/practice/28700/

思路：先处理掉"IV"，然后直接求解

##### 代码

```python
roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def romanToArabic(r):
    r = r.replace("CM", "DCD").replace("CD", "CCCC").replace("XC", "LXL").replace(
        "XL", "XXXX").replace("IX", "VIV").replace("IV", "IIII")
    return (sum(roman[p] for p in r))


def arabicToRoman(a):
    r: str = a//1000 * "M"+a % 1000//500 * "D"+a % 500//100*"C" + \
        a % 100//50 * "L"+a % 50//10 * "X"+a % 10//5*"V"+a % 5*"I"
    r = r.replace("IIII", "IV").replace("VIV", "IX").replace("XXXX", "XL").replace(
        "LXL", "XC").replace("CCCC", "CD").replace("DCD", "CM")
    return r


s = input()
if s[0] in roman:
    print(romanToArabic(s))
else:
    print(arabicToRoman(int(s)))

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241011095942.png)

### *T25353: 排队 （选做）

http://cs101.openjudge.cn/practice/25353/

思路：贪心，找到能到达第一位的所有数，排序后放到最前面，递归。
事实上，看似是递归，但由于循环通常更快，还是用循环实现吧

代码

```python
# constants
MAXD = int(1e9+7)
# input
n, d = map(int, input().split())
# input lst
# use removed to mark, instead of truly remove the value
lst = []
removed = []
removed_total = 0
for _ in range(n):
    lst.append(int(input()))
    removed.append(0)

# if lst is empty, just finish
while removed_total < n:
    # find all numbers that can swap to the 1st place
    # just sort swapable later
    swapable = []

    # mark the minimum and maximum, instead of using min or max method
    preMin = MAXD
    preMax = -MAXD

    for i in range(len(lst)):
        # if it is removed before, just pass this, instead of truly remove the value
        if removed[i]:
            continue

        # update the minimum and maximum
        # obviously, lst[i]-d <= lst[i] <= lst[i]+d
        preMin = min(preMin, lst[i])
        preMax = max(preMax, lst[i])

        # check if it is swapable
        if preMax-d <= lst[i] <= preMin+d:
            # add to the swapable list, sort and print later
            swapable.append(lst[i])
            # mark it is removed
            removed[i] = 1
            removed_total += 1

    # print the sorted swapable
    print(*sorted(swapable), sep="\n")

```

![](https://raw.githubusercontent.com/Usercyk/images/main/20241011184244.png)

## 2. 学习总结和收获

事实证明，难题在间隔了一段时间后，不加注释思路容易乱
已经完成10月11日及以前的每日选做
