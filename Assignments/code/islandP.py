n, m = map(int, input().split())
islands = [[0]*(m+2)]

for i in range(n):
    s = list(map(int, input().split()))
    islands.append([0, *s, 0])

islands.append([0]*(m+2))
p = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if islands[i][j] != 0:
            p += 4-islands[i][j-1]-islands[i][j+1] - \
                islands[i-1][j]-islands[i+1][j]

print(p)
