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
