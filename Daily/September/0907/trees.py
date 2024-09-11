l, m = map(int, input().split())
trees = [1]*(l+1)
for _ in range(m):
    u, v = map(int, input().split())
    for i in range(u, v+1):
        trees[i] = 0

print(sum(trees))
