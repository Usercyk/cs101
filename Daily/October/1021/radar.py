from decimal import Decimal


case = 1


def solve(d, islands):
    if d < 0:
        return -1
    r = []
    for x, y in islands:
        if y > d:
            return -1
        r.append((Decimal(x)+Decimal(d*d-y*y).sqrt(),
                 Decimal(x)-Decimal(d*d-y*y).sqrt()))

    r.sort()

    cnt = 1
    t = r[0][0]
    for p in r[1:]:
        if p[1] > t:
            t = p[0]
            cnt += 1

    return cnt


while True:
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        break
    islands = []
    for _ in range(n):
        islands.append(map(int, input().split()))
    input()
    res = solve(d, islands)
    print(f"Case {case}: {res}")
    case += 1
