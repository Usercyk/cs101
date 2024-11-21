from math import isqrt


def isSquare(x):
    x = int(x)
    return x != 0 and isqrt(x)**2 == x


def dfs(x):
    global n, flag, s
    if x >= n-1:
        flag = True
    v = ""
    for j in range(x+1, n):
        v = v+s[j]
        if isSquare(v):
            dfs(j)


s = input()
n = len(s)
flag = False
dfs(-1)
print("Yes" if flag else "No")
