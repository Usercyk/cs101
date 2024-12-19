from itertools import product


def get_layer(x, y, n):
    return min(x, y, n-x-1, n-y-1)


res = [0]*100
n = int(input())
onion = [list(map(int, input().split())) for _ in range(n)]
for i, j in product(range(n), range(n)):
    res[get_layer(i, j, n)] += onion[i][j]

print(max(res))
