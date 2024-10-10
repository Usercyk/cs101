n, q = map(int, input().split())
r = {}
for i in range(1, n+1):
    r[i] = []
flag = False
for _ in range(q):
    x, y = map(int, input().split())
    if flag:
        continue
    for z in r[y]:
        if x in r[z]:
            flag = True
            break
    r[x].append(y)

print("Yes" if flag else "No")
