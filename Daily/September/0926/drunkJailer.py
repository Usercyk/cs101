for _ in range(int(input())):
    n = int(input())
    prison = [-1 for _ in range(n)]
    for i in range(1, n+1):
        for k in range(1, n//i+1):
            prison[i*k-1] *= -1
    print(sum((i for i in prison if i > 0)))
