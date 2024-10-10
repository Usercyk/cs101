input()
a = sorted(map(int, input().split()))
cur = []

for p in a:
    if not cur:
        cur.append(p)
        continue
    if cur[0] < p:
        cur.append(p)
        cur.pop(0)
        continue
    cur.append(p)

print(len(cur))
