def solve(n, m):
    pos = 0
    for i in range(2, n + 1):
        pos = (pos + m) % i
    return pos + 1


while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    print(solve(n, m))
