from functools import reduce

n = int(input())
print(reduce(lambda x, y: x+int(y), input().split(" "), 0)/n)
