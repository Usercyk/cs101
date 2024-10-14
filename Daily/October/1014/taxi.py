input()
kids = {1: 0, 2: 0, 3: 0, 4: 0}
for p in input().split():
    kids[int(p)] += 1
res = kids[4]+kids[3]+(kids[2]+1)//2 + \
    (max(kids[1]-(kids[3]+(kids[2]+1)//2*4-kids[2]*2), 0)+3)//4
print(res)
