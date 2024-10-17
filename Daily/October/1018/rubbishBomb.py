from itertools import product


def solve():
    d = int(input())
    r = []
    for _ in range(int(input())):
        x, y, rb = map(int, input().split())
        r.append((x, y, rb))

    ans = -1
    cnt = 0
    for i, j in product(range(1025), range(1025)):
        tem = 0
        for p in r:
            if i-d <= p[0] <= i+d and j-d <= p[1] <= j+d:
                tem += p[2]
        if tem > ans:
            ans = tem
            cnt = 1
        elif tem == ans:
            cnt += 1

    print(cnt, ans)


solve()
