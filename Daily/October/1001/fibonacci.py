def fibonacci():
    x, y = 1, 1
    while True:
        yield x
        x, y = y, x+y


for _ in range(int(input())):
    n = int(input())
    gen = fibonacci()
    for _ in range(n):
        a = next(gen)
    print(a)
