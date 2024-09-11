n = int(input())

for _ in range(n):
    res = []
    for i, v in enumerate(input()[::-1]):
        if v != "0":
            res.append(int(v)*pow(10, i))

    print(len(res))
    print(*res)
