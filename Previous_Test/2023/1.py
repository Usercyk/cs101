from math import log2


for _ in range(int(input())):
    n = int(input())
    r = int(log2(n))
    print(n*(n+1)//2-2*(2**(r+1)-1))
