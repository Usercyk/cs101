weight = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 1)
for _ in range(int(input())):
    s = tuple(map(lambda x: 10 if x == "X" else int(x), input()))
    r = sum((s[i]*weight[i] for i in range(18)))
    print("YES" if r % 11 == 1 else "NO")
