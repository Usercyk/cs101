nar = (153, 370, 371, 407)
a, b = map(int, input().split())
res = []
for n in nar:
    if a <= n <= b:
        res.append(n)
if res:
    print(*res)
else:
    print("NO")
