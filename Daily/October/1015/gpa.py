h = int(input())
m = int(input())

l = [(*map(float, input().split()),) for _ in range(m)]
l.sort(key=lambda x: x[0]*x[1], reverse=True)

cur = 2*h-0.5*m
res = 0
for p in l:
    if cur == 0:
        break
    t = min(5/p[0], cur)
    cur -= t
    res += t*p[0]*p[1]
print(f"{res:.1f}")
