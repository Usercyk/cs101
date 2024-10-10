def pell():
    x, y = 1, 2
    while True:
        yield x
        x, y = y % 32767, (x+2*y) % 32767


for _ in range(int(input())):
    n = int(input())
    gen = pell()
    for _ in range(n):
        a = next(gen)
    print(a)
