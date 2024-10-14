input()
a = map(int, input().split())
b = map(int, input().split())
x = 0
y = 0
while True:
    if x == 0:
        try:
            x = next(a)
        except StopIteration:
            if y:
                print(y, end="")
            print("", *b)
            break
    if y == 0:
        try:
            y = next(b)
        except StopIteration:
            if x:
                print(x, end="")
            print("", *a)
            break
    if x < y:
        print(x, end=" ")
        x = 0
    else:
        print(y, end=" ")
        y = 0
