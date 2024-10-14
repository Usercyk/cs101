from functools import reduce


def gap(x, y):
    if x[1] == -1:
        return x[0], y
    x[0].append(y-x[-1])
    return x[0], y


n, m = map(int, input().split())
p = reduce(gap, sorted(map(int, input().split())), ([], -1))[0]
print(sum(sorted(p,reverse=True)[m-1:]))
