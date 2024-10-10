from math import inf


while True:
    n = int(input())
    if n == 0:
        break
    hotels = []
    for _ in range(n):
        hotels.append(tuple(map(int, input().split())))
    hotels.sort(key=lambda x: (x[0], -x[1]))
    minPrice = inf
    res = 0
    for i in range(n):
        if i < n-1 and hotels[i][0] == hotels[i+1][0]:
            continue
        if minPrice > hotels[i][1]:
            res += 1
            minPrice = hotels[i][1]
    print(res)
