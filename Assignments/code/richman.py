print(__import__("functools").reduce(lambda x, y: (y, y, y) if x[0] is None else (max(
    x[0]+y, y), max(x[0], x[1]+y, y), max(x[2], max(x[0], x[1]+y, y))), map(int, input().split(',')), (None, None, None))[2])
