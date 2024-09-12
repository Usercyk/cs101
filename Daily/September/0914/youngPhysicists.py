x, y, z = 0, 0, 0
for _ in range(int(input())):
    m, n, p = map(int, input().split())
    x += m
    y += n
    z += p
if x == 0 and y == 0 and z == 0:
    print("YES")
else:
    print("NO")
