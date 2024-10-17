from functools import reduce


t = int(input())
for _ in range(t):
    n = int(input())
    la = map(int, input().split(" "))
    lb = map(int, input().split(" "))
    sum_a, min_a = reduce(lambda x, y: (
        x[0]+y, x[1] if x[1] < y else y), la, (0, 1e10))
    sum_b, min_b = reduce(lambda x, y: (
        x[0]+y, x[1] if x[1] < y else y), lb, (0, 1e10))
    print(min(sum_a+n*min_b, n*min_a+sum_b))
