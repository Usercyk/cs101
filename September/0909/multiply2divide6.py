for _ in range(int(input())):
    n = int(input())
    p2 = 0
    p3 = 0
    while (n % 2 == 0):
        p2 += 1
        n //= 2
    while (n % 3 == 0):
        p3 += 1
        n //= 3

    if n != 1 or p3 < p2:
        print(-1)
    else:
        print(2*p3-p2)
