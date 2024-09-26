from math import log


for _ in range(int(input())):
    n = int(input())
    s = int(log(2, n))
    print(n*(n+1)//2-(2**(s+2)-2))
