n = int(input())
trees = []
for _ in range(n):
    trees.append(tuple(map(int, input().split())))

r = 0
oc = -int(1e9+7)
for i in range(n):
    if trees[i][0]-trees[i][1] > oc:
        r += 1
        oc = trees[i][0]
        continue
    if i == n-1 or trees[i+1][0] > trees[i][0]+trees[i][1]:
        r += 1
        oc = trees[i][0]+trees[i][1]
        continue
    oc = trees[i][0]

print(r)
