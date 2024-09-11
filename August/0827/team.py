from functools import reduce

n = int(input())
count = 0
for _ in range(n):
    sol = reduce(lambda x, y: x+int(y), input().split(), 0)
    if (sol >= 2):
        count += 1

print(count)
