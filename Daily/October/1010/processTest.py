for _ in range(int(input())):
    process = []
    n = int(input())
    for _ in range(n):
        process.append(tuple(map(int, input().split())))
    process.sort(key=lambda x: x[1])
    cnt = 0
    t = -1
    for p in process:
        if p[0] > t:
            cnt += 1
            t = p[1]
    print(cnt)
