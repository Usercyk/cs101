from functools import reduce

criminal = 0


def func(cur, y):
    global criminal
    left = cur+int(y)
    if left < 0:
        criminal += 1
        return 0
    else:
        return left


n = input()
reduce(func, input().split(" "), 0)

print(criminal)
