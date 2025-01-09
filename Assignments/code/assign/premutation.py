from itertools import permutations

n = int(input())

for p in permutations(range(1, n+1)):
    print(*p)
