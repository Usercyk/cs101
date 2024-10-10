n, q = map(int, input().split())
r = {}
for i in range(1, n+1):
    r[i] = []
flag = False
for _ in range(q):
    x, y = map(int, input().split())
    if flag:
        continue
    if x in r[y]:
        flag = True
    r[x].append(y)

print("Yes" if flag else "No")
