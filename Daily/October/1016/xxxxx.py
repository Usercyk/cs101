from functools import reduce


def solve():
    n, x = map(int, input().split())
    *a, = map(lambda p: int(p) % x, input().split())
    s = reduce(lambda g, h: (g+h) % x, a)
    if s != 0:
        print(n)
        return
    l, r = n, n
    for i in range(n):
        if a[i] != 0:
            l = i+1
            break
    for j in range(n):
        if a[n-1-j] != 0:
            r = j+1
            break
    p = n-min(l, r)
    print(p if p > 0 else -1)


for _ in range(int(input())):
    solve()
