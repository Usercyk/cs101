from functools import reduce


def myFormat(s):
    return str(s).replace("\'", "").replace(" ", "")


def encode(x, y):
    if x is None:
        return (y, 1)
    if y == x[0]:
        return (x[0], x[1]+1)
    print(myFormat(x), end="")
    return (y, 1)


s = input().lower()
print(myFormat(reduce(encode, s, None)))
