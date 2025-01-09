n = int(input())
ab_max = 0
xa, xb = map(int, input().split())
p = []
for _ in range(n):
    p.append(tuple(map(int, input().split())))
p.sort(key=lambda x: x[0]*x[1])
ans = 0
amul = xa
for q in p:
    ans = max(ans, amul//q[1])
    amul *= q[0]
print(ans)
